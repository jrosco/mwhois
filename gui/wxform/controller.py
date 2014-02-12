#!/usr/bin/env python

from mwhois.whosearch import WhoisSearch
from threading import *


class SingleSearchThread(Thread):
    
    def __init__(self, obj, event):
       
        Thread.__init__(self)
        self._obj = obj
        self._event = event
        self.setDaemon(True)

    def run(self):
        
        search = WhoisSearch()
        search.dname = self._obj.m_textctrl_domain.GetValue()
        search.whois_search()
        self._obj.m_textctrl_results.SetValue(search.response())
        
        self._obj.m_listbox_history.Append(search.dname)
        
        #UIEvents(self, None).set_history(search.dname, search.response())
        
        print(dir(self))


class GUIEvents():
     
    def __init__(self, obj, parent):
         
        self._obj = obj
        self.history = []
         
    def get_history(self, data):
         
        return self.history
        
    def set_history(self, domain, response):
         
        self.history[domain, response]
        