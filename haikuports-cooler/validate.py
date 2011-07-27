import altparse
from validate_constants import *

def validate_single_bep(beppath):
    "Simplify, simplify, simplify. The caller can handle errors."
    bepKeys = altparse.file_to_dict(beppath)
    for key in bep_defaults:
        if key not in bepKeys and bep_defaults[key][0]:
            raise ValueError
    for key in bepKeys:
        try:
            if type(bepKeys[key]) not in bepTypes[key]:
                raise TypeError
        except KeyError, e:
            print "Warning: Unknown key label '" + key
    if 'LICENSE' in bepKeys:
        check_license(bepKeys)
    if 'LICENSE' not in bepKeys or not bepKeys['LICENSE']:
        print 'Warning: No LICENSE found in bep file'
    if 'COPYRIGHT' not in bepKeys or not bepKeys['COPYRIGHT']:
        print 'Warning: No COPYRIGHT found in bep file'

def check_license(bepKeys):
    fileList = []
    bepLicense = []
    if type(bepKeys['LICENSE']) == type(str()):
        bepLicense.append(self.bepKeys['LICENSE'])
    else:
        bepLicense = self.bepKeys['LICENSE']
    for item in bepLicense:
        dirname = findDirectory('B_SYSTEM_DIRECTORY', 'data/licenses')
        for filename in os.listdir(dirname):
            fileList.append(filename)
        haikuLicenseList = fileList
        if item not in fileList:
            fileList = []
            dirname = os.path.dirname(bepFilePath) + '/licenses'
            print 'Try looking in ' + dirname
            if os.path.exists(dirname):
                for filename in os.listdir(dirname):
                    fileList.append(filename)
        if item not in fileList:
            print ('\n######## Error: No match found for License %s '
                   '########\n' % item)
            print 'Valid license filenames included with Haiku are: '
            print haikuLicenseList
            print '\n'
        else:
            print 'Matching License (%s) found in %s' % (item, dirname)
