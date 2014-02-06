#!/usr/bin/env python 

import re
import sys
import logging

from whomap import WhoisServerMap
import const as CONST
from exception import WhoException

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
        
        self.logger.debug('clearing previous server used')
        
        if self.second_server == False:
            
            self.logger.debug('no second server needed')
            list_number = 0
            #server_map = self.server_map
        
        else:
            
            self.logger.debug('second server needed, must have exceeded limit!!')
            list_number = 1
            #server_map = self.backup_server_map
        
        try:
           if self.domain != None:
               self.logger.debug('%s domain is set', self.domain)
               self.get_domain_tld()
           
           self.whoisserver =  self.all_server_map[self.tld][list_number]
           #self.whoisserver =  server_map[self.tld]
           self.logger.debug('return %s', self.whoisserver)
           
           #self.logger.info('Querying %s' % self.whoisserver)
           
           return self.whoisserver
        
        except:
            
            if self.second_server == True:
                self.logger.info("problem mapping second whois server")
            else:
                self.logger.info("problem mapping whois server with %s please use a different tld to search for.", self.tld)
   
    
    def tld_not_found_text(self):
        
        self.logger.debug('called tld_not_found_text()')
        
        try:
            self.not_found = self.all_server_map[self.tld][2]
            self.logger.debug('return not found text = %s', self.not_found)
            
            return self.not_found
        
        except:
            self.logger.error("dead domain text not found")
        
    
    def exceeded_limit(self):
        
        self.logger.debug('called exceeded_limit()')
        
        try:
            self.exceeded = self.all_server_map[self.tld][3]
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
        
    
    def get_list_supported_tlds(self):
    
        return self.all_server_map
    
    def get_repsonse(self):
        
        self.logger.debug('called get_repsonse()')
        
        return self.response
    
    
    def get_whois_attr(self, whois_attr):
        
        self.logger.debug('called get_whois_attr()')
        
        self.whois_attr = whois_attr
        
        try:
            
            if whois_attr == CONST.CDATE: 
                self.whois_attr =  self.all_info_map[self.tld][0]
            
            elif whois_attr == CONST.EDATE:
                self.whois_attr =  self.all_info_map[self.tld][1]
                
            elif whois_attr == CONST.UPDATE:
                self.whois_attr =  self.all_info_map[self.tld][2]
            
            elif whois_attr == CONST.REGISTRANT:
                self.whois_attr =  self.all_info_map[self.tld][3]
            
            elif whois_attr == CONST.NAMESERVER:
                self.whois_attr =  self.all_info_map[self.tld][4]
                    
            elif whois_attr == CONST.WHOIS_STATUS:
                self.whois_attr = self.all_info_map[self.tld][5]
            
            self.logger.debug('return %s', self.whois_attr)
            
            self.whois_attr_list = []
            
            for item in re.findall(self.whois_attr, self.response):
                
                self.whois_attr_list.append(item)
        
        except WhoException, e:
            
            self.logger.info('No attr %s', self.whois_attr)
        
        return self.whois_attr_list
        
    
    def is_domain_alive(self):
        
        self.logger.debug('called is_domain_alive()')
        
        self.tld_not_found_text()
        self.exceeded_limit()
        
        if re.search(self.exceeded, self.response) and self.exceeded != '':
            self.second_server = True
            self.logger.info('%s you have exceeded your quota of queries (oops)', self.domain)
            self.logger.info('Lets try a different server...')
            return CONST.DOMAIN_SEARCH_EXCEEDED
        
        if re.search(self.not_found, self.response):
            #self.second_server = True
            self.logger.debug('%s domain is dead', self.domain)
            return CONST.DOMAIN_DEAD
        
        else:
            self.logger.debug('%s domain is alive', self.domain)
            return CONST.DOMAIN_ALIVE
