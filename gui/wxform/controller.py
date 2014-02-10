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
        
        search = WhoisSearch()
        search.dname = self.data
        search.whois_search()
        self.obj.SetValue(search.response())
            
    def abort(self):
        print "Stopping Thread"
        self.daemon = True


class Controller():
    
    def __init__(self):
        
        return
