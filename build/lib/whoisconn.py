#!/usr/bin/env python 

import re
import socket
import sys

import const as CONST
from whoismap import WhoisServerMap


class WhoisServerConnection(WhoisServerMap):
    
    def __init__(self):
        
        WhoisServerMap.__init__(self)
        
    def connection(self):
        
        self.response = ''
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)        

        try:
            if self.whoisserver != None:
                s.connect((self.whoisserver, 43))
#                 if self.tld == "com":
#                     self.domain = "="+self.domain
                s.send(self.domain + "\r\n")
                while True:
                    data = s.recv(4096)
                    self.response += data
                    if data == '': break     
                s.close()
        except Exception, e:
            print("Error: %s" % (e)) 
            sys.exit()
        return
        
    def whois_search(self):
        
        return self.response
    
    def is_domain_alive(self):
        
        self.tld_not_found_text()
        
        if re.search(self.not_found_text, self.response):
            return CONST.DOMAIN_DEAD
        else:
            return CONST.DOMAIN_ALIVE
    

