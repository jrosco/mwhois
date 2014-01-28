#!/usr/bin/env python 

import os
import re
import sys

import const as CONST
from whoissearch import WhoisSearch

if __name__ == "__main__":
    
    #search = WhoisSearch(dname='google.de').single_search()
    
    basic = WhoisSearch(tld='com', wordlist='./wordlist.txt').basic_search()
    
    #print search
        
        