from urllib2 import urlopen
from tempfile import _RandomNameSequence

def makenames():
    randomnames = []
    for x in names():
        if len(randomnames) < 7:
            randomnames.append(x) 
    for name in randomnames:
        print urlopen("http://localhost:8080/json/%s" % name)
def names():
    characters = ("abcdefghijklmnopqrstuvwxyz" +
                  "ABCDEFGHIJKLMNOPQRSTUVWXYZ" +
                  "0123456789_")
    name = ""
    while len(name) < 5:
        ''.join(random.choice(characters))
    yield name
if __name__ == '__main__':
    makenames()