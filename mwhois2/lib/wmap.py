#!/usr/bin/env python

import sys
from wconn import whoisConn

class wserverMap:
        
    def __init__(self, tld):
        
        self.tld = tld
        
        self.wserverismap = { 'com': 'wserveris.verisign-grs.com', \
                    'com.au': 'wserveris.verisign-grs.com', \
                    'org': 'wserveris.pir.org', \
                    'net': 'wserveris.internic.net', \
                    'biz': 'wserveris.neulevel.biz', \
                    'edu': 'wserveris.educause.net', \
                    'info': 'wserveris.afilias.info' } 
    
        self.exmap = { 'com': 'No match for', \
                    'com.au': 'No match for', \
                    'org': 'NOT FOUND', \
                    'net': 'No match for', \
                    'biz': 'Not found:', \
                    'edu': 'No Match', \
                    'info': 'NOT FOUND' }
    
    
    def wserver(self):
        try:
            w = self.wserverismap[self.tld]
            return w
        except Exception, e:
            print "Error finding %s please use a different tld to search for." % (e) 
            sys.exit()
    
    def regex(self):
        try:
            x = self.exmap[self.tld]
            return x
        except Exception, e:
            sys.exit()
    
if __name__ == "__main__":
        x = wserverMap('net')
        w = x.wserver()
        print 'Using server', w
        who = whoisConn('google.net', w, 'net')
        who.connection()
        print who.single()