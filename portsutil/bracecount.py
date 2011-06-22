import StringIO
def match_braces(braceset, startline=0):
     openBr = "magic"
     location = {'line': 0, 'char': 0}
     f = StringIO.StringIO(braceset)
     while openBr is not 0:
         if openBr == "magic":
             openBr = 0
         for line in f:
             location['line']+=1
             location['char']=0
             for char in line:
                 location['char']+=1
                 if char is "{":
                     openBr +=1
                 elif char is "}":
                     openBr -=1
     print location