# Recieves post-push information from github/etc and communicates the new versions and blob refs.
# Upload to Camlistore with git info, this allows users to vouch for it.
import time
from bottle import route, run, static_file, debug, template, default_app, request
import camli.op
# TODO: How to share blob refs sanely? [Simple http/json]
def upload_files(op, path_list):
  """Uploads a list of files Args:
    op: The CamliOp to use.
    path_list: The list of file paths to upload."""
  real_path_set = set([os.path.abspath(path) for path in path_list])
  all_blob_files = [open(path, 'rb') for path in real_path_set]
  logging.debug('Uploading blob paths: %r', real_path_set)
  op.put_blobs(all_blob_files)

@route('/jobs')
def availible_jobs(name="All"):
    if name is not "All":
        return jobs[name]
    pass

@route('/pkg/:name')
def named_pkg(name):
    return availible_jobs(name=name)        
        
class Job():
    def __init__(self, name):
        self.start = 