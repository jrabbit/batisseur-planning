from bottle import route, run, static_file, debug, template, default_app, request
import anydbm
import json

@route('/achieve/:username/:number')
def got_acheivement(username,number):
    user(username).achieve(number)

@route('/user/:username')
def userpage(username):
    u = user(username)

@route('/json/:username')
def show_user(username):
    return user(username).achievements

def get_db(name="achievers"):
    return anydbm.open(name, 'c')
    
class user():
    # Todo use real framework for registration? Or allow users to set a gravatar.
    def __init__(self, name):
        self.db = get_db()
        if name in self.db:
            self.acheivements = json.loads(self.db[name])
        else:
            self.db[name] = json.dumps(False)
            self.acheivements = 0
        self.name = name
    def achieve(number):
        self.db[self.name] = json.dumps(json.loads(db[self.name]) + [number])
        self.acheivements = json.loads(self.db[name])



@route('/js/:filename')
def js_static(filename):
    return static_file(filename, root='./js')
@route('/css/:filename#.+#')
def css_static(filename):
    return static_file(filename, root='./css')

if __name__ == '__main__':
    debug(True)
    run(host='localhost', port=8080, reloader=True)