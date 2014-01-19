#!/usr/bin/env python 

import socket, sys

class WhoisServerConnection():
    
    def __init__(self, domain, who, tld):
        
        self.domain = domain
        self.tld = tld
        self.response = ''
        self.who = who
        
    def connection(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)        
        
        print "Using Domain:", self.domain
        print "Using Server:", self.who
        print "Using TLDs:", self.tld
        
        try:
            s.connect((self.who, 43))
            if self.tld == "com":
                self.domain = "="+self.domain
            s.send(self.domain + "\r\n")
            while True:
                d = s.recv(4096)
                self.response += d
                if d == '': break     
            s.close()
        except Exception, e:
            print "Error: %s" % (e) 
            sys.exit()
        
    def single(self):
        return self.response
    
    def basic(self):
        if re.search(self.ex(self.tld), self.response):
            return self.domain
    
    def advance(self):
        if re.search(self.ex(self.tld), self.response):return self.domain, DOMAIN_DEAD
        else:return self.domain, DOMAIN_ALIVE

    