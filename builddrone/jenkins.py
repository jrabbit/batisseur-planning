#Submit a jenkins run
#https://wiki.jenkins-ci.org/display/JENKINS/Monitoring+external+jobs

import urllib2

class runResult():
    def __init__(log, result, duration):
        self.log = log.encode("hex")
        self.xml = \
        """<run>
          <log encoding="hexBinary">%s</log>
          <result>%d</result>
          <duration>%d</duration>
        </run>
        """ %(self.log,result,duration)
    
    def send(host, job):
        return urllib2.urlopen("http://%s/jenkins/job/%s/postBuildResult" \
        %(host, job), data=self.xml)
