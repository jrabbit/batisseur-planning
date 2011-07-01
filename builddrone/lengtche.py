import urllib
import json
import sys
from daemon import Daemon

class leng_tche(Daemon):
    def run(self):
        while 1:
            #Query the builddrone queen.
            u = urllib.urlopen("http://%s/jobs" % "192.168.1.45") #TODO remove ip
            data = json.loads(u)
            

    def do_we_want(self, job):
        """This will allow users to not compile some dev's packages
        i.e. Mr. rm -rf"""
        return True

if __name__ == '__main__':
    ourdaemon = leng_tche('/boot/home/config/settings/Builddrone_pid')
    if sys.argv[1] == "-d":
        ourdaemon.start()
    elif sys.argv[1] == "-s":
        ourdaemon.stop()
    else:
        ourdaemon.run()