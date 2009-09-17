import re
import socket
import sys
import fileselect
import whois

class basicSearch:
    
    def __init__(self, tld):
        
        self.tld = tld
        fr = open(wordList, 'r')
        fd = open(domainFound, 'w')
        
        for line in fr:
            response = ''
            line = line.rstrip() + "." + tld
            if not line: break
            try:
                w = whois.whoisServer()
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)   
                s.connect((w.who(tld), 43))
                s.send(line + "\r\n")
                while True:
                    d = s.recv(4096)
                    response += d
                    if d == '':
                        break
                if re.search(w.ex(tld), response):
                    print line + " Domain Not Found" 
                    print >>fd, line + " Domain Not Found" #TODO // Use a better format 
                    s.close()   
                else:
                    #print line +" Domain Found" #debugging
                    s.close()
            except socket.error, e:
                print "Connection Error", e
                s.close()
                
        fr.close()
        return
    sys.exit()




