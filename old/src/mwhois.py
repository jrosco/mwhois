#!/usr/bin/env python


"""
@author Joel Cumberland
@contact joel_c@zoho.com
@version 0.1.10a
@status: Alpha, non-release
@copyright 2009
@license: GPL

"""

import sys, re, socket, getpass, os
from optparse import OptionParser
from threading import *

"""
Check if WX Module installed 
"""
try:import wx
except ImportError:pass 
else:from mgui import *

_version = "0.1.10a"

DOMAIN_FOUND = "Domain Available"
DOMAIN_FOUND_ADV = "Domain Found but could be Parked, a Dead Site or a Redirected Domain" 
DOMAIN_DEAD = 0
DOMAIN_ALIVE = 1
SINGLE_TYPE=1
BASIC_TYPE=2
ADV_TYPE=3
START_WITH_GUI=1


class WhoisServer:
        
    """
    TODO // Have a way to produce a fall-back/Redundant server if the default one FAILS!!!
    A list of whois server to be used
    """
    whoismap = {         'de' : 'whois.denic.de', \
                                        'uk' : 'whois.nic.uk', \
                                        'com' : 'whois.verisign-grs.com', \
                                        'net': 'whois.internic.net', \
                                        'biz' : 'whois.biz', \
                                        'biz' : 'whois.nic.biz', \
                                        'info' : 'whois.afilias.info', \
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
    
    
    """Regular expression cl_displayed by the output of the whois query performed"""
    exmap =                     {'de' : 'Status: free', \
                                        'uk' : 'no match', \
                                        'com' : 'No match for', \
                                        'net': 'No match for', \
                                        'biz' : 'Not found', \
                                        'info' : 'NOT FOUND', \
                                        'org' : 'NOT FOUND', \
                                        'at' : 'nothing found', \
                                        'tv' : '.tv you have used', \
                                        'ch' : 'not have an entry', \
                                        'nl' : 'is free', \
                                        'us' : 'not found:', \
                                        'ws' : 'no match for', \
                                        'it' : 'AVAILABLE', \
                                        'ru' : 'no entries found', \
                                        'be' : 'no such domain', \
                                        'pl' : 'No information available', \
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
                                        'hk' : 'The domain has not been registered.', \
                                        'nz' : '220 Available'}
        
    
    
    def who(self, tld):
        try:
            w = self.whoismap[tld]
            return w
        except Exception, e:
            print "Error finding %s please use a different tld to search for." % (e) 
            return False
            sys.exit()
    
    def ex(self, regex):
        x = self.exmap[regex]
        return x
    
    """Whois connection"""
    def connection(self, domain, who, tld):
        self.domain = domain
        self.tld = tld
        self.response = ''
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)        
        s.connect((who, 43))
        if tld == "com":
            domain = "="+domain
        s.send(domain + "\r\n")
        while True:
            d = s.recv(4096)
            self.response += d
            if d == '': break     
        s.close()
        
    def single(self):
        return self.response
    
    def basic(self):
        if re.search(self.ex(self.tld), self.response):
            return self.domain
   
    def advance(self):
        if re.search(self.ex(self.tld), self.response):return self.domain, DOMAIN_DEAD
        else:return self.domain, DOMAIN_ALIVE
    

class DBConnection:  
    
    """Create a wordlist from a mysql database"""
    def connection(self, user, passwd, host, port, database, table, column, file):
        
        try:
            import MySQLdb
            
            try:
                if port == None: port = 3306
                if host == None: host = '127.0.0.1'
                db = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=database)
                query = db.cursor()
                query.execute("SELECT %s FROM %s" % (column, table) ) 
                result = query.fetchall()
                file = open(file, 'w')
                for record in result:
                        print >>file, record[0]
            except Exception, e: print e
            
        except:
            print "\nPlease install the MySQL-python Package to use the mysql function\n"
            exit(1)


