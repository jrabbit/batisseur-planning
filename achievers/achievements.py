#Achievements for haiku packages
import anydbm
import os
from urllib2 import urlopen

import haikunotify

achievements = [{'name': 'Failure', 'desc': 'Had a build fail'},
{'name': 'Expansionist', 'desc': 'Installed a package'},
{'name': 'Iron-fisted Ruler', 'desc': 'Forced a build'},
{'name': 'Curiousity Killed The Cat', 'desc': 'Inquired about a package using -a'},
{'name': 'Zip Trafficker', 'desc': 'Built a zip for distrobution using -d'},
{'name': 'Shredder-9000', 'desc': "I'm sorry I can't let you do that.\n Automated a build with -y"},
{}]

def get_db(app="haikuports", name="achievements"):
    home = os.path.expanduser('~')
    directory = os.path.join(home,"config", "settings","haikuports")
    return anydbm.open(os.path.join(directory, name), 'c')


def web_achieve(username, number):
    urlopen("http://scoreboard.haiku-os.org/%s/%s" %(username, number))


def notify(ach):
    haikunotify.send_notification(ach, "You Acheived!")
