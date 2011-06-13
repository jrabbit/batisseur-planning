from urllib2 import urlopen
from tempfile import _RandomNameSequence

def makenames():
    randomnames = []
    for x in _RandomNameSequence():
        if len(randomnames) < 7:
            randomnames.append(x) 
    for name in randomnames:
        urlopen("http://localhost:8080/json/%s" % name)
if __name__ == '__main__':
    makenames()