import sys, os, StringIO
from time import sleep


class progress:
    
    def __init__(self):
       self.already = 0
       
    def progressbar(self, number, total,  char):

       percentage = int(100 - round(number*100.0/total))
       if percentage > 0:
           xchar = char * (percentage-self.already)
           self.already = percentage 
           sys.stdout.write(xchar)
           sys.stdout.flush()               
           sleep(0.1)                        
                
                
    def countlines(self, file):
        
        linecount = 0
        f = open(file)
        it = iter(f)
        try: 
            while it.next():
                linecount += 1
        except StopIteration:
                    pass
        return linecount

    
def main():
    
    p = progress()
    lines = p.countlines("/tmp/junk")  
    count = lines        
    for i in xrange(lines):
        p.progressbar(count, lines, "*")
        count -=1
    print "Finished"      
     
if __name__ == "__main__":
        main()