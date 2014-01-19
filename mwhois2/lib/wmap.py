#!/usr/bin/env python

import sys
from wconn import WhoisServerConnection

class WhoisServerMap:
        
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
            return self.wserverismap[self.tld]
        except Exception, e:
            print "Error finding %s please use a different tld to search for." % (e) 
            sys.exit()
    
    def regex(self):
        try:
            x = self.exmap[self.tld]
            return x
        except Exception, e:
            sys.exit()