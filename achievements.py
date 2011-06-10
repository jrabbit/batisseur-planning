#Achievements for haiku packages
import anydbm
import os
import haikunotify

def get_db(app="haikuports", name="achievements"):
    home = os.path.expanduser('~')
    directory = os.path.join(home,"config", "settings","haikuports")
    return anydbm.open(os.path.join(directory, name), 'c')


def acheive():
    pass

def notify(ach):
    haikunotify.send_notification(ach, "You Acheived!")
    # TODO: notfiy the website.