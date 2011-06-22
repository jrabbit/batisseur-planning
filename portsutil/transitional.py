import json
import sys
# class New_Bep(object):
#     def __init__(self, bep):
#         self.data = {}
#         for line in bep:
#             if "=" in line:
#                 self.data.update([line.split("=")])
# The old/new seem to just be different in building 
# this is no problem for parse, only emitting

class Old_Bep(object):
    def __init__(self, bep_name):
        self.data = {}
        self.bep = bep_name
        for i, line in enumerate(self.bep):
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
            print i, self.end_brace(i)
            orig = self.bep[i:self.end_brace(i)]
            full = ' '.join(orig)
            print full.split()
            k = full.split()[0] #BUILD/PATCH/INSTALL
            print k 
            l = full[full.find("{"):full.find("}")+1]
            v = [r.strip() for r in l.split('\n')][1:-1]
            self.data.update([(k,v)])
    def end_brace(self, i):
        print 'end_brace called'
        openBr = "magic"
        i2 = 0
        openBr = 0
        for internal, line in enumerate(self.bep[i-1:]):
            if openBr == 0:
                i2 = internal
                return (i2+i+1) #this is the last line of the {} block.
                break
            if line.find("{"):
                openBr +=1
                print "Increased Braces: %s" %openBr
            if line.find("}"):
                openBr -=1
                print "Decreased Braces: %s" %openBr
            print "Enum: %s" % internal
        

if __name__ == '__main__':
    if sys.argv[1] == '-json':
        print json.dumps(Old_Bep(sys.argv[2]))