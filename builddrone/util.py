import platform
import tempfile
import json
import os

try:
    import gnupg
except ImportError:
    pass

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

def sign_json(jsono):
    json_object = json.dumps(jsono)
    if json_object[-1] == '}':
        trimmed = json_object.rstrip()[:-1]
    else:
        raise ValueError
    # trim_file = open(tempfile.mkstemp()[1], 'wb')
    # trim_file.write(trimmed)
    # trim_file.name
    #gpg --detach-sign --local-user=54F8A914 --armor -o  signing-before.camli (trimmed)
    if not gnupg:
        pass
    else:
        gpg = gnupg.GPG()
        # Todo: use specific keys
        signature = gpg.sign(trimmed, detach=True)
        thegoodparts = ''.join(signature.data.splitlines()[3:-1])
        signed_json = trimmed + ',"camliSig":"%s"}\n' % thegoodparts
        return signed_json #this is a string.
def verify_json(jsonstr):
    payload, sep, signature = jsonstr.partition(',"camliSig":"')
    #make the payload real json.
    payload = payload + "}"
    sign_block = json.loads('{' + sep[1:] + signature) #reconstruct json.
    sign = sign_block['camliSig']
    #todo finish verification after seeing actual share blobs.
def conf():
    "Return configuration dict for the builddrone client (leng tche)"
    home = os.path.expanduser('~')
    options = open("%s/config/settings/build_drone/options.json" % home)
    return json.load(options)