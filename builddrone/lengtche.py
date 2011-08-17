import urllib
import json
import sys
import time
import os
import ftplib

import camli.op

import jenkins
import util
from daemon import Daemon

class leng_tche(Daemon):
    def run(self):
        self.lastrun = 0
        self.notbuilding = True
        while 1:
            #Query the builddrone queen.
            if time.time() - self.lastrun > 60*5 and self.notbuilding:
                u = urllib.urlopen("http://%s/jobs" % util.conf()['queen']['url']) #TODO: ask for GCC/arch jobid
                #TODO care about user prefrence on arch
                data = json.loads(u)
                self.lastrun = time.time()
                if data['vcs'] == "haikuports":
                    self.package_id = data['jobid']
                    build_info = do_haikuport(data['meta-name'])
#Haikuports may or may not reccomend to build source archive as last line depending if GPL'd
                    for l in build_info[0][0].splitlines()[-2:]:
                        if l[-4:] == '.zip':
                            self.store_zip(l.split()[-1], build_info[1], data['jobid'])
                    self.report_build(build_info) #Send to jenkins.
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
        result.send(util.conf()['jenkins']['url'], name)
    
    def do_we_want(self, job):
        """This will allow users to not compile some dev's packages
        i.e. Mr. rm -rf"""
        return True
        
    def store_zip(self, zip_loc, name, job_id):
        conf = util.conf()['camli']
        op = camli.op.CamliOp(conf['url'], auth=conf['auth'], basepath=conf['basepath'])
        blobref = op.put_blobs([open(zip_loc)]) #list does matter
        if len(blobref) == 1:
            blobref_clean = blobref.pop()
        else:
            raise ValueError("Multiple blobrefs!")
        self.tell_queen(blobref_clean, name, job_id)
    
    def store_ftp(self, zip_loc, name, job_id):
        "optional fall back if camlistore doesn't pan out"
        conf = util.conf()['ftp']
        f = ftplib.FTP_TLS(conf['ftp_host']) #We don't actually want to upload here
        f.login() #Anonymous login
        f.prot_p() #secure the line
        f.cwd(os.path.join(conf['remotepath'], name))
        f.storbinary("STOR %s" % os.path.split(zip_loc)[1], open(zip_loc))
        
    def tell_queen(self, blobref, name, job_id):
        urllib.urlopen("http://%(server)s/completed/%(job_id)s/%(blobref)s" \
        % {'server': util.conf()['queen']['url'], 'job_id': job_id, 'blobref': blobref})
        
if __name__ == '__main__':
    ourdaemon = leng_tche('/boot/home/config/settings/build_drone/Builddrone_pid')
    if len(sys.argv) > 1:
        if sys.argv[1] == "-d":
            ourdaemon.start()
        elif sys.argv[1] == "-s":
            ourdaemon.stop()
    else:
        ourdaemon.run()