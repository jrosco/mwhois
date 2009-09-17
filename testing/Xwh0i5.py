#!/usr/bin/env python

"""
@author Joel Cumberland

@contact zeme_6@hotmail.com

@version 0.1.3a

@status: Alpha, non-release

@copyright 2009

@license: GPL

"""

import sys, re, socket

_version = "0.1.3a"
dList = ''
type = ''
domain_found = "Domain Not Found"
domain_foundadv = "Domain Found but could be Parked, a Dead Site or an Un-Popular Domain that is not in your DNS Server Cache" 

class whois_server():
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
            print "Error finding %s please use a different tld to search for." % (e) 
            sys.exit()
    
    def ex(self, regex):
        x = self.exmap[regex]
        return x
    
    def connection(self, domain, who, tld):
        response = ''
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)        
        s.connect((who, 43))
        s.send(domain + "\r\n")
        while True:
            d = s.recv(4096)
            response += d
            if d == '': break     
        
        global dList
        fw = dList
        print whois_search.type
        if whois_search.type == "single":
            print response
            s.close()     
        
        if type == "basic":
            if re.search(self.ex(tld), response):
                    indent = command_display().format_this(domain, 30)
                    print >>fw,  domain + indent + domain_found 
                    print domain + indent + domain_found
                    s.close()             
            else:
                    s.close()
                              
        if type == "advance":
            if re.search(self.ex(tld), response):
                    indent = command_display.format_this(domain, 30)
                    print >>fw, domain + indent + domain_found
                    print domain + indent + domain_found
                    s.close()   
            else:
                    print >>fw, domain + indent + domain_foundadv
                    print domain + indent + domain_foundadv
                    s.close()
        return

class command_display:
    
    def __init__(self):
       self.already = 0
    
    def progress_bar(self, number, total,  char):
       percentage = int(100 - round(number*100.0/total))
       if percentage > 0:
           xchar = char * (percentage-self.already)
           self.already = percentage 
           sys.stdout.write(xchar)
           sys.stdout.flush()                                      
                
                
    def count_lines(self, file):
        linecount = 0
        f = open(file)
        it = iter(f)
        try: 
            while it.next():
                linecount += 1
        except StopIteration:
                    pass
        return linecount
    
    def format_this(self, word, indent):
        wcount = len(word)
        num = (indent - wcount)
        whitespace = " "
        format = whitespace * num
        return format

    
class whois_search():
    
    type = ""
    
    def __init__(self, domain, tld, wordlist, domainlist):
       
       self.domain = domain
       self.tld = tld
       self.wordlist = wordlist
       self.domainlist = domainlist
       self.type = type
       
    def single_search(self):
        
        self.type = "single"
        try:
            domainame,tld = self.domain.split(".") #NOTE // If using a tld like .com.au this will fail, need a better way to determine the tld
            w = whois_server()
            whois = w.who(tld)
            w.connection(self.domain, whois, tld)
        except Exception, e: print e
        return

    
    def basic_search(self):
        
        global dList, type
        dList = open(self.domainlist, 'w')
        type = "basic"
        fr = open(self.wordlist, 'r')
        for line in fr:
            line = line.rstrip() + "." + self.tld
            if not line: break
            try:
                w = whois_server()
                whois = w.who(self.tld)
                w.connection(line, whois, self.tld)
            except Exception, e: print e
        dList.close()
        fr.close()
        return        

    
    def advance_search(self):
        
        advlist = self.domainlist + ".adv"
        wordlist = open(self.wordlist, 'r')
        advfile = open(advlist, 'w+r')
        c = command_display()
        countline = c.count_lines(self.wordlist)
        total = countline
        
        print "Performing a Advanced Search..."
        for line in wordlist:
            c.progress_bar(countline, total, "*")
            line = line.rstrip() + "." + self.tld
            countline-=1
            if not line: break
            try: socket.getaddrinfo(line, socket.AF_INET, 0, socket.SOCK_STREAM)
            except Exception, e:
                while True:
                    print >>advfile,line 
                    break 
        print "100%"
        wordlist.close()
        
        global dList, type
        type = "advance"
        dList = open(self.domainlist, 'w+r')
        for advline in advfile:
            advline = advline.rstrip()
            if not advline: break
            try:
                w = whois_server()
                whois = w.who(tld)
                w.connection(advline, whois, tld)
            except Exception, e: print e
        return 
        dList.close()
        advfile.close()
         
    
w = whois_search('google.com', None, None, None)
w.single_search()
