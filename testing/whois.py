#!/usr/bin/env python
"""
@author Joel Cumberland

@contact jr_cumbo@hotmail.com

@version 1.3 

@status: Development and Testing

@copyright 2009

@license: GPL

"""

import sys
import socket
import re
import domainsearch


class whoisserver:
    #TODO // Have a way to produce a fall-back/Redundant server if the default one FAILS!!!
    whoismap = {'com': 'whois.verisign-grs.com', \
                'org': 'whois.pir.org', \
                'net': 'whois.internic.net', \
                'biz': 'whois.neulevel.biz', \
                'edu': 'whois.educause.net', \
                'info': 'whois.afilias.info' } # Will add more Whois Servers later.
    
    exmap =     {'com': 'No match for', \
                 'org': 'NOT FOUND', \
                 'net': 'No match for', \
                 'biz': 'Not found:', \
                 'edu': 'No Match', \
                 'info': 'NOT FOUND' }
    
    
    def who(self, tld):
        
        try:
            w = self.whoismap[tld]
            return w
        except Exception, e:
            print "Error finding", e, "please use a different tld to search for." # Mite remove this Exception..Maybe
            sys.exit()
    
    
    def ex(self, regex):
        
        x = self.exmap[regex]
        return x
    
    
    def conn(self, domain, who, tld, type):
        
        response = ''
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)        
        s.connect((who, 43))
        s.send(domain + "\r\n")
        while True:
            d = s.recv(4096)
            response += d
            if d == '': break     
        
        if type == "single":
            print response
       	    s.close()     
        
        global domainsearch
        fw = domainsearch.dList
        
        if type == "basic":
            if re.search(whoisServer().ex(tld), response):
                    print >>fw, domain + " Domain Not Found"
                    print domain + " Domain Not Found" 
                    s.close()             
            else:
                    s.close()
                              
        if type == "advance":
            if re.search(whoisServer().ex(tld), response):
                    print >>fw, domain + " Domain Not Found" 
                    print domain + " Domain Not Found" 
                    s.close()   
            else:
                    print >>fw, domain + " Domain Found but could be Parked, a Dead Site or an Un-Popular Domain that is not in your DNS Server Cache" 
                    print domain + " Domain Found but could be Parked, a Dead Site or an Un-Popular Domain that is not in your DNS Server Cache" 
                    s.close()
        return
    
