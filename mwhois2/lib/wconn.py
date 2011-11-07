#!/usr/bin/env python 

import socket

class whoisConn():
    
    def __init__(self, domain, who, tld):
        
        self.domain = domain
        self.tld = tld
        self.response = ''
        self.who = who
        
    def connection(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)        
        s.connect((self.who, 43))
        if tld == "com":
            domain = "="+domain
        s.send(domain + "\r\n")
        while True:
            d = s.recv(4096)
            self.response += d
            if d == '': break     
        s.close()
        
    def single(self):
        return self.response
    
    def basic(self):
        if re.search(self.ex(self.tld), self.response):
            return self.domain
    
    def advance(self):
        if re.search(self.ex(self.tld), self.response):return self.domain, DOMAIN_DEAD
        else:return self.domain, DOMAIN_ALIVE

    