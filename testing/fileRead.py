import socket
from socket import gethostbyaddr


############################################################TESTING AREA##############################################################

wordList = '/tmp/Wordlist'
domainList = '/tmp/domains.txt'
f = open(wordList, 'r')
fd = open(domainList, 'w')


def readDomain(ext):
    
    for line in f:
        
        line = line.rstrip() + ext
        if not line:
            break
   
        try:
            #socket(AF_INET, SOCK_STREAM, [53])
            gethostbyaddr("www" + line)
            #socket.getaddrinfo(line, None, 0, socket.SOCK_STREAM)
            
        except Exception, e:
            while True:
                #if e == Exception.__getattribute__(1, 'Unknown host'):
                    print >>fd,line, e 
                    print line, e #debugging
                    break
            
    return                 
                      
readDomain(".com")
f.close()

######################################################END OF TESTING AREA###############################################################

