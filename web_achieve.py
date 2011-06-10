from bottle import route, run, static_file, debug, template, default_app, request
import anydbm
import json

@route('/achieve/:username/:number')
def got_acheivement(username,number):
    user(username).achieve(number)

@route('/user/:username')
def userpage(username):
    u = user(username)
    
def get_db(name="achievers"):
    return anydbm.open(name, 'c')
    
class user():
    def __init__(self, name):
        self.db = get_db()
        self.acheivements = json.loads(self.db[name])
        self.name = name
    def achieve(number):
        self.db[self.name] = json.dumps(json.loads(db[self.name]) + [number])
        self.acheivements = json.loads(self.db[name])


if __name__ == '__main__':
    debug(True)
    run(host='localhost', port=8080, reloader=True)