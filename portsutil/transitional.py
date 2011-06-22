import json
import sys

class Old_Bep(object):
    def __init__(self, bep_name):
        self.data = {}
        self.braceranges = []
        self.end = 0
        self.bep = open(bep_name).readlines()
        for i, line in enumerate(self.bep):
            if self.end == len(self.bep) == i:
                break
            if "=" in line and "{" not in line:
                self.simple_line(line)
            elif '{' in line:
                self.complex_line(i, line)
    def simple_line(self, line):
        self.data.update([[w.strip() for w in line.split("=", 1)]])    
    def complex_line(self, i, line):
        if '}' in self.bep[i]:
            self.simple_line(line)
        else:
            self.end =self.end_brace(i)
            print i, self.end
            orig = self.bep[i:self.end]
            full = ' '.join(orig)
            k = full.split()[0] #BUILD/PATCH/INSTALL
            print full
            l = full[full.find("{"):self.end]
            v = [r.strip() for r in l.split('\n')][1:-1]
            self.data.update([(k,v)])
    def end_brace(self, i):
        for i2, x in enumerate(self.bep[i:]):
            if x.startswith("}"):
                return int(i2+i + 1)
if __name__ == '__main__':
    if sys.argv[1] == '-json':
        print json.dumps(Old_Bep(sys.argv[2]).data)
    print Old_Bep(sys.argv[1]).data
