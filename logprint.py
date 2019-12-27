import time

class logprint :

    name = ""

    def __init__(self, name_ ) :
        self.name = name_ 
    
    def prin( self,  s ) :
        f1 = open( "D:\Data\log\log_" + self.name + "." + time.strftime('%Y%m%d'), "at" )        
        f1.write( time.strftime("%H:%M:%S" ) + " " + s )
        
        

a = logprint("aa")

a.prin("anafd")