class WriteFile:
    
    def __init__(self, domain, file, display):
        self.domain = domain
        self.file = file
        self.display = display

    
    def single(self):
        print self.domain
    
    """Print/CLDisplay and write a basic whois search to file """
    def basic(self):
        indent = CLDisplay().format_this(self.domain, 30)
        print >>self.file,  self.domain + indent + DOMAIN_FOUND 
        if self.display == True: print self.domain + indent + DOMAIN_FOUND
    

    """
    Print/CLDisplay and write a advanced whois search to file           
    Print domains that are not found on the whois server/s
    """ 
    def advance(self, status):
        self.status = status
        indent = CLDisplay().format_this(self.domain, 30)
        if self.status == DOMAIN_DEAD:    
            print >>self.file, self.domain + indent + DOMAIN_FOUND
            if self.display == True: print self.domain + indent + DOMAIN_FOUND 
        
        """
        Prints out the domains that are not found by the advanced domain search. These domains could be dead
        sites, not being used on port 80 or could be parked domains. These domains are registred on the whois server
        """
        if self.status == DOMAIN_ALIVE:
            print >>self.file, self.domain + indent + DOMAIN_FOUND_ADV
            if self.display == True: print self.domain + indent + DOMAIN_FOUND_ADV
    
          
class CLDisplay:
    
    def __init__(self):
       """Used by the progress_bar() to keep track of the percentage being used"""
       self.already = 0
    
    """Used by the advanced search, so the user can be shown the program is still running :) """
    def progress_bar(self, number, total,  char):
       percentage = int(100 - round(number*100.0/total))
       if percentage > 0:
           xchar = char * (percentage-self.already)
           self.already = percentage 
           sys.stdout.write(xchar)
           sys.stdout.flush()                                      
                
                
    """Counts the number of lines in a file for the progress_bar()"""
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
    
    """Indents the command line CLDisplay to make it look pretty"""
    def format_this(self, word, indent):
        wcount = len(word)
        num = (indent - wcount)
        whitespace = " "
        format = whitespace * num
        return format
    
    def remove_whitespace(self, str):
        self.str = re.sub("\s+", "", str)
        return self.str
        
        
class WhoisSearch():
    
    def __init__(self, domain, tld, wordlist, domainlist, obj):
    
        self.domain = domain
        self.tld = tld
        self.wordlist = wordlist
        self.domainlist = domainlist
        self.textbox = obj
       
       
    def single_search(self):
        
        try:
            domainame,tld = self.domain.split(".", 1) 
            w = WhoisServer()
            whois = w.who(tld)
            
            if self.textbox and whois == False:
                self.textbox.SetValue("Error finding %s please use a different tld to search for." % (tld))
            w.connection(self.domain, whois, tld)
            self.domain = w.single()
            write = WriteFile(self.domain, None, True)
            if not self.domain:
                del self.domain
            else:
                if self.textbox:
                    self.textbox.SetValue(self.domain)
                else:
                    write.single() 
        except Exception, e: print e
        return self.domain

    
    def basic_search(self):
        
        dlist = open(self.domainlist, 'w')
        fr = open(self.wordlist, 'r')
        for line in fr:
            line = CLDisplay().remove_whitespace(line)
            line = line.rstrip() + "." + self.tld
            if not line: break
            try:
                w = WhoisServer()
                whois = w.who(self.tld)
                w.connection(line, whois, self.tld)
                domain = w.basic()
                write = WriteFile(domain, dlist, True)
                if not domain:del domain
                else:
                    if self.textbox:
                        indent = CLDisplay().format_this(domain, 30)
                        self.textbox.AppendText(domain+indent+"\t"+DOMAIN_FOUND+"\n")
                    else:
                        write.basic()
            except Exception, e: print e
        dlist.close()
        fr.close()
        
        if self.textbox:self.textbox.AppendText("\nFinished")
            
        return 

    
    def advance_search(self):
     
        advfile = open(self.domainlist + ".adv", 'w')
        wordlist = open(self.wordlist, 'r')
        c = CLDisplay()
        countline = c.count_lines(self.wordlist)
        total = countline
        
        if not self.textbox: print "Performing a Advanced Search..."
        for line in wordlist:
            c.progress_bar(countline, total, "*")
            line = CLDisplay().remove_whitespace(line)
            line = line.rstrip() + "." + self.tld
            countline-=1
            if not line: break
            try: socket.getaddrinfo(line, socket.AF_INET, 0, socket.SOCK_STREAM)
            except Exception, e:
                while True:
                    print >>advfile,line
		    break 
        print "100%"
        advfile.close()
        wordlist.close()
        
        dlist = open(self.domainlist, 'w')
        advfile = open(self.domainlist + ".adv", 'r')
        for advline in advfile:
            advline = advline.rstrip()
            if not advline: break
            try:
                w = WhoisServer()
                whois = w.who(self.tld)
                w.connection(advline, whois, self.tld)
                domain, status = w.advance()
                write = WriteFile(domain, dlist, True)
                if not domain:del domain
                else:
                    if self.textbox:
						indent = CLDisplay().format_this(domain, 30)
						if status == DOMAIN_ALIVE:
							self.textbox.AppendText(domain+indent+"\t"+DOMAIN_FOUND+"\n")
						if status == DOMAIN_DEAD:
							self.textbox.AppendText(domain+indent+"\t"+DOMAIN_FOUND_ADV+"\n")
                    else:write.advance(status) 
            except Exception, e: print e
        advfile.close()
        dlist.close()
        return     
    

    def set_text_box(self, object):
        self.textbox = object
        


