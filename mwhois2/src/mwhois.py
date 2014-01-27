#!/usr/bin/env python 

import sys, os
sys.path.append(os.path.abspath("../lib"))
from whoisconn import WhoisServerConnection
from whoismap import WhoisServerMap

if __name__ == "__main__":
        x = WhoisServerMap('info')
        y = x.whois_server()
        who = WhoisServerConnection('google.info', y, 'net')
        who.connection()
        x.regex()
        #print who.single()