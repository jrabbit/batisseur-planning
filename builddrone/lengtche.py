import urllib
import json
import sys
import time

import jenkins
import util
from daemon import Daemon

class leng_tche(Daemon):
    def run(self):
        while 1:
            #Query the builddrone queen.
            if time.time() - self.lastrun > 60*5 and self.notbuilding
                u = urllib.urlopen("http://%s/jobs" % "192.168.1.45") #TODO remove ip
                data = json.loads(u)
                self.lastrun = time.time()
                if data['vcs'] == "haikuports":
                    report_build(do_haikuport(data['meta-name']))      
                
                self.notbuilding = True
            else:
                pass
    def do_haikuport(self, name):
        self.notbuilding = False
        popen_data = util.haikuporter_build(name)
        #Popen.communicate() returns a tuple (stdoutdata, stderrdata).
        return popen_data, name

    def report_build(self, build_data, name):
        duration = time.time() - self.lastrun
        if  build_data[1]:
            log = build_data[0] + "\n STDERROR: \n" + build_data[1]
        else:
            log = build_data[0]
        result = jenkins.runResult(log, "Success?", duration)
        result.send("192.168.1.45", name)
        
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