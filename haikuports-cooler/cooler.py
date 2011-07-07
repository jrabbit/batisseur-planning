import urlparse
import os.path

def parse_uri(uri):
    "take a uri and give file"
    parsed = urlparse.urlparse(uri)
    return os.path(parsed.path)[-1]

def parse_rev(f):
    "We're going to assume we can parse it, if we fail we ask the user."
    def is_version(s):
        for i in s.split('.'):
            if i.isdigit():
                pass
            else:
                return False
        return True
    try:
        pkg_name = f.split('-')[0]
        if '.tar.gz' in f:
            version = f.split('.tar.gz')[0].split('-')[1]
        elif '.xz' in f:
            version = f.split('.xz')[0].split('-')[1]
        elif '.tar.bz2' in f:
            version = f.split('.tar.bz2')[0].split('-')[1]
        else:
            raise NameError
        if not is_version(version):
            raise ValueError
    except (NameError, ValueError) as e:
        # Mention VCS urls.
        pass