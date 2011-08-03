import platform
if platform.python_version_tuple()[:2] == ('2', '6'):
    from subprocess import PIPE, Popen, call
else:
    from subprocess import PIPE, Popen, check_output, call
    
def haikuporter_build(package, clean=False):
    if clean:
        return Popen(['haikuporter', '-y', '-c', '-d', package], stdout=PIPE).communicate()
    else:
        return Popen(['haikuporter', '-y', '-d', package], stdout=PIPE).communicate()

def haikuporter_tree():
    if check_output:
        #requires python 2.7
        return check_output(['haikuporter','-t'], stdout=PIPE)
    else:
        pass

def setgcc(version):
    if version != 4 or 2:
        raise ValueError
    else:
        call(['setgcc' 'gcc%s' % str(version)])
