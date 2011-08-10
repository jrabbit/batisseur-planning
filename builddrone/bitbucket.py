import time

class BBCommit():
    "Abstraction class for handling a bitbucket POST hook"
    def __init__(self, payload):
        self.payload = payload
        #Metadata
        self.url = payload['canon_url'] + payload['repository']['absolute_url']
        self.name = payload['repository']['name']
        #Commit id(s), (commit-sha, unix_time)
        self.commits = [(x['node'], time.mktime(time.strptime(x['timestamp'], "%Y-%m-%d %H:%M:%S"))for x in payload['commits'] ]    
    def is_single_commit(self):
        "Does commits contain only one element. API consumers can simplify code then."
        if len(self.payload['commits']) == 1:
            return True
        else:
            return False
    