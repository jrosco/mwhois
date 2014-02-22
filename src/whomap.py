#!/usr/bin/env python

import re

class WhoisServerMap(object):
        
    def __init__(self):
        
        
        self.list_of_emails = r'[\w.-]+@[\w.-]+'
        
        #Structure
        # ['first_server, 'second _server', 'status', 'exceeded']
        
        self.all_server_map = { 'ac': ['whois.nic.ac','', 'is available'    ,''], \
                        'aero': ['whois.aero','', 'NOT FOUND' ,''], \
                        'af': ['whois.nic.af','', 'No Object Found',''], \
                        'ag': ['whois.nic.ag','', 'NOT FOUND' ,''], \
                        'am': ['whois.nic.am','', 'No match' ,''], \
                        'as': ['whois.nic.as','', 'Not Registered' ,''], \
                        'at': ['whois.nic.at','', 'nothing found' ,''], \
                        'au': ['whois.aunic.net','', 'No Data Found' ,''], \
                        'be': ['whois.dns.be','', 'Status: [   AVAILABLE' ,''], \
                        'biz': ['whois.biz','', 'Not found' ,''], \
                        'bj': ['whois.nic.bj','', ''], \
                        'br': ['whois.registro.br','', 'No match for' ,''], \
                        'bz': ['whois.belizenic.bz','', 'No Match' ,''], \
                        'ca': ['whois.cira.ca','whois.domainpeople.com', 'Domain status: .*available' ,''], \
                        'cat': ['whois.cat','', ''], \
                        'cc': ['whois.nic.cc','', 'No match' ,''], \
                        'cd': ['whois.nic.cd','', 'Domain Status: Available' ,''], \
                        'ch': ['whois.nic.ch','', 'not have an entry' ,''], \
                        'ci': ['whois.nic.ci','', ''], \
                        'cl': ['whois.nic.cl','', 'no existe' ,''], \
                        'cn': ['whois.cnnic.net.cn','', 'no matching record' ,''], \
                        'com': ['whois.verisign-grs.com','whois.domain.com', 'No match for' ,'You have exceeded your quota of queries'], \
                        'coop': ['whois.nic.coop','', ''], \
                        'cx': ['whois.nic.cx','', 'No Object Found' ,''], \
                        'cz': ['whois.nic.cz','', 'No data found' ,''], \
                        'de': ['whois.denic.de','', 'Status: free' ,'access control limit exceeded'], \
                        'dk': ['whois.dk-hostmaster.dk','', 'No entries found' ,''], \
                        'edu': ['whois.educause.edu','', 'No Match' ,''], \
                        'ee': ['whois.eenet.ee','', ''], \
                        'eu': ['whois.eu','', 'AVAILABLE'], \
                        'fi': ['whois.ficora.fi','', ''], \
                        'fr': ['whois.nic.fr','', 'No entries found' ,''], \
                        'gf': ['whois.internic.net','', 'No match for domain' ,''], \
                        'gg': ['whois.channelisles.net','', ''], \
                        'gov': ['whois.dotgov.gov','', 'No match',''], \
                        'gr': ['whois.ripe.net','', 'no entries found' ,''], \
                        'graphics' : ['whois.donuts.co','','Domain not found',''], \
                        'guru' : ['whois.donuts.co','','Domain not found',''], \
                        'hk': ['whois.hkirc.net.hk','', 'The domain has not been registered.' ,''], \
                        'hn': ['whois2.afilias-grs.net','', ''], \
                        'hu': ['whois.nic.hu','', ''], \
                        'ie': ['whois.domainregistry.ie','', 'Not Registered ' ,''], \
                        'il': ['whois.isoc.org.il','', '% No data was found' ,''], \
                        'in': ['whois.inregistry.net','', ''], \
                        'info': ['whois.afilias.info','', 'NOT FOUND' ,''], \
                        'int': ['whois.iana.org','', ''], \
                        'io': ['whois.nic.io','', ''], \
                        'is': ['whois.isnic.is','', 'No entries found' ,''], \
                        'it': ['whois.nic.it','', 'AVAILABLE' ,''], \
                        'jp': ['whois.jprs.jp','', 'No match!!' ,''], \
                        'ke': ['whois.kenic.or.ke','', ''], \
                        'kr': ['whois.nic.or.kr','', 'is not registered' ,''], \
                        'kz': ['whois.nic.kz','', 'Nothing found for this query' ,''], \
                        'li': ['whois.nic.li','', 'not have an entry' ,''], \
                        'lt': ['whois.domreg.lt','', ''], \
                        'lu': ['whois.dns.lu','', '% No such domain' ,''], \
                        'lv': ['whois.nic.lv','', ''], \
                        'me': ['me.whois-servers.net', '', '', ''], \
                        'mg': ['whois.nic.mg','', ''], \
                        'mil': ['whois.nic.mil','', ''], \
                        'mn': ['whois.nic.mn','', ''], \
                        'ms': ['whois.adamsnames.tc','', 'is not registered' ,''], \
                        'museum': ['whois.museum','', ''], \
                        'mx': ['whois.nic.mx','', 'Object_Not_Found' ,''], \
                        'my': ['whois.mynic.net.my','', ''], \
                        'na': ['whois.na-nic.com.na','', ''], \
                        'name': ['whois.nic.name','', 'No match' ,''], \
                        'net': ['whois.markmonitor.com','whois.internic.net', 'No match for' ,''], \
                        'nl': ['whois.domain-registry.nl','', 'is free' ,''], \
                        'no': ['whois.norid.no','', '% No match' ,''], \
                        'nu': ['whois.nic.nu','', 'not found' ,''], \
                        'nz': ['whois.srs.net.nz','', '220 Available' ,''], \
                        'org': ['whois.publicinterestregistry.net','whois.domain.com', 'NOT FOUND' ,'WHOIS LIMIT EXCEEDED'], \
                        'pl': ['whois.dns.pl','', 'No information available' ,''], \
                        'pm': ['whois.nic.pm','', ''], \
                        'pr': ['whois.uprr.pr','', ''], \
                        'pro': ['whois.registrypro.pro','', ''], \
                        're': ['whois.nic.re','', ''], \
                        'ro': ['whois.rotld.ro','', 'No entries found' ,''], \
                        'ru': ['whois.ripn.net','', 'No entries found' ,''], \
                        'se': ['whois.iis.se','', 'not found' ,''], \
                        'sg': ['whois.nic.net.sg','', 'Domain Not Found' ,''], \
                        'sh': ['whois.nic.sh','', 'is available' ,''], \
                        'si': ['whois.arnes.si','', 'No entries found' ,''], \
                        'st': ['whois.nic.st','', 'No entries found' ,''], \
                        'technology' : ['whois.donuts.co','','Domain not found',''], \
                        'tf': ['whois.nic.tf','', ''], \
                        'tj': ['whois.nic.tj','', 'no match' ,''], \
                        'tk': ['whois.dot.tk','', 'domain name not known' ,''], \
                        'tl': ['whois.nic.tl','', ''], \
                        'tm': ['whois.nic.tm','', 'is available' ,''], \
                        'to': ['monarch.tonic.to','', 'No match for' ,''], \
                        'today' : ['whois.donuts.co','','Domain not found',''], \
                        'tr': ['whois.nic.tr','', ''], \
                        'tv': ['whois.nic.tv','', 'No match for' ,''], \
                        'tw': ['whois.twnic.net.tw','', ''], \
                        'ua': ['whois.net.ua','', ''], \
                        'ug': ['whois.co.ug','', 'No entries found' ,''], \
                        'uk': ['whois.nic.uk','', 'no match' ,''], \
                        'us': ['whois.nic.us','', 'Not found' ,''], \
                        'uz': ['whois.cctld.uz','', ''], \
                        've': ['whois.nic.ve','', ''], \
                        'wf': ['whois.nic.wf','', ''], \
                        'ws': ['whois.nic.ws','', 'No match for' ,''], \
                        'yt': ['whois.nic.yt','', 'No entries found' ,''], \
                        'xxx': ['whois.nic.xxx','whois.internic.net','NOT FOUND','']}
        
        
        self.all_info_map = { 'ac' : ['N/A', 'Expiry :\s*(.+)', 'N/A', 'N/A', 'N/A'], \
                         'aero' : ['N/A', 'Expires On:\s*(.+)', 'Updated On:\s*(.+)', 'Registrant\s*(.+)', 'Name Server:\s*(.+)'], \
                         'af' : ['Creation Date\s*(.+)', 'Registry Expiry Date\s*(.+)', 'Updated Date:\s*(.+)', 'Registrant\s*(.+)', 'Name Server:\s*(.+)'], \
                         'ag' : ['Created On\s*(.+)', 'Expiration Date:\s*(.+)', 'Last Updated On:\s*(.+)', 'Registrant\s*(.+)', 'Name Server:\s*(.+)'], \
                         'am' : ['Registered:\s*(.+)', 'Expires:\s*(.+)', 'Last modified:\s*(.+)', 'Registrant:\s*(.+)', 'N/A'], \
                         'as' : ['Created:\s*(.+)', 'Expires:\s*(.+)', 'N/A', 'Registrant:\s*(.+)', 'Name Servers:\s*(.+)'], \
                         'at' : ['N/A', 'N/A', 'N/A', 'registrant:\s*(.+)', 'N/A'], \
                         'au' : ['N/A', 'N/A', 'N/A', 'Registrant\s*(.+)', 'N/A'], \
                         'be' : ['N/A', 'N/A', 'N/A', 'Registrant:\s*(.+)', 'Nameservers:\s*(.+)'], \
                         'biz' : ['Created\s*(.+)', 'Expiration Date:\s*(.+)', 'Last Updated Date:\s*(.+)', 'Registrant\s*(.+)', 'Name Server:\s*(.+)'], \
                         'bj' : ['N/A', 'N/A', 'Last Updated:\s*(.+)', 'N/A', 'N/A'], \
                         'br' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'bz' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'ca' : ['Creation date:\s*(.+)', 'Expiry date:\s*(.+)', 'Updated date:\s*(.+)', 'Registrant:\s*(.+)', 'Name servers:\s*(.+)'], \
                         'cat' : ['Created On\s*(.+)', 'Expiration Date:\s*(.+)', 'Last Updated On:\s*(.+)', 'Registrant\s*(.+)', 'Name Server\s*(.+)'], \
                         'cc' : ['Creation Date\s*(.+)', 'N/A', 'N/A', 'N/A', 'Name Server:\s*(.+)'], \
                         'cd' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'ch' : ['N/A', 'N/A', 'N/A', 'N/A', 'Name servers:\s*(.+)'], \
                         'ci' : ['N/A', 'Expiration date:\s*(.+)', 'N/A', 'N/A', 'Nameserver:\s*(.+)'], \
                         'cl' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'cn' : ['N/A', 'Expiration Date:\s*(.+)', 'N/A', 'Registrant\s*(.+)', 'Name Server:\s*(.+)'], \
                         'com' : ['Creation Date:\s*(.+)', ' Expiration Date:\s*(.+)', 'Updated Date:\s*(.+)', 'Registrant\s*(.+)', 'Name Server:\s*(.+)'], \
                         'coop' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'cx' : ['Creation Date\s*(.+)', 'Registry Expiry Date\s*(.+)', 'Updated Date:\s*(.+)', 'Registrant\s*(.+)', 'Name Server:\s*(.+)'], \
                         'cz' : ['created:\s*(.+)', 'N/A', 'N/A', 'registrant:\s*(.+)', 'N/A'], \
                         'de' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'dk' : ['N/A', 'Expires:\s*(.+)', 'N/A', 'N/A', 'Nameservers\s*(.+)'], \
                         'edu' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'ee' : ['created:\s*(.+)', 'N/A', 'N/A', 'registrant:\s*(.+)', 'N/A'], \
                         'eu' : ['N/A', 'N/A', 'N/A', 'N/A', 'Name servers:\s*(.+)'], \
                         'fi' : ['created:\s*(.+)', 'expires:\s*(.+)', 'N/A', 'N/A', 'N/A'], \
                         'fr' : ['created:\s*(.+)', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'gf' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'gg' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'gov' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'gr' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'graphics' : ['Creation Date:\s*(.+)','Expiry Date:\s*(.+)','Updated Date:\s*(.+)','Registrant\s*(.+)', 'Name Server:\s*(.+)'], \
                         'guru' : ['Creation Date:\s*(.+)','Expiry Date:\s*(.+)','Updated Date:\s*(.+)','Registrant\s*(.+)', 'Name Server:\s*(.+)'], \
                         'hk' : ['N/A', 'Expiry Date:\s*(.+)', 'N/A', 'N/A', 'Name Server:\s*(.+)'], \
                         'hn' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'hu' : ['record created\s*(.+)', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'ie' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'il' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'in' : ['Created On\s*(.+)', 'Expiration Date:\s*(.+)', 'Last Updated On:\s*(.+)', 'Registrant\s*(.+)', 'Name Server:\s*(.+)'], \
                         'info' : ['Created On\s*(.+)', 'Expiration Date:\s*(.+)', 'Last Updated On:\s*(.+)', 'Registrant\s*(.+)', 'Name Server:\s*(.+)'], \
                         'int' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'io' : ['N/A', 'Expires :\s*(.+)', 'Last Updated :\s*(.+)', 'N/A', 'N/A'], \
                         'is' : ['created:\s*(.+)', 'expires:\s*(.+)', 'N/A', 'N/A', 'N/A'], \
                         'it' : ['Created:\s*(.+)', 'N/A', 'N/A', 'N/A', 'Nameservers\s*(.+)'], \
                         'jp' : ['Created on\s*(.+)', 'Expires on\s*(.+)', 'Last Updated\s*(.+)', 'N/A', 'Name Server\s*(.+)'], \
                         'ke' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'kr' : ['N/A', 'Expiration Date             :\s*(.+)', 'Last Updated Date           :\s*(.+)', 'Registrant\s*(.+)', 'Name Server\s*(.+)'], \
                         'kz' : ['Domain created\s*(.+)', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'li' : ['N/A', 'N/A', 'N/A', 'N/A', 'Name servers:\s*(.+)'], \
                         'lt' : ['N/A', 'N/A', 'N/A', 'N/A', 'Nameserver:\s*(.+)'], \
                         'lu' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'lv' : ['N/A', 'N/A', 'Updated:\s*(.+)', 'N/A', 'N/A'], \
                         'me' : ['Create Date:\s*(.+)', 'Expiration Date:\s*(.+)', 'Updated Date:\s*(.+)', 'Registrant \s*(.+)', 'Nameservers:\s*(.+)'], \
                         'mg' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'mil' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'mn' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'ms' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'museum' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'mx' : ['Created On\s*(.+)', 'Expiration Date:   \s*(.+)', 'Last Updated On:   \s*(.+)', 'N/A', 'Name Servers:\s*(.+)'], \
                         'my' : ['Record Created\s*(.+)', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'na' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'name' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'net' : ['Creation Date\s*(.+)', 'N/A', 'Updated Date:\s*(.+)', 'Registrant\s*(.+)', 'Name Server:\s*(.+)'], \
                         'nl' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'no' : ['N/A', 'N/A', 'Last updated:\s*(.+)', 'N/A', 'N/A'], \
                         'nu' : ['N/A', 'expires:\s*(.+)', 'N/A', 'N/A', 'N/A'], \
                         'nz' : ['domain_date registered:\s*(.+)', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'org' : ['Creation Date:\s*(.+)', 'Expiry Date:\s*(.+)', 'Updated Date:\s*(.+)', 'Registrant\s*(.+)', 'Name Server:\s*(.+)'], \
                         'pl' : ['option created:\s*(.+)', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'pm' : ['created:\s*(.+)', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'pr' : ['N/A', 'expiration date:       \s*(.+)', 'N/A', 'N/A', 'N/A'], \
                         'pro' : ['created:\s*(.+)', 'Expiration Date:\s*(.+)', 'Last Updated On:\s*(.+)', 'Registrant\s*(.+)', 'Name Server:\s*(.+)'], \
                         're' : ['created:\s*(.+)', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'ro' : ['Registered On:\s*(.+)', 'N/A', 'N/A', 'N/A', 'Nameserver:\s*(.+)'], \
                         'ru' : ['created:\s*(.+)', 'N/A', 'Last updated on\s*(.+)', 'N/A', 'N/A'], \
                         'se' : ['created:\s*(.+)', 'expires:\s*(.+)', 'N/A', 'N/A', 'N/A'], \
                         'sg' : ['Creation Date\s*(.+)', 'Expiration Date:\s*(.+)', 'N/A', 'N/A', 'Name Servers:\s*(.+)'], \
                         'sh' : ['N/A', 'Expiry :\s*(.+)', 'N/A', 'N/A', 'N/A'], \
                         'si' : ['created:\s*(.+)', 'N/A', 'N/A', 'N/A', 'nameserver:\s*(.+)'], \
                         'st' : ['created-date:\s*(.+)', 'expiration-date:\s*(.+)', 'updated-date:\s*(.+)', 'registrant-\s*(.+)', 'Name Server:\s*(.+)'], \
                         'technology' : ['Creation Date:\s*(.+)','Expiry Date:\s*(.+)','Updated Date:\s*(.+)','Registrant\s*(.+)', 'Name Server:\s*(.+)'], \
                         'tf' : ['created:\s*(.+)', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'tj' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'tk' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'tl' : ['Creation Date\s*(.+)', 'Expiry Date:\s*(.+)', 'Updated Date:\s*(.+)', 'Registrant\s*(.+)', 'Name Server:\s*(.+)'], \
                         'tm' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'to' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'today' : ['Creation Date:\s*(.+)','Expiry Date:\s*(.+)','Updated Date:\s*(.+)','Registrant\s*(.+)', 'Name Server:\s*(.+)'], \
                         'tr' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'tv' : ['Creation Date\s*(.+)', 'N/A', 'Updated Date:\s*(.+)', 'N/A', 'Name Server:\s*(.+)'], \
                         'tw' : ['Record created on\s*(.+)', 'expires on\s*(.+)', 'N/A', 'Registrant\s*(.+)', 'N/A'], \
                         'ua' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'ug' : ['Registered:\s*(.+)', 'Expiry:             \s*(.+)', 'Updated:\s*(.+)', 'N/A', 'Nameserver:\s*(.+)'], \
                         'uk' : ['Registered on:\s*(.+)', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'us' : ['Last Transferred Date:\s*(.+)', 'Expiration Date:\s*(.+)', 'Domain Last Updated Date:\s*(.+)', 'Registrant\s*(.+)', 'Name Server:\s*(.+)'], \
                         'uz' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         've' : ['N/A', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'wf' : ['created:\s*(.+)', 'N/A', 'N/A', 'N/A', 'N/A'], \
                         'ws' : ['Creation Date\s*(.+)', 'Expiration Date:\s*(.+)', 'Updated Date:\s*(.+)', 'Registrant\s*(.+)', 'Name Server:\s*(.+)'], \
                         'yt' : ['created:\s*(.+)', 'anniversary:\s*(.+)', 'last-update:\s*(.+)', 'N/A', 'N/A' ], \
                         'xxx': ['Creation Date:\s*(.+)','Updated Date:\s*(.+)','Expiry Date:\s*(.+)','Registrant\s*(.+)','Name Server:\s*(.+)']}
           