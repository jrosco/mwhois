#!/usr/bin/env python
from numpy.oldnumeric.ma import domain_check_interval

import wx 
from threading import *
import logging

from mwhois.whosearch import WhoisSearch
from util import WhoisClientUtil


class SingleSearchThread(Thread):
    
    def __init__(self, window_obj):
       
        Thread.__init__(self)
        self._window_obj = window_obj
        self.setDaemon(True)
        self.history_list_counter = 0
        self.history = {}

        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)
        self.logger.debug('SingleSearchThread constructor: __init__()')
        
    def run(self):
       
        self.logger.debug('called SingleSearchThread().run')

        search = WhoisSearch()

        try:
            
            self.logger.debug('trying search thread')
            
            if self._window_obj.history_select is True:

                self.logger.debug('history select enabled.')
                history_items = self._window_obj.m_listbox_history.GetItems()
                search.dname = history_items[self._window_obj.m_listbox_history.GetSelection()]

                #TODO Have history search use stored results. Need to have history data stored in a list type
                # domain_history_list_no = self._window_obj.m_listbox_history.GetSelection()
                # self.logger.debug('history select enabled. using %s' % domain_history_list_no)
                # self._window_obj.history_select = False
                #
                # try:
                #     domain_history = str(self.get_history(domain_history_list_no))
                #     wx.PostEvent(self._window_obj, ResultEvent(self._window_obj.SINGLE_SEARCH_EVT_RESULT_ID,
                #                                                domain_history, 2))
                # except Exception, e:
                #     wx.PostEvent(self._window_obj, ResultEvent(self._window_obj.SINGLE_SEARCH_EVT_ERROR_ID, str(e)))
                
            else:
                search.dname = self._window_obj.m_textctrl_domain.GetValue()
                search.whois_server = self._window_obj.m_combobox_whoisserver.GetValue()

            self.logger.debug('doing a whois search via whois servers')
            search.whois_search()

            #self.set_history(self.history_list_counter, search.response())
            #self.history_list_counter += 1

            wx.PostEvent(self._window_obj, ResultEvent(self._window_obj.HISTORY_DISPLAY_EVT_ID,
                                                       search.dname))
            wx.PostEvent(self._window_obj, ResultEvent(self._window_obj.SINGLE_SEARCH_EVT_RESULT_ID,
                                                       search.response(), search.whois_info.is_domain_alive()))
                
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
        self.logger.debug('set %s' % self.history)
        return


class MultiSearchThread(Thread):
    
    def __init__(self, window_obj):
       
        Thread.__init__(self)
        self._window_obj = window_obj
        self.setDaemon(True)
        self._want_abort = 0
        
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)
        self.logger.debug('MultiSearchThread constructor: __init__()')
        
    def run(self):
        
        self.logger.debug('called MultiSearchThread().run')
        
        search = WhoisSearch()
        search.wordlist = self._window_obj.m_textctrl_file.GetValue()
        
        tld = self._window_obj.m_combo_tld.GetValue()
        cctld = self._window_obj.m_combo_cctld.GetValue()
        gtld = self._window_obj.m_combo_gtld.GetValue()
        
        if tld != '' and cctld != '':search.tld = tld + "." + cctld
        elif tld != '':search.tld = tld
        elif cctld != '':search.tld = cctld
        elif gtld != '':search.tld = gtld
        #else:search.tld = 'com'
            
        if self._window_obj.m_checkbox_dead.GetValue() is True: search.deadonly = True
        
        if self._window_obj.m_textctrl_sleep.GetValue() == '':
            self._window_obj.m_textctrl_sleep.SetValue('0')

        search.sleep = float(self._window_obj.m_textctrl_sleep.GetValue())
        
        multi = search.whois_multi_search()

        try:

            for multi_list in multi:

                status = multi_list[0]
                domain = multi_list[1]
                whois_server = search.whois_server

                try: cdate = search.creation_date()
                except: cdate = 'N/A'

                try: edate = search.expiry_date()
                except: edate = 'N/A'

                try: udate = search.update_date()
                except: udate = 'N/A'

                if self._want_abort is 0:
                    wx.PostEvent(self._window_obj, ResultEvent(self._window_obj.MULTI_SEARCH_EVT_RESULT_ID, status,
                                                               domain, cdate, edate, udate, whois_server))
                else:
                    self.logger.debug('aborted MultiSearchThread()')
                    break

        except Exception, error:

            self.logger.debug('error in MultiSearchThread()')
            wx.PostEvent(self._window_obj, ResultEvent(self._window_obj.MULTI_SEARCH_EVT_ERROR_ID, error))

        self.logger.debug('cleanup MultiSearchThread()')
        wx.PostEvent(self._window_obj, ResultEvent(self._window_obj.CLEANUP_EVT_ID, self))

    def abort(self):

        self.logger.debug('abort MultiSearchThread()')
        self._want_abort = 1


class ResultEvent(wx.PyEvent):
    
    def __init__(self, event_id, *args):

        self.event_id = event_id
        wx.PyEvent.__init__(self)
        self.SetEventType(self.event_id)
        self.data = args
        

class GUIEvent():
     
    def __init__(self, win_obj):
         
        self.history = { }
        self._win_obj = win_obj
        
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
    
    def set_tld_list(self):
        
        self.logger.debug('called set_tld_list()')
        client_util = WhoisClientUtil()
        tld_list = client_util.get_tld()
        cctld = client_util.get_cctld()
        gtld = client_util.get_gtld()
        
        self._win_obj.m_combo_tld.SetItems(tld_list)
        self._win_obj.m_combo_cctld.SetItems(cctld)
        self._win_obj.m_combo_gtld.SetItems(gtld)
        return
