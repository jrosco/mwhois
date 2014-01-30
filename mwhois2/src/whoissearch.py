#!/usr/bin/env python 

import os
import sys
from types import ListType

from whoisconn import WhoisServerConnection
from whoismap import WhoisServerMap
import const as CONST

class WhoisSearch(WhoisServerMap):
    
    def __init__(self, wordlist=None, dname=None, tld=CONST.DEFAULT_TLD, deadonly=False):
        
        WhoisServerMap.__init__(self)
        
        self.wordlist = wordlist
        self.dname = dname
        self.tld = tld
        self.deadonly = deadonly
        
      
    def single_search(self):
        
        w = WhoisServerConnection()
        w.domain = self.dname
        w.get_whois_server()
        w.connection()
        
        self.response = w.whois_search()
        return self.response

    
    def basic_search(self):
    
        w = WhoisServerConnection()
        w.tld = self.tld
        
        try:
            search_list = open(self.wordlist, 'r')
        except:
            search_list = self.wordlist
            
        for line in search_list:
            if ('.' in line):
                w.domain = line
                #self.tld = w.get_domain_tld()
            else:
                w.domain = line.rstrip() + "." + self.tld
            w.get_whois_server()
            w.connection()
            alive = w.is_domain_alive()
            if alive == CONST.DOMAIN_DEAD:
                d_list = [CONST.DOMAIN_DEAD, w.domain]
                yield d_list
            elif alive == CONST.DOMAIN_ALIVE and self.deadonly == False or self.deadonly == None:
                d_list = [CONST.DOMAIN_ALIVE, w.domain]
                yield d_list

        if type(search_list) is ListType:
            return
        else:
            search_list.close()
        
        return 
    
 
    def deeper_search(self):
        
        import socket
        d_list = []
        
        try:
            search_list = open(self.wordlist, 'r')
        except:
            search_list = self.wordlist
        
        for line in search_list:
            d_line = line.rstrip() + "." + self.tld
            try: socket.getaddrinfo(d_line, socket.AF_INET, 0, socket.SOCK_STREAM)
            except Exception, e:
                d_list.append(line)
        
        if type(search_list) is ListType:
            pass
        else:
            search_list.close()
        
        self.wordlist = d_list
        x = self.basic_search()
        return x     
    
    