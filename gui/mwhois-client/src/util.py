#!/usr/bin/env python

from mwhois.whomap import WhoisServerMap
import mwhois.const as CONST


class WhoisClientUtil():

    def __init__(self):
        pass
  
    def map_whois_server(self, domain):
        
        tld = domain.split('.')
        server = WhoisServerMap().all_server_map
    
        for keys, values in server.items():
            if keys == tld[-1]:
                return values[0], values[1]
            else:
                continue
            
    def get_tld(self):
        
        get_tld = WhoisServerMap().all_server_map
        tld = ['', 'co']
        
        for keys, values in get_tld.items():
            if values[4] is CONST.TLD_STANDARD:
                tld.append(keys)
        tld.sort()
        return tld
    
    def get_cctld(self):
        
        get_cctld = WhoisServerMap().all_server_map
        cctld = ['']
        
        for keys, values in get_cctld.items():
            if values[4] is CONST.CCTLD_STANDARD:
                cctld.append(keys)
        
        cctld.sort()
        return cctld
    
    def get_gtld(self):
        
        get_gtld = WhoisServerMap().all_server_map
        gtld = ['']
        
        for keys, values in get_gtld.items():
            if values[4] is CONST.GTLD_STANDARD:
                gtld.append(keys)
            elif values[4] is CONST.GTLD_DONUTS:
                gtld.append(keys)
            elif values[4] is CONST.GTLD_UNITED:
                gtld.append(keys)
            elif values[4] is CONST.GTLD_UNIREG:
                gtld.append(keys)
        
        gtld.sort()
        return gtld
