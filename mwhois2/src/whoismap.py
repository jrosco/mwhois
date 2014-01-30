#!/usr/bin/env python

import re
import sys


class WhoisServerMap(object):
        
    def __init__(self, domain=None):
        
        self.domain = domain
       
        self.servermap = {   'de' : 'whois.denic.de', \
                        'de' : 'whois.nic.de', \
                        'uk' : 'whois.nic.uk', \
                        'com' : 'whois.markmonitor.com', \
                        'net': 'whois.internic.net', \
                        'biz' : 'whois.biz', \
                        'biz' : 'whois.nic.biz', \
                        'info' : 'whois.afilias.net', \
                        'org' : 'whois.publicinterestregistry.net', \
                        'org' : 'whois.pir.org', \
                        'at' : 'whois.nic.at', \
                        'tv' : 'whois.www.tv', \
                        'ch' : 'whois.nic.ch', \
                        'nl' : 'whois.domain-registry.nl', \
                        'us' : 'whois.nic.us', \
                        'ws' : 'whois.nic.ws', \
                        'it' : 'whois.nic.it', \
                        'ru' : 'whois.ripn.net', \
                        'be' : 'whois.dns.be', \
                        'pl' : 'whois.dns.pl', \
                        'br' : 'whois.nic.br', \
                        'name' : 'whois.nic.name', \
                        'cc' : 'whois.nic.cc', \
                        'to' : 'monarch.tonic.to', \
                        'tk' : 'whois.dot.tk', \
                        'ag' : 'whois.nic.ag', \
                        'se' : 'whois.nic-se.se', \
                        'se' : 'whois.nic.se', \
                        'se' : 'whois.iis.se', \
                        'fr' : 'whois.nic.fr', \
                        'dk' : 'whois.dk-hostmaster.dk', \
                        'ro' : 'whois.rotld.ro', \
                        'cz' : 'whois.nic.cz', \
                        'ac' : 'whois.nic.ac', \
                        'ms' : 'whois.adamsnames.tc', \
                        'li' : 'whois.nic.li', \
                        'am' : 'whois.amnic.net', \
                        'am' : 'whois.nic.am', \
                        'gr' : 'whois.ripe.net', \
                        'ca' : 'whois.cira.ca', \
                        'mx' : 'whois.nic.mx', \
                        'cn' : 'whois.cnnic.net.cn', \
                        'edu' : 'whois.educause.edu', \
                        'edu' : 'whois.internic.net', \
                        'lu' : 'whois.dns.lu', \
                        'tf' : 'whois.nic.tf', \
                        'cx' : 'whois.nic.cx', \
                        'jp' : 'whois.nic.ad.jp', \
                        'jp' : 'whois.jprs.jp', \
                        'nu' : 'whois.nic.nu', \
                        'pro' : 'whois.registrypro.pro', \
                        'si' : 'whois.arnes.si', \
                        'br' : 'whois.registro.br', \
                        'lv' : 'whois.nic.lv', \
                        'au' : 'whois.aunic.net', \
                        'lt' : 'whois.domreg.lt', \
                        'st' : 'whois.nic.st', \
                        'ua' : 'whois.net.ua', \
                        'gov' : 'whois.nic.gov', \
                        'gov' : 'whois.dotgov.gov', \
                        'ie' : 'whois.domainregistry.ie', \
                        'no' : 'whois.norid.no', \
                        'as' : 'whois.nic.as', \
                        'il' : 'whois.isoc.org.il', \
                        'mil' : 'whois.nic.mil', \
                        'bz' : 'mhpwhois1.verisign-grs.net', \
                        'cl' : 'whois.nic.cl', \
                        'kr' : 'whois.nic.or.kr', \
                        'is' : 'whois.isnic.is', \
                        'af' : 'whois.netnames.net', \
                        'aero' : 'whois.aero', \
                        'aero' : 'whois.information.aero', \
                        'sh' : 'whois.nic.sh', \
                        'sg' : 'whois.nic.net.sg', \
                        'tm' : 'whois.nic.tm', \
                        'bj' : 'whois.nic.bj', \
                        'cat' : 'whois.cat', \
                        'cd' : 'whois.cd', \
                        'ci' : 'whois.nic.ci', \
                        'coop' : 'whois.nic.coop', \
                        'ee' : 'whois.eenet.ee', \
                        'eu' : 'whois.eu', \
                        'fi' : 'whois.ficora.fi', \
                        'gf' : 'whois.nplus.gf', \
                        'gg' : 'whois.channelisles.net', \
                        'hk' : 'whois.hkirc.net', \
                        'hk' : 'whois.hkirc.net.hk', \
                        'hk' : 'whois.hkirc.hk', \
                        'hn' : 'whois2.afilias-grs.net', \
                        'hu' : 'whois.nic.hu', \
                        'in' : 'whois.inregistry.net', \
                        'int' : 'whois.iana.org', \
                        'io' : 'whois.nic.io', \
                        'ke' : 'whois.kenic.or.ke', \
                        'kz' : 'whois.domain.kz', \
                        'kz' : 'whois.nic.kz', \
                        'mg' : 'whois.nic.mg', \
                        'mn' : 'whois.nic.mn', \
                        'museum' : 'whois.museum', \
                        'my' : 'whois.mynic.net.my', \
                        'na' : 'whois.na-nic.com.na', \
                        'nz' : 'whois.srs.net.nz', \
                        'pm' : 'whois.nic.pm', \
                        'pr' : 'whois.uprr.pr', \
                        're' : 'whois.nic.re', \
                        'tj' : 'whois.nic.tj', \
                        'tl' : 'whois.nic.tl', \
                        'tr' : 'whois.nic.tr', \
                        'tw' : 'whois.twnic.net.tw', \
                        'ug' : 'whois.co.ug', \
                        'uz' : 'whois.cctld.uz', \
                        've' : 'whois.nic.ve', \
                        'wf' : 'whois.nic.wf', \
                        'yt' : 'whois.nic.yt' }
    
    
        self.exmap = {   'de' : 'Status: free', \
                        'uk' : 'no match', \
                        'com' : 'No match for', \
                        'net': 'No match for', \
                        'biz' : 'not found', \
                        'biz' : 'not found', \
                        'info' : 'not found', \
                        'org' : 'not found', \
                        'at' : 'nothing found', \
                        'tv' : '.tv you have used', \
                        'ch' : 'not have an entry', \
                        'nl' : 'is free', \
                        'us' : 'not found:', \
                        'ws' : 'no match for', \
                        'it' : 'AVAILABLE', \
                        'ru' : 'no entries found', \
                        'be' : 'no such domain', \
                        'pl' : 'no information about', \
                        'br' : 'no match for', \
                        'name' : 'no match', \
                        'cc' : 'no match', \
                        'to' : 'no match for', \
                        'tk' : 'not known', \
                        'ag' : 'not found', \
                        'se' : 'no data found', \
                        'fr' : 'no entries found', \
                        'dk' : 'no entries found', \
                        'ro' : 'no entries found', \
                        'cz' : 'no data found', \
                        'ac' : 'no match for', \
                        'ms' : 'is not registered', \
                        'li' : 'not have an entry', \
                        'am' : 'no match', \
                        'gr' : 'no entries found', \
                        'ca' : 'avail', \
                        'mx' : 'referencias de organization no encontradas', \
                        'cn' : 'no matching record', \
                        'edu' : 'no match for', \
                        'lu' : '% no such domain', \
                        'cx' : 'no match for', \
                        'jp' : 'No match!!', \
                        'nu' : 'no match for', \
                        'si' : 'no entries found', \
                        'au' : 'No Data Found', \
                        'st' : 'no entries found', \
                        'ua' : '% no entries found', \
                        'gov' : 'ready please', \
                        'ie' : '% there was no match in the ie domain', \
                        'no' : 'no matches', \
                        'as' : 'domain not found', \
                        'il' : 'no data was found', \
                        'bz' : 'no match', \
                        'cl' : 'no existe', \
                        'kr' : 'is not registered', \
                        'is' : 'no entries found', \
                        'af' : 'no match', \
                        'aero' : 'not registered', \
                        'sh' : 'no match', \
                        'sg' : 'nomatch', \
                        'tm' : 'no match', \
                        'cd' : 'no match', \
                        'gf' : 'not found in our database', \
                        'kz' : 'no entries found', \
                        'tj' : 'no match',
                        'hk' : 'The domain has not been registered.'}

    
    def get_whois_server(self):
        
        try:
            if self.domain != None:
                self.get_domain_tld()
            self.whoisserver =  self.servermap[self.tld]
            return self.whoisserver
        except Exception, e:
            print("Error finding %s please use a different tld to search for." % (e)) 
            return False
    
    def tld_not_found_text(self):
        
        try:
            self.not_found_text = self.exmap[self.tld]
            return self.not_found_text
        except Exception, e:
            return "Error not found: %s" % (e)
        
    
    def get_domain_tld(self):
        
        self.tld = re.split('[. :]', self.domain)
        self.tld = self.tld[-1]
        return self.tld
        
        
        
