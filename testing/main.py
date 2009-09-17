#!/usr/bin/env python

"""
@author Joel Cumberland

@contact zeme_6@hotmail.com

@version 0.1.3a

@status: Alpha, non-release

@copyright 2009

@license: GPL

"""

_version = '0.1.3a'
import whois
from optparse import OptionParser
import sys
        

def main():
    usage = "usage: %prog [options] [file-to-read-from] [file-to-write-too]"
    parser = OptionParser(usage=usage)

    parser.add_option("-t", "--tld", action="store", type="string", dest="tld",
                      help="--tld com/net/org - Search for these TLD's (Only use one of these tlds for each whois search")

    parser.add_option("-a", "--advance", action="store_true", dest="advance", help="Advanced Search")
    
    parser.add_option("-i", "--file-in", dest="filein",  type="string", help="File to read from")
    
    parser.add_option("-o", "--file-out", dest="fileout", type="string",  help="File to write to")
    
    (options, args) = parser.parse_args()
    
    strtld =  options.tld
    stradv = options.advance
    strfilein =  options.filein
    strfileout = options.fileout
    
    w = whois.whois_search(None, strtld, strfilein, strfileout)
    if stradv == True:
        w.advance_search()
    else:
        pass
        w.basic_search()
    
if __name__ == "__main__":
        main()

