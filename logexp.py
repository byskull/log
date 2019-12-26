class Exp :
    a = 1
    b = True
    c = "1231"
    d = [ 12, 3, 4 ]
    e = [ ["a","b", "c" ], 12, 345 ]

    def __init__(self) :
        a = 2

    def prin(self) :
        print self.a

def log(s):
    #print dir(s)
    print "Class Name : " + s.__class__.__name__
    for i in dir(s) :
        tmp = getattr( s, i )
        if tmp != None and not callable(tmp) and  __name__ != tmp :
            print i, tmp
        #print type(tmp)
        #print callable(tmp)
        #print isinstance( tmp, FunctionType )
    
    
a = Exp()

log(a)