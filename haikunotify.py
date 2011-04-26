import os
import platform
from subprocess import *

if platform.system() is not 'Haiku':
    raise OSError
    
def send_notification(message, title, kind="information", app="PyHaikuNotify", **kwargs):
    if not icon:
        icon = "`finddir B_SYSTEM_APPS_DIRECTORY`/AboutSystem"
    options = " --type %s --title %s --app %s" % (kind, title, app)
    for arg in kwargs:
        if arg in ['messageid', 'progress', 'timeout', 'icon', 'onClickApp', 'onClickFile', 'onClickRef','onClickArgv']:
            options += ' --%s %s' % (arg, kwargs[arg])
    
    #Do the notification
    Popen(['notify' ]+ [options] + [message], stdout=PIPE).communicate()


if __name__ == '__main__':
    send_notification("Testing", "Test")