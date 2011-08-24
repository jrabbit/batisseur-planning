#!/usr/bin/env python
import sys
from subprocess import PIPE, Popen, call
import urllib2
import urllib
import json

QUEEN_ADRESS = "http://192.168.1.45:8080/commit_haikuports"

def send_hook(payload):
    urllib2.urlopen(QUEEN_ADRESS, urllib.urlencode({'payload': json.dumps(payload)}))

def main(location, revision):
    out, err = Popen(['svn', 'log', '-v' ,'-r', revision] cwd=location, stdout=PIPE).communicate()
    paths = []
    for x in out.splitlines():
        if x and x.strip()[0] in ['M', 'A']:
            paths.append(x.strip())
    beps = [x for x in paths if x.split('.')[-1] == 'bep']
    payload = {'commits':{}, 'revision': revision}
    for bep in beps:
        branch = bep.split("/")[2]
        name = '.'.join(bep.split("/")[-1].split('.')[0:-1])
        c = payload['commits'][name.split('-')[0]]
        try:
            c.append({'branch': branch, 'version': name})
        except KeyError:
             c = [{'branch': branch, 'version': name}]
             
    send_hook(payload)


if __name__ == '__main__':
    main(sys.argv[0], sys.argv[1])