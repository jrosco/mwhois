#!/usr/bin/env python

import re

class WhoisServerMap(object):
        
    def __init__(self):
        
        self.server_map =            {'de' : 'whois.denic.de', \
                                        'uk' : 'whois.nic.uk', \
                                        'com' : 'whois.verisign-grs.com', \
                                        'net': 'whois.internic.net', \
                                        'biz' : 'whois.biz', \
                                        #'biz' : 'whois.nic.biz', \
                                        'info' : 'whois.afilias.info', \
                                        'org' : 'whois.publicinterestregistry.net', \
                                        #'org' : 'whois.pir.org', \
                                        'at' : 'whois.nic.at', \
                                        'tv' : 'whois.nic.tv', \
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
                                        #'edu' : 'whois.internic.net', \
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
                                        'bz' : 'whois.belizenic.bz', \
                                        'cl' : 'whois.nic.cl', \
                                        'kr' : 'whois.nic.or.kr', \
                                        'is' : 'whois.isnic.is', \
                                        'af' : 'whois.nic.af', \
                                        'aero' : 'whois.aero', \
                                        #'aero' : 'whois.information.aero', \
                                        'sh' : 'whois.nic.sh', \
                                        'sg' : 'whois.nic.net.sg', \
                                        'tm' : 'whois.nic.tm', \
                                        'bj' : 'whois.nic.bj', \
                                        'cat' : 'whois.cat', \
                                        'cd' : 'whois.nic.cd', \
                                        'ci' : 'whois.nic.ci', \
                                        'coop' : 'whois.nic.coop', \
                                        'ee' : 'whois.eenet.ee', \
                                        'eu' : 'whois.eu', \
                                        'fi' : 'whois.ficora.fi', \
                                        'gf' : 'whois.internic.net', \
                                        'gg' : 'whois.channelisles.net', \
                                        #'hk' : 'whois.hkirc.net', \
                                        'hk' : 'whois.hkirc.net.hk', \
                                        #'hk' : 'whois.hkirc.hk', \
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
    
    
        self.backup_server_map =    {'com' : 'whois.domain.com', \
                                     'org': 'whois.publicinterestregistry.net', \
                                     'au' : 'whois.melbourneit.com.au'}
        
        
        self.not_found_map =        {'de' : 'Status: free', \
                                        'uk' : 'no match', \
                                        'com' : 'No match for', \
                                        'net': 'No match for', \
                                        'biz' : 'Not found', \
                                        'info' : 'NOT FOUND', \
                                        'org' : 'NOT FOUND', \
                                        'at' : 'nothing found', \
                                        'tv' : 'No match for', \
                                        'ch' : 'not have an entry', \
                                        'nl' : 'is free', \
                                        'us' : 'Not found:', \
                                        'ws' : 'No match for', \
                                        'it' : 'AVAILABLE', \
                                        'ru' : 'No entries found', \
                                        'be' : 'Status:    AVAILABLE',  #Causing Issues 
                                        'pl' : 'No information available', \
                                        'br' : 'No match for', \
                                        'name' : 'No match', \
                                        'cc' : 'No match', \
                                        'to' : 'No match for', \
                                        'tk' : 'domain name not known', \
                                        'ag' : 'NOT FOUND', \
                                        'se' : 'not found', \
                                        'fr' : 'No entries found', \
                                        'dk' : 'No entries found', \
                                        'ro' : 'No entries found', \
                                        'cz' : 'No data found', \
                                        'ac' : 'is available', \
                                        'ms' : 'is not registered', # Not found text unmapped
                                        'li' : 'not have an entry', \
                                        'am' : 'No match', \
                                        'gr' : 'no entries found', \
                                        'ca' : 'Domain status:         available', \
                                        'mx' : 'Object_Not_Found', \
                                        'cn' : 'no matching record', \
                                        'edu' : 'No Match', \
                                        'lu' : '% No such domain', #Something wrong with this
                                        'cx' : 'No Object Found', \
                                        'jp' : 'No match!!', \
                                        'nu' : 'not found', \
                                        'si' : 'No entries found', #Need to test further
                                        'au' : 'No Data Found', \
                                        'st' : 'No entries found', \
                                        'gov' : 'No match', #Test a gov live site
                                        'ie' : 'Not Registered ', \
                                        'no' : '% No match', \
                                        'as' : 'Not Registered', \
                                        'il' : '% No data was found', \
                                        'bz' : 'No Match', \
                                        'cl' : 'no existe', \
                                        'kr' : 'is not registered', \
                                        'is' : 'No entries found', \
                                        'af' : 'No Object Found', \
                                        'aero' : 'NOT FOUND', \
                                        'sh' : 'is available', \
                                        'sg' : 'Domain Not Found', \
                                        'tm' : 'is available', \
                                        'cd' : 'Domain Status: Available', \
                                        'gf' : 'No match for domain', \
                                        'kz' : 'Nothing found for this query', \
                                        'tj' : 'no match',
                                        'hk' : 'The domain has not been registered.', \
                                        'nz' : '220 Available', \
                                        'yt' : 'No entries found', \
                                        'ug' : 'No entries found'}
        
        
        
        self.creation_date_map =    {'org' : 'Creation Date:\s*(.+)', \
                                        'ca' : 'Creation date:\s*(.+)', \
                                        'info' : 'Created On:\s*(.+)' }

        
        self.updated_date_map =     {'org' : 'Updated Date:\s*(.+)', \
                                     'info' : 'Last Updated On:\s*(.+)'}

        
        self.expiry_date_map =      {'org' : 'Expiry Date:\s*(.+)', \
                                     'info' : 'Expiration Date:\s*(.+)'}


        self.email_map =            {'org' : 'Email:\s*(.+)'}

        
        self.registrant_map =       {'org' : 'Registrant\s*(.+)'}


        self.nameserver_map =       {'org' : 'Name Server:\s*(.+)'}


        self.execeed_map =          {'com' : 'You have exceeded your quota of queries', \
                                        'org' : 'WHOIS LIMIT EXCEEDED', \
                                        'nz' : '440 Request Denied', \
                                        'jp' : 'Cannot process your search request', \
                                        'de' : 'onnection refused; access control limit exceeded', \
                                        'au' : 'BLACKLISTED:', \
                                        'cz' : 'Your connection limit exceeded',
                                        'ms' : 'Lookup quota exceeded', \
                                        'si' : 'Too many queries'}

    