def main():
    usage = "usage: %prog [options] -i [file-to-read-from] -o [file-to-write-too]\n \n Examples:\n mwhois -t net -i /tmp/wordlist -o /tmp/domains\n mwhois -s sourceforge.net\n mwhois --gui \n\nWordlists Found @ http://www.packetstormsecurity.org/Crackers/wordlists/"
    parser = OptionParser(usage=usage)

    try:
        parser.add_option("-t", "--tld", action="store", type="string", dest="tld",
                          help="--tld com/net/org/biz/edu/info - Search for these TLD's (Only use one of these tlds for each whois search")
        parser.add_option("-s", "--single", action="store_true", dest="single", help="Single domain search")
        parser.add_option("-a", "--advance", action="store_true", dest="advance", help="Advanced domain search")
        parser.add_option("-i", "--file-in", dest="filein",  type="string", help="File to read from")
        parser.add_option("-o", "--file-out", dest="fileout", type="string",  help="File to write to")
        parser.add_option("--sql", action="store_true", dest="sql", help="Connect to a MySQL database")
        parser.add_option("--host", dest="host", type="string", help="Host address for MySQL database connection (Default 127.0.0.1)")
        parser.add_option("--port", dest="port", type="int", help="Port to use for MySQL database connection (Default 3306)")
        parser.add_option("--user", dest="user", type="string", help="User to use for MySQL database connection")
        parser.add_option("-p", "--passwd", action='store_true', dest="passwd",  help="Prompt for a password to use with MySQL database connection")
        parser.add_option("--database", dest="database", type="string", help="Database to use for MySQL database query")
        parser.add_option("--table", dest="table", type="string", help="Table to use for MySQL database query")
        parser.add_option("--column", dest="column", type="string", help="Column to use for MySQL database query")
        parser.add_option("-g", "--gui", action="store_true", dest="gui", help="Start GUI Interface")

        (options, args) = parser.parse_args()
        
        if START_WITH_GUI == 1 or options.gui == True:
            window = StartGUI()
            window.main()
            
        if options.single == True:
            w = WhoisSearch(sys.argv[2], None, None, None, None)
            w.single_search()
        else:
            if options.sql == True:
                options.filein = options.fileout + ".tmp"
                if options.passwd == True:
                    options.passwd = getpass.getpass()
                conn = WhoisServer()
                DBConnection().connection(options.user, options.passwd, options.host, options.port, options.database, options.table, \
                                        options.column, options.filein)
            w = WhoisSearch(None, options.tld, options.filein, options.fileout, None)
            if options.advance == True:
                w.advance_search()
            else:
                w.basic_search()
                
        try: os.remove(options.fileout + ".tmp")
        except Exception, e: pass
        
    except IOError as (errno, strerror):
        print "\nI/O error({0}): {1}".format(errno, strerror) +"\n"
        print parser.get_usage()
        sys.exit()
    
    except KeyboardInterrupt:
        sys.exit()
   
    except:
        print "\nParameter Error\n"
        print parser.get_usage()
        sys.exit()
        


if __name__ == "__main__":
        main()
