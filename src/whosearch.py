#!/usr/bin/env python 

import logging
from types import ListType

from whoconnect import WhoisServerConnection
from whois import WhoisInfo
import const as CONST


class WhoisSearch():
    
    def __init__(self, wordlist=None, dname=None, tld=CONST.DEFAULT_TLD, deadonly=False, debug=False, time_to_sleep=0):
        
        self.wordlist = wordlist
        self.dname = dname
        self.tld = tld
        self.deadonly = deadonly
        self.debug = debug
        self.sleep = time_to_sleep
        self.whois_server = None
        
        if self.debug is True:
            logging.basicConfig(level=logging.DEBUG)
        else: 
            logging.basicConfig(level=logging.INFO)
            
        self.logger = logging.getLogger(__name__)
        self.logger.debug('constructor: __init__()')

    def whois_search(self):
        
        self.logger.debug('called whois_search()')
        
        self.whois_info = WhoisInfo()
        self.whois_info.domain = self.dname
        
        if self.whois_server is None:
            self.whois_server = self.whois_info.get_whois_server()
        else:
            self.whois_info.get_domain_tld()
            self.whois_info.whoisserver = self.whois_server
            
        self.connection = WhoisServerConnection(self.whois_info)
        self.connection.sleep = self.sleep
        self.connection.connection()
        
        status = self.whois_info.is_domain_alive()
        
        if status == CONST.DOMAIN_SEARCH_EXCEEDED and self.connection.no_of_attempts != 1:
            
            self.logger.debug('lets try a another server shall we. Attempts = %s', self.connection.no_of_attempts)
            self.whois_info.second_server = True
            self.connection.no_of_attempts = 1
            self.connection.connection()
        
        if status == CONST.DOMAIN_DEAD:
            
            return "No information about domain %s" % self.dname
        
        else:
            
            return self.whois_info.response

    
    def whois_multi_search(self):
        
        self.logger.debug('called whois_multi_search()')
        
        self.whois_info = WhoisInfo()
        self.whois_info.tld = self.tld
        
        self.connection = WhoisServerConnection(self.whois_info)
        self.connection.sleep = self.sleep
        
        try:
            
            self.logger.debug('trying opening wordlist as a file')
            search_list = open(self.wordlist, 'r')
            
        except:
            self.logger.debug('ok it\'s not a file object must be a list type. ')
            search_list = self.wordlist
            
        for line in search_list:

            if '.' in line:
                self.whois_info.domain = line
                #self.tld = w.get_domain_tld()
            else:
                self.whois_info.domain = line.rstrip() + "." + self.tld
            
            self.whois_server = self.whois_info.get_whois_server()
            self.connection.connection()
            
            alive = self.whois_info.is_domain_alive()
            
            if alive == CONST.DOMAIN_SEARCH_EXCEEDED and self.connection.no_of_attempts != 1:
                self.whois_info.second_server = True
                self.connection.no_of_attempts = 1
                self.connection.connection()
                alive = self.whois_info.is_domain_alive()
#             else:
#                 self.logger.info("sorry your out of luck, you have been denied by both whois servers, \
#                   please try again later....better luck next time")
#                 sys.exit()
              
            if alive == CONST.DOMAIN_DEAD:
                d_list = [CONST.DOMAIN_DEAD, self.whois_info.domain]
                yield d_list
            elif alive == CONST.DOMAIN_ALIVE and self.deadonly == False or self.deadonly == None:
                d_list = [CONST.DOMAIN_ALIVE, self.whois_info.domain]
                yield d_list

        if type(search_list) is ListType:
            return
        else:
            self.logger.debug('closing file object')
            search_list.close()    
        
        return 

    def deeper_search(self):
        
        self.logger.debug('called deeper_search()')
        
        import socket
        d_list = []
        
        try:
            search_list = open(self.wordlist, 'r')
        except:
            search_list = self.wordlist
        
        for line in search_list:
            d_line = line.rstrip() + "." + self.tld
            try: socket.getaddrinfo(d_line, socket.AF_INET, 0, socket.SOCK_STREAM)
            except Exception:
                d_list.append(line)
        
        if type(search_list) is ListType:
            pass
        else:
            search_list.close()
        
        self.wordlist = d_list
        x = self.whois_multi_search()
        return x     

    def get_tld_type(self):
        
        self.logger.debug('called get_tld_type()')
        
        return self.whois_info.get_tld_type()
    
    def creation_date(self):
        
        self.logger.debug('called creation_date()')
        
        return self.whois_info.get_whois_attr(CONST.CDATE)

    def expiry_date(self):
        
        self.logger.debug('called expiry_date()')
        
        return self.whois_info.get_whois_attr(CONST.EDATE)
    
    def update_date(self):
        
        self.logger.debug('called update_date()')
        
        return self.whois_info.get_whois_attr(CONST.UPDATE)

    def registrant(self):
        
        self.logger.debug('called registrant()')
        
        return self.whois_info.get_whois_attr(CONST.REGISTRANT)
    
    def nameservers(self):
        
        self.logger.debug('called nameservers()')
        
        return self.whois_info.get_whois_attr(CONST.NAMESERVER)
    
#     def whois_status(self):
#         
#         self.logger.debug('called whois_status()')
#         
#         return self.whois_info.get_whois_attr(CONST.WHOIS_STATUS)
#     
    def response(self):
        
        self.logger.debug('called response()')
        
        return self.whois_info.response
    
    def emails(self):
        
        self.logger.debug('called emails()')
        
        return self.whois_info.get_all_emails()