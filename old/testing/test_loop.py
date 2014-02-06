import time


class foo2014():
    
    def foo(self):

        for x in range(0,10000000):
    
            foo = 1 + x 
            #time.sleep(1)
            yield foo
        

class bar2014():
    
    def bar(self):
        
        goof = foo2014()
        
        self.bugs = goof.foo()     
        
        for i in self.bugs:
            print i
            
            
tas = bar2014()

tas.bar()