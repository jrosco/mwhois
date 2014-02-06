#!/usr/bin/env python

from threading import *
from mwhois.whosearch import WhoisSearch
import mwhois.const as CONST

class WorkerThread(Thread):
    
    def __init__(self, type, data, obj):
        Thread.__init__(self)
        self._want_abort = 0
        self.type = type
        self.data = data
        self.obj = obj
        
        self.start()

    def run(self):
        
        if self.type == CONST.SINGLE_TYPE:
            search = WhoisSearch()
            search.dname = self.data
            search.whois_search()
            self.obj.SetValue(search.response())
            
        else:
            self.tld = self.data[0]
            self.wordlist = self.data[1]
            self.domainlist = self.data[2]
            
            mwhois = WhoisSearch(None, self.tld, self.wordlist, self.domainlist,self.obj)
            if self.type == CONST.BASIC_TYPE:
                mwhois.whois_multi_search()
            else:
                mwhois.advance_search()
                
    def abort(self):
        print "Stopping Thread"
        self.daemon = True


class Controller():
    
    def __init__(self):
        
        return