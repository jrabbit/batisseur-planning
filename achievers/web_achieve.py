from bottle import route, run, static_file, debug, template, default_app, request
import anydbm
import json

@route('/achieve/:username/:number')
def got_acheivement(username,number):
    user(username).achieve(int(number))

@route('/user/:username')
def userpage(username):
    u = user(username)
    return template("achievers.tpl", user=u.name, acheivements=maketable(user.achievements))
    def maketable(obj):
        # TODO: Is there a html table generator?
        pass

@route('/json/:username')
def show_user(username):
    return user(username).achievements

def get_db(name="achievers"):
    return anydbm.open(name, 'c')

@route('/')
@route('/index.html')
@route('/ranking/:number')
def index(number=5):
    top = getranks()[:int(number)]
    return template('scores.tpl', top)

def getranks():
    """Return sorted dict of users."""
    db = {x : sum(json.loads(y)) for x, y in get_db().items()}
    q = lambda x: db[x[0]] # Do evil things to sort by values not keys
    return dict(sorted(db.items(), key=q))


@route("/favicon.ico")
def favicon():
    return css_static(favicon.png)

class user():
    # Todo use real framework for registration? Or allow users to set a gravatar.
    def __init__(self, name):
        self.db = get_db()
        self.name = name
        if name in self.db:
            self.achievements = json.loads(self.db[name])
        else:
            self.db[name] = json.dumps([0])
            self.achievements = 0
        self.name = name
    def achieve(self, number):
        x = json.loads(self.db[self.name])
        x.append(number)
        self.db[self.name] = json.dumps(x)
        self.acheivements = json.loads(self.db[self.name])

@route('/js/:filename')
def js_static(filename):
    return static_file(filename, root='./js')
@route('/css/:filename#.+#')
def css_static(filename):
    return static_file(filename, root='./css')

if __name__ == '__main__':
    
    @route('/db')
    def debug_db():
        return dict(get_db())
    debug(True)
    run(host='localhost', port=8080, reloader=True)