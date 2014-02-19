#!/usr/bin/env python

from mwhois.whomap import WhoisServerMap

class WhoisClientUtil():
  
    def map_whois_server(self, domain):
        
        tld = domain.split('.')
        server = WhoisServerMap().all_server_map
    
        for keys,values in server.items():
            if keys == tld[-1]:return values[0], values[1]
            else:continue
        
        