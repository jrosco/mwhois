#!/usr/bin/env python

import wx 
from threading import *
import logging

from mwhois.whosearch import WhoisSearch

class SingleSearchThread(Thread):
    
    def __init__(self, window_obj):
       
        Thread.__init__(self)
        self._window_obj = window_obj
        self.setDaemon(True)
        
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.debug('SingleSearchThread constructor: __init__()')
        #self.gui_event = GUIEvent()
        self.history_list_counter = 0
        self.history = { }
        
    def run(self):
       
        self.logger.debug('called SingleSearchThread().run')
        
        try:
            self.logger.debug('trying search thread')
            
            if self._window_obj.history_select == True:
                domain_history_list_no = self._window_obj.m_listbox_history.GetSelection()
                self.logger.debug('history select enabled. using %s' % (domain_history_list_no))
                self._window_obj.history_select = False
                
                try:
                    domain_history =  str(self.get_history(domain_history_list_no))
                    wx.PostEvent(self._window_obj, ResultEvent(self._window_obj.SINGLE_SEARCH_EVT_RESULT_ID, domain_history))
                except Exception, e: 
                    wx.PostEvent(self._window_obj, ResultEvent(self._window_obj.SINGLE_SEARCH_EVT_ERROR_ID, str(e)))
                
            else:
                
                search = WhoisSearch()
                search.dname = self._window_obj.m_textctrl_domain.GetValue()
                self.logger.debug('doing a whois search via whois servers')
                search.whois_search()
                self.set_history(self.history_list_counter, search.response())
                self.history_list_counter += 1
                print('history counter=%s' % self.history_list_counter)
                wx.PostEvent(self._window_obj, ResultEvent(self._window_obj.HISTORY_DISPLAY_EVT_ID, search.dname))
                wx.PostEvent(self._window_obj, ResultEvent(self._window_obj.SINGLE_SEARCH_EVT_RESULT_ID, search.response(), search.whois_info.is_domain_alive()))
                
        except Exception, e:
            
            print('error %s' % str(e))
            wx.PostEvent(self._window_obj, ResultEvent(self._window_obj.SINGLE_SEARCH_EVT_ERROR_ID, str(e)))
            
    
    def get_history(self, position):
        
        self.logger.debug('called get_history()')
        self.logger.debug('get %s' % self.history)
        return self.history.get(position)
        
    
    def set_history(self, domain_history, response):
        
        self.logger.debug('called set_history()')
        self.history.update({domain_history:response})
        self.logger.debug('set %s' % (self.history))
        return

            

class ResultEvent(wx.PyEvent):
    
    def __init__(self, event_id, *args):
        
        print(args)
        self.event_id = event_id
        wx.PyEvent.__init__(self)
        self.SetEventType(self.event_id)
        self.data = args
        


class GUIEvent():
     
    def __init__(self):
         
        self.history = { }
        
        self.logger = logging.getLogger(__name__)
        self.logger.debug('GUIEvent constructor: __init__()')
         
    def get_history(self, position):
        
        self.logger.debug('called get_history()')
        self.logger.debug('return %s' % self.history)
        return self.history[position]
        
    def set_history(self, domain_history, response):
        
        self.logger.debug('called set_history()')
        self.history.update({domain_history:response})
        self.logger.debug('return %s' % (self.history))
        return
