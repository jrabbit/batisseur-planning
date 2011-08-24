# Recieves post-push information from github/etc and communicates the new versions and blob refs.
# Upload to Camlistore with git info, this allows users to vouch for it.
import time
import json
import os
import random
import uuid
import atexit
import cPickle

from bottle import error, route, run, static_file, debug, template, default_app, request, post

import hooks

@route('/jobs')
def availible_jobs(name="All"):
    db = get_db()
    if name is not "All":
        q = dict(db[name]) #force json?
        arch = request.GET.get('arch') #?arch=i368&gcc=gcc4
        gcc = request.GET.get('gcc')
        if not arch:
            arch = 'i368'
        if not gcc:
            gcc = 'gcc4'
        q['meta-name'] = name
        q['jobid'] = mk_id(name, arch, gcc, 6) 
        return q
    else:
        x = db.copy()
        if 'jobs' in x:
            del x['jobs'] # This returns the database minus the jobs storage.
        return x

# @route('/get_job')
@route('/pkg/:name')
def named_pkg(name):
    return availible_jobs(name=name)        

@post('/commit/:pkg')
@post('/commit_github/:pkg')
def github_hook(pkg):
    payload = request.forms.get('payload')
    d = json.loads(payload)
    new_commit(pkg, hooks.Github_Commit(d))

@post('/commit_bitbucket/:pkg')
def bitbucket_hook(pkg):
    payload = request.forms.get('payload')
    d = json.loads(payload)
    new_commit(pkg, hooks.BB_Commit(d))

@post('/commit_haikports')
def haikuports_hook():
    payload = request.forms.get('payload')
    d = json.loads(payload)
    h = hooks.Haikuports_Commit(d)
    for k in h.commits:
        dumby = Dumby_Commit( ('hp-trunk', (k['sha'], time.time()) )
        new_commit(k['name'], dumby)

def new_commit(name, commits):
    db = get_db()
    if name not in db.keys():
        pass
    if name not in db:
        db[name] = {}
        db[name]['revs'] = {}
    else:
        #Tuple (branch , (commit-sha, unix_time))
        for commit in commits.commits: 
            #Tuple of time of commit and commit ID.
            db[name]['revs'][commit[0]] = {}
            db[name]['revs'][commit[0]]['last-commit'] = (commit[1][1], commit[1][0])
            db[name]['revs'][commit[0]][commit[1][0]] = {'Builds': 0}

def mk_id(name, arch, gcc, length=6):
    u = uuid.uuid4().hex[:length] #This reduces the uniqueness but makes better urls
    jobid = name +'-'+ arch +'-'+ gcc +'-'+ u
    return jobid

@post('/completed')
def recieve_blob():
    db = get_db()
    info = json.loads(request.forms.get('json'))
    if 'jobs' not in  get_db():
        get_db()['jobs'] = {}
    db['jobs'][info['job_id']] = {'status': 'completed', 'blob': info['blobref'], 'date': time.time()}
    which = db[info['project']]['revs'][info['branch']][info['sha']]
    which['Builds'] += 1
    if 'Jobs' in which:
        which['Jobs'].append(info['job_id'])
    else:
        which['Jobs'] = [info['job_id']]


@route("/blob/:job_id")
def give_blob(job_id):
    return get_db()['jobs'][job_id]['blob']

@error(404)
def error404(e):
    img = random.choice([x for x in os.listdir('css/neko100') if x[0] != '.']) 
    # I have a .DS_Store from OSX might have other weird stuff on other platforms
    return "<!DOCTYPE html><html><head><title>Error 404: Cat Found</title></head><body style='text-align:center;'><img src='/css/neko100/%s'><p><a href='http://www.cavestory.org/othergames_neko100.php'>src</a></p></body></html>" % img
@route('/css/:filename#.+#')
def css_static(filename):
    return static_file(filename, root='./css')
    

def get_db():
    return our_db

def close_pickle(db):
    with open('data.pkl', 'wb') as f:
        cPickle.dump(db, f)

class Job(object):
    def __init__(self, name, database):
        self.start =  time.localtime()
        self.name = name
        self.database = database
        self.vcs = self.lookup_vcs()
    def __setattr__(self, key, value):
        self.database[self.name][key] = value
    def __getattr__(self,key):
        try:
            return self.database[self.name][key]
        except:
             raise AttributeError
    def __delattr__(self, key):
        del self.database[self.name][key]
    def give(self):
        "Yield an actionable job?"
        ids = []
        for branch in self.database[self.name]:
            br = self.database[self.name]['revs'][branch]
            ids = ids + [rev for rev in br if br[rev]['Builds'] == 0]
        return ids
    def lookup_vcs(self):
        "Which VCS does the build use?"
        d = self.database
        if self.name in d['vcs']:
            return d['vcs'][self.name]
        else:
            return "haikuports"
        #This is the VCS of the development/source of the package 
        #not of the software within
        #Gorram Brecht, we needed that parser for real beps.
    

if __name__ == '__main__':
    debug(True)
    try:
        with open('data.pkl', 'rb') as our_file:
            our_db = cPickle.load(our_file)
    except EOFError:
        our_db = {}
    atexit.register(close_pickle, our_db)
    run(host='192.168.1.45', port=8080, reloader=True)