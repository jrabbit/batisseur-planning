import platform

from txjsonrpc.web import jsonrpc
from twisted.web import server
from twisted.internet import reactor

__VERSION__ = 0.01

class build_drone(jsonrpc.JSONRPC):
    def jsonrpc_hostinfo():
        return {'version': __VERSION__, 'os': platform.system(), 
        'revision': platform.platform()}
    

if __name__ == '__main__':
    reactor.listenTCP(5383, server.Site(build_drone()))
    reactor.run()