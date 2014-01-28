#!/usr/bin/env python 

import os
import sys

from whoisconn import WhoisServerConnection
import const as CONST

class WhoisSearch():
    
    def __init__(self, wordlist=None, domainlist=None, dname=None, tld=None, deadonly=False):
    
        self.wordlist = wordlist
        self.domainlist = domainlist
        self.dname = dname
        self.tld = tld
        self.deadonly = deadonly
        
      
    def single_search(self):
        
        w = WhoisServerConnection()
        w.domain = self.dname
        w.get_whois_server()
        w.connection()
        
        self.response = w.whois_search()
        return self.response

    
    def basic_search(self):
    
        w = WhoisServerConnection()
        w.tld = self.tld
        #fwrite = open(self.domainlist, 'w')
        
        fread = open(self.wordlist, 'r')
        for line in fread:
            w.domain = line.rstrip() + "." + self.tld
            w.get_whois_server()
            w.connection()
            alive = w.is_domain_alive()
            if alive == CONST.DOMAIN_DEAD:
                print "Domain %s is dead! provided by whois server %s" % (w.domain, w.whoisserver)
            elif alive == CONST.DOMAIN_ALIVE and self.deadonly == False or self.deadonly == None:
                print "Domain %s is alive! provided by whois server %s" % (w.domain, w.whoisserver)
#             else:
#                 print "Error getting domain %s and file line %s" % (w.domain, line)
#         
        fread.close()
        return 
 
     
#     def advance_search(self):
#      
#         advfile = open(self.domainlist + ".adv", 'w')
#         wordlist = open(self.wordlist, 'r')
#         c = CLDisplay()
#         countline = c.count_lines(self.wordlist)
#         total = countline
#         
#         if not self.textbox: print "Performing a Advanced Search..."
#         for line in wordlist:
#             c.progress_bar(countline, total, "*")
#             line = CLDisplay().remove_whitespace(line)
#             line = line.rstrip() + "." + self.tld
#             countline-=1
#             if not line: break
#             try: socket.getaddrinfo(line, socket.AF_INET, 0, socket.SOCK_STREAM)
#             except Exception, e:
#                 while True:
#                     print >>advfile,line
#             break 
#         print "100%"
#         advfile.close()
#         wordlist.close()
#         
#         dlist = open(self.domainlist, 'w')
#         advfile = open(self.domainlist + ".adv", 'r')
#         for advline in advfile:
#             advline = advline.rstrip()
#             if not advline: break
#             try:
#                 w = WhoisServer()
#                 whois = w.who(self.tld)
#                 w.connection(advline, whois, self.tld)
#                 domain, status = w.advance()
#                 write = WriteFile(domain, dlist, True)
#                 if not domain:del domain
#                 else:
#                     if self.textbox:
#                         indent = CLDisplay().format_this(domain, 30)
#                         if status == DOMAIN_ALIVE:
#                             self.textbox.AppendText(domain+indent+"\t"+DOMAIN_FOUND+"\n")
#                         if status == DOMAIN_DEAD:
#                             self.textbox.AppendText(domain+indent+"\t"+DOMAIN_FOUND_ADV+"\n")
#                     else:write.advance(status) 
#             except Exception, e: print e
#         advfile.close()
#         dlist.close()
#         return     
#     
# 
#     def set_text_box(self, object):
#         self.textbox = object
#         
