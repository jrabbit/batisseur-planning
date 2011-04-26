import os
import platform
from subprocess import *

if platform.system() != 'Haiku':
    print "This is for Haiku, not %s" %platform.system()
    raise OSError
    
def send_notification(message, title, kind="information", app="PyHaikuNotify", **kwargs):
    options = " --type %s --title %s --app %s" % (kind, title, app)
    for arg in kwargs:
        if arg in ['messageid', 'progress', 'timeout', 'icon', 'onClickApp', 'onClickFile', 'onClickRef','onClickArgv']:
            options += ' --%s %s' % (arg, kwargs[arg])
    #Do the notification
    print ['notify' ]+ [options]
    Popen(['notify']+ options.split() + message.split(), stdout=PIPE).communicate()


if __name__ == '__main__':
    send_notification("Testing", "Test")