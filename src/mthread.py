#!/usr/bin/env python -W

from threading import *
from mwhois import *

class WorkerThread(Thread):
    
    def __init__(self, type, data, obj):
        Thread.__init__(self)
        self._want_abort = 0
        self.type = type
        self.data = data
        self.obj = obj
        
        self.start()

    def run(self):
        
        if self.type == SINGLE_TYPE:
            WhoisSearch(self.data, None, None, None, self.obj).single_search()
        else:
            self.tld = self.data[0]
            self.wordlist = self.data[1]
            self.domainlist = self.data[2]
            
            mwhois = WhoisSearch(None, self.tld, self.wordlist, self.domainlist,self.obj)
            if self.type == BASIC_TYPE:
                mwhois.basic_search()
            else:
                mwhois.advance_search()
                
    def abort(self):
        print "Stopping Thread"
        self.daemon = True
