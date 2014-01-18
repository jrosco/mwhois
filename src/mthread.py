#!/usr/bin/env python

import time
from threading import *
import wx
from mwhois import *

# Thread class that executes processing
class WorkerThread(Thread):
    """Worker Thread Class."""
    def __init__(self, type, data, obj):
        print """Init Worker Thread Class."""
        Thread.__init__(self)
        #self._notify_window = notify_window
        self._want_abort = 0
        self._type = type
        self._data = data
        self._obj = obj
        # This starts the thread running on creation, but you could
        # also make the GUI thread responsible for calling this
        self.start()

    def run(self):
        print """Run Worker Thread."""
        
        if self._type == SINGLE_TYPE:
            self.domain = whois_search(self._data, None, None, None, None).single_search()
            self._obj.SetValue(self.domain)
        else:
            mwhois = whois_search(None, "com", "/home/jrosco/Desktop/sw.txt", "/home/jrosco/Downloads/goo",self._obj)
            #mwhois = whois_search(None, self.tld, self.wordlist, self.domainlist)
            if self._type == BASIC_TYPE:
                mwhois.basic_search()
            else:
                mwhois.advance_search()
                

    def abort(self):
        print """abort worker thread."""
        # Method for use by main thread to signal an abort
        self._want_abort = 1
