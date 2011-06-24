# Recieves post-push information from github/etc and communicates the new versions and blob refs.
# Upload to Camlistore with git info, this allows users to vouch for it.
import time
import json
from redish.client import Client
from bottle import route, run, static_file, debug, template, default_app, request, post
# import camli.op
# TODO: How to share blob refs sanely? [Simple http/json]
# def upload_files(op, path_list):
#   """Uploads a list of files Args:
#     op: The CamliOp to use.
#     path_list: The list of file paths to upload."""
#   real_path_set = set([os.path.abspath(path) for path in path_list])
#   all_blob_files = [open(path, 'rb') for path in real_path_set]
#   logging.debug('Uploading blob paths: %r', real_path_set)
#   op.put_blobs(all_blob_files)

@route('/jobs')
def availible_jobs(name="All"):
    if name is not "All":
        return jobs[name]
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
        db['name']['last-commit'] = time.time()
        db['name']['revs'][payload['commits'][0]['id']] = {'Builds': 0} # Never been built.

def get_db():
    return Client()

class Job(object):
    def __init__(self, name, database):
        self.start =  time.localtime()
        self.name = name
        self.database = database
        self.vcs = self.lookup_vcs(name)
    def __setattr__(self, name, value):
        self.database[name] = value
    def __getattr__(self,name):
        try:
            return self.database[name]
        except:
             raise AttributeError
    def __delattr__(self, name):
        del self.database[name]
    def lookup_vcs(self, name):
        "Which VCS does the build use?"
        d = self.database
        if name in d['vcs']:
            return d['vcs'][name]
        else:
            return "haikuports"
        #This is the VCS of the development/source of the package 
        #not of the software within
        #Gorram Brecht, we needed that parser for real beps.
    

if __name__ == '__main__':
    run(host='192.168.1.45', port=8080, reloader=True)