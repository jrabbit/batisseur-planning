import time
import iso8601

class BB_Commit():
    "Abstraction class for handling a bitbucket POST hook"
    def __init__(self, p):
        self.payload = p
        #Metadata
        self.url = p['canon_url'] + p['repository']['absolute_url']
        self.name = p['repository']['name']
        #Commit id(s), (branch , (commit-sha, unix_time))
        self.commits = [( x['branch'] ,(x['node'], time.mktime(time.strptime(x['timestamp'], "%Y-%m-%d %H:%M:%S")))) for x in p['commits']]    
    
    def is_single_commit(self):
        "Does commits contain only one element. API consumers can simplify code then."
        if len(self.payload['commits']) == 1:
            return True
        else:
            return False

class Github_Commit():
    "Abstraction class to match bitbucket one."
    def __init__(self, p):
        self.payload = p
        # Metadata 
        self.url = p['repository']['url']
        self.name = p['repository']['name']
        #Commit ids (branch, (commit-sha, unix_time))
        self.commits = [((p['ref'][11:]), (x['id'], time.mktime(iso8601.parse_date(x['timestamp']).timetuple()))) for x in p['commits']]
    def is_single_commit(self):
        "This may the the only similar thing between these hooks."
        if len(self.payload['commits']) == 1:
            return True 
        else:
            return False
    

        
        