#Achievements for haiku packages
import anydbm
import os
from urllib2 import urlopen

import haikunotify

def get_db(app="haikuports", name="achievements"):
    home = os.path.expanduser('~')
    directory = os.path.join(home,"config", "settings","haikuports")
    return anydbm.open(os.path.join(directory, name), 'c')


def web_acheive(username, number):
    urlopen("http://scoreboard.haiku-os.org/%s/%s" %(username, number))


def notify(ach):
    haikunotify.send_notification(ach, "You Acheived!")
