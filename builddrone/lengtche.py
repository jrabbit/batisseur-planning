import urllib
import json
import sys
import time

import camli.op

import jenkins
import util
from daemon import Daemon

class leng_tche(Daemon):
    def run(self):
        while 1:
            #Query the builddrone queen.
            if time.time() - self.lastrun > 60*5 and self.notbuilding:
                u = urllib.urlopen("http://%s/jobs" % "192.168.1.45") #TODO remove ip
                data = json.loads(u)
                self.lastrun = time.time()
                if data['vcs'] == "haikuports":
                    self.package_id = data['jobid']
                    build_info = do_haikuport(data['meta-name'])
                    #Haikuports may or may not reccomend to build source archive as last line depending if GPL'd
                    for l in build_info[0][0].splitlines()[-2:]:
                        if l[-4:] == '.zip':
                            store_zip(l.split()[-1], build_info[1], data['job-id'])
                    report_build(build_info) #Send to jenkins.
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
        
    def store_zip(self, zip_loc, name, job_id):
        op = camli.op.CamliOp("192.168.1.45", 'pass3179')
        blobref = op.put_blobs(file(zip_loc))
        tell_queen(blobref, name, job_id)
        
    def tell_queen(self, blobref, name, job_id):
        urllib.urlopen("http://%(server)s/completed/%(job_id)s/%(blobref)s" \
        % {'server': "192.168.1.45", 'job_id': job_id, 'blobref': blobref}) #TODO remove ip
        
if __name__ == '__main__':
    ourdaemon = leng_tche('/boot/home/config/settings/Builddrone_pid')
    if sys.argv[1] == "-d":
        ourdaemon.start()
    elif sys.argv[1] == "-s":
        ourdaemon.stop()
    else:
        ourdaemon.run()