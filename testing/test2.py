#file2.py
import test1

class foo2():
    
    def __init__(self):
        
        global test1
        print test1.DL
        print test1.DW
        
test1.foo1("value12", "value2")
foo2()