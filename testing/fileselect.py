
#############################################TESTING AREA#############################################

import sys

class list:
    
    def wordlist(self, wordlist):
        
        #self.readlist = readlist
        self.wordist = wordlist
        readlist = open(wordlist, 'r')
        print readlist
       
    def domainlist(self, domainlist, write):
        
        #self.list = domainlist
        wr = open(domainlist, 'w')
        print >>wr, write + "Domain Not Found"
        
    def advlist(self, advlist):
        
        self.advlist = advlist
        open(advlist, 'w')
        #return advlist

#############################################TESTING AREA############################################# 