from subprocess import PIPE, Popen, check_output, call

def haikuporter_build(package):
    return Popen(['haikuporter', '-g', '-v', '-y', '-c', '-d', package], stdout=PIPE).communicate()

def haikuporter_tree():
    return check_output(['haikuporter','-t'], stdout=PIPE)

def setgcc(version):
    if version != 4 or 2:
        raise ValueError
    else:
        call(['setgcc' 'gcc%s' % str(version)])