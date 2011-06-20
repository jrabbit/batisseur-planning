""" The Batisseur 'client' it's a twisted server 
but it runs on our clients' computers."""

import platform
import json
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory

__VERSION__ = 0.01

class drone_proto(Protocol):
    def connectionMade(self):
        json_send({'version': __VERSION__, 'os': platform.system(), 
        'revision': platform.platform()})
    def dataReceived(self, data):
        #Parse function calls
        obj = json_loads(data)
        if 'call' in obj:
            if 'args' in obj:
                args = eval(obj['args'])
                eval(obj['call'])(args)
            else:
                eval(obj['call'])()
    def json_send(self, obj):
        self.transport.write(json.dumps(obj) + "\r\n")
    


if __name__ == '__main__':
    factory = Factory()
    factory.protocol = drone_proto
    reactor.listenTCP(5383, factory)
    reactor.run()
