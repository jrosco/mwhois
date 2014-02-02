#!/usr/bin/env python 

import re
import sys
import logging

from whomap import WhoisServerMap
import const as CONST

class WhoisInfo(WhoisServerMap):
    
    
    def __init__(self):
        
        WhoisServerMap.__init__(self)
        
        self.logger = logging.getLogger(__name__)
        
        self.logger.debug('constructor: __init__()')
        
        self.domain = ''
        self.tld = ''
        self.whoisserver = ''
        self.response = ''
        self.not_found = ''
        self.exceeded = ''
        self.second_server = False
        
    def get_whois_server(self):
        
        self.logger.debug('called get_whois_server() domain = %s', self.domain)
        
        if self.second_server == False:
            
            self.logger.debug('no second server needed')
            server_map = self.server_map
        
        else:
            
            self.logger.debug('second server needed, must have exceeded limit!!')
            server_map = self.backup_server_map
        
        try:
           if self.domain != None:
               self.logger.debug('%s domain is set', self.domain)
               self.get_domain_tld()
           
           self.whoisserver =  server_map[self.tld]
           self.logger.debug('return %s', self.whoisserver)
           
           return self.whoisserver
        
        except:
            
            if self.second_server == True:
                self.logger.info("problem mapping second whois server")
            else:
                self.logger.info("problem mapping whois server with %s please use a different tld to search for.", self.tld)
   
    
    def tld_not_found_text(self):
        
        self.logger.debug('called tld_not_found_text()')
        
        try:
            self.not_found = self.not_found_map[self.tld]
            self.logger.debug('return not found text = %s', self.not_found)
            
            return self.not_found
        
        except:
            self.logger.error("dead domain text not found")
        
    
    def exceeded_limit(self):
        
        self.logger.debug('called exceeded_limit()')
        
        try:
            self.exceeded = self.execeed_map[self.tld]
            self.logger.debug('return exceeded text = %s for tld %s', self.exceeded, self.tld)

        
        except:
            
            self.logger.debug("exceeded text not found")
    
        return self.exceeded
    
    def get_domain_tld(self):
        
        self.logger.debug('called get_domain_tld()')
        
        self.tld = re.split('[. :]', self.domain)
        self.tld = self.tld[-1]
        self.logger.debug('return %s', self.tld)
        
        return self.tld
        
    
    def get_repsonse(self):
        
        self.logger.debug('called get_repsonse()')
        
        return self.response
    
    
    def get_whois_attr(self, whois_attr):
        
        self.logger.debug('called get_whois_attr()')
        
        self.whois_attr = whois_attr
        
        try:
            
            if whois_attr == CONST.CDATE: 
                self.whois_attr =  self.creation_date_map[self.tld]
            
            elif whois_attr == CONST.EDATE:
                self.whois_attr =  self.expiry_date_map[self.tld]
                
            elif whois_attr == CONST.UPDATE:
                self.whois_attr =  self.updated_date_map[self.tld]
            
            elif whois_attr == CONST.REGISTRANT:
                self.whois_attr =  self.registrant_map[self.tld]
            
            elif whois_attr == CONST.NAMESERVER:
                self.whois_attr =  self.nameserver_map[self.tld]
                    
            self.logger.debug('return %s', self.whois_attr)
            for item in re.findall(self.whois_attr, self.response):
                self.whois_attr = item
        
        except:
            
            self.logger.info('No attr %s', self.whois_attr)
        
        return self.whois_attr
        
    
    def is_domain_alive(self):
        
        self.logger.debug('called is_domain_alive()')
        
        self.tld_not_found_text()
        self.exceeded_limit()
        
        if re.search(self.exceeded, self.response) and self.exceeded != '':
            self.second_server = True
            self.logger.info('%s you have exceeded your quota of queries (oops)', self.domain)
            return CONST.DOMAIN_SEARCH_EXCEEDED
        
        if re.search(self.not_found, self.response):
            #self.second_server = True
            self.logger.debug('%s domain is dead', self.domain)
            return CONST.DOMAIN_DEAD
        
        else:
            self.logger.debug('%s domain is alive', self.domain)
            return CONST.DOMAIN_ALIVE
