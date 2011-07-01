import urllib
import json
import sys
from daemon import Daemon

class leng_tche(Daemon):
    def run(self):
        while 1:
            #Query the builddrone queen.
            pass
if __name__ == '__main__':
    ourdaemon = leng_tche('/boot/home/config/settings/builddrone.pid')
    if sys.argv[1] == "-d":
        ourdaemon.start()
    else:
        ourdaemon.run()