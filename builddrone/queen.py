# Recieves post-push information from github/etc and communicates the new versions and blob refs.
# Upload to Camlistore with git info, this allows users to vouch for it.
import time
import json
import os
import random
import uuid

from redish.client import Client
from bottle import error, route, run, static_file, debug, template, default_app, request, post

@route('/jobs')
def availible_jobs(name="All"):
    db = get_db()
    if name is not "All":
        q = dict(db[name]) #force json?
        q['meta-name'] = name
        return q
    else:
        pass

@route('/pkg/:name')
def named_pkg(name):
    return availible_jobs(name=name)        

@post('/commit/:pkg')
def github_hook(pkg):
    payload = request.forms.get('payload')
    d = json.loads(payload)
    new_commit(d['repository']['name'], d)

def new_commit(name, payload):
    db = get_db()
    if name not in db.keys():
        pass
    else:
        branch = payload['ref'][11:]
        db[name]['revs'][branch]['last-commit'] = (time.time(), payload['commits'][0]['id'])
        #Tuple of time of commit and commit ID.
        db[name]['revs'][branch][payload['commits'][0]['id']] = {'Builds': 0} # Never been built.

def mk_id(name, arch, gcc, length):
    u = uuid.uuid4().hex[:length] #This reduces the uniqueness but makes better urls
    jobid = name +'-'+ arch +'-'+ gcc +'-'+ u
    return jobid

@route("/completed/:job_id/:blobref")
def recieve_blob(job_id, blobref):
    get_db()['jobs'][job_id] = {'status': 'completed', 'blob': blobref}

@route("/blob/:job_id")
def give_blob(job_id):
    return get_db()['jobs'][job_id]['blob']

@error(404)
def error404(e):
    img = random.choice([x for x in os.listdir('css/neko100') if x[0] != '.']) 
    # I have a .DS_Store from OSX might have other weird stuff on other platforms
    return "<!DOCTYPE html><html><head><title>Error 404: Cat Found</title></head><body style='text-align:center;'><img src='/css/neko100/%s'><p><a href='http://www.cavestory.org/othergames_neko100.php'>src</a></p></body></html>" % img
def get_db():
    return Client()

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
    run(host='192.168.1.45', port=8080, reloader=True)