from urllib2 import urlopen
import random
import string
def makenames():
    for x in range(5):
        name = names().next()
        print urlopen("http://localhost:8080/json/%s" % name)
def names():
    name = ""
    while len(name) < 5:
        name = name + random.choice(string.ascii_letters)
    yield name
if __name__ == '__main__':
    makenames()