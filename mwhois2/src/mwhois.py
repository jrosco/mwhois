#!/usr/bin/env python 

import sys, os
sys.path.append(os.path.abspath("../lib"))
from wconn import WhoisServerConnection
from wmap import WhoisServerMap

if __name__ == "__main__":
        x = WhoisServerMap('info')
        y = x.wserver()
        who = WhoisServerConnection('google.info', y, 'net')
        who.connection()
        print who.single()