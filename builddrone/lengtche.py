import urllib
import json
import sys
import time
import util
from daemon import Daemon

class leng_tche(Daemon):
    def run(self):
        while 1:
            #Query the builddrone queen.
            if time.time() - self.lastrun > 60*5 and self.notbuilding
                u = urllib.urlopen("http://%s/jobs" % "192.168.1.45") #TODO remove ip
                data = json.loads(u)
                if data['vcs'] == "haikuports":
                    do_haikuport(data['meta-name'])       
                self.lastrun = time.time()
                self.notbuilding = True
            else:
                pass
    def do_haikuport(self, name):
        self.notbuilding = False
        popen_data = util.haikuporter_build(name)
        #Popen.communicate() returns a tuple (stdoutdata, stderrdata).
        return popen_data

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