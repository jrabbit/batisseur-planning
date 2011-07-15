from bottle import route, run, static_file, debug, template, default_app, request
from redish.client import Client
import json
import hashlib
import urlparse

@route('/achieve/:username/:number')
def got_achievement(username,number):
    user(username).achieve(int(number))

@route('/user/:username')
def userpage(username):
    u = user(username)
    return template("achievers.tpl", user=u.name, achievements=maketable(user.achievements))

@route('/register/:username/:email')
def mk_user(username, email):
    pass

@route('/json/:username')
def show_user(username):
    return user(username).achievements


def get_db():
    return Client()

@route('/')
@route('/index.html')
@route('/ranking/:number')
def index(number=5):
    top = getranks()
    html= ""
    for user, points in top:
        html = html + "<tr><td class='user'>%s</td> <td class='points'>%s</td></tr>" % (user, points)
    return template('scores.tpl', top=html, number=number)

def getranks():
    """Return sorted dict of users."""
    db = {x : sum(y) for x, y in get_db()['scores'].items()}
    q = lambda x: db[x[0]] # Do evil things to sort by values not keys
    return dict(sorted(db.items(), key=q))


@route("/favicon.ico")
def favicon():
    return css_static(favicon.png)

class user():
    #use real framework for registration? NO USER CONTENT EVER. Or allow users to set a gravatar.
    def __init__(self, name):
        self.db = get_db()
        self.name = name
        if self.name in self.db['scores']:
            self.achievements = self.db['scores'][self.name]['achievements']
        else:
            self.db['scores'][name] = {'achievements': 0}
            self.achievements = 0
        self.name = name
    def achieve(self, number):
        x = self.db['scores'][self.name]['achievements']
        x.append(number)
        self.achievements = self.db['scores'][self.name]['achievements']
    def set_avatar(self, email):
        self.db['scores'][self.name]['email'] = email
        options = {'d': 'wavatar', 'r':'pg'} #Default size is 80x80
        hashed = hashlib.md5(email.lower()).hexdigest()
        #urlunparse takes a 5-tuple
        url = urlparse.urlunparse(('http', 'www.gravatar.com', '/avatar/%s/' % hashed, None, urllib.urlencode(options), None))
        self.db['scores'][self.name]['avatar'] = url
    def get_avatar(self):
        return self.db['scores'][self.name]['avatar']
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
    run(host='localhost', port=8090, reloader=True)