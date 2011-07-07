import sys
from optparse import OptionParser
from subprocess import PIPE, Popen

def handle_new():
    pass


def handle(args):
    arg_list = ['force', 'install', 'get', 'tree', 'lint', 'search', 'yes', 'archive', 'about', 'list', 'patch', 'build', 'clean', 'test', 'distro']
    arg_dict = dict((opt, getattr(args, str(opt))) for opt in arg_list)
    # achieve(arg_dict)

def endofrun(process):
    # If this doesn't work tee into a temp file and read it for data.
    n, k  = itertools.tee(process.stdout)
    for l in n:
        print l
    v, d = itertools.tee(process.stderr)
    for i in v:
        print i
    exit(k, d, process.returncode)
    

def exit(stdout, stderr, exitcode):
    # TODO: Achieve failure from exiting.
    print stdout, stderr, exitcode

if __name__ == '__main__':
    # taken from haikuporter
    parser =  OptionParser(usage='usage: %prog [options] portname[-portversion]',
                           version='%prog ')
    parser.add_option('-l', '--list', action='store_true', dest='list',
                      default=False, help='list available ports')
    parser.add_option('-a', '--about', action='store_true', dest='about',
                      default=False, help='show description of the specified port')
    parser.add_option('-s', '--search', action='store_true', dest='search',
                      default=False, help='search for a port (regex)')
    parser.add_option('-p', '--nopatch', action='store_false', dest='patch',
                      default=True, help="don't patch the sources, just download "
                                         "and unpack")
    parser.add_option('-b', '--nobuild', action='store_false', dest='build',
                      default=True, help="don't build the port, just download, "
                                         "unpack and patch")
    parser.add_option('-i', '--install', action='store_true', dest='install',
                      default=False, help="also install the port (the default is "
                                          "to only build)")
    parser.add_option('-d', '--distro', action='store_true', dest='distro',
                      default=False, help="make distribution package of the "
                                          "specified port (include download, "
                                          "unpack, patch, build)")
    parser.add_option('-c', '--clean', action='store_true', dest='clean',
                      default=False, help="clean the working directory of the "
                                          "specified port")
    parser.add_option('-g', '--get', action='store_true', dest='get',
                      default=False, help="get/update the ports tree")
    parser.add_option('-f', '--force', action='store_true', dest='force',
                      default=False, help="force to perform the steps (unpack, "
                                          "patch, build)")
    parser.add_option('-z', '--archive', action='store_true', dest='archive',
                      default=False, help="Create a patched source archive as "
                                          "<package>_haiku.tar.xz")
    parser.add_option('-t', '--tree', action='store_true', dest='tree',
                      default=False, help="print out the location of the "
                                          "haikuports source tree")
    parser.add_option('-y', '--yes', action='store_true', dest='yes',
                      default=False, help="answer yes to all questions")

    parser.add_option('--test', action='store_true', dest='test',
                      default=False, help="run tests on resulting binaries")
    parser.add_option('--lint', action='store_true', dest='lint',
                      default=False, help="scan the ports tree for problems")
    handle(parser.parse_args()[0])
    endofrun(Popen(['haikuporter'] + sys.argv[1:], stdout=PIPE, stderr=PIPE))