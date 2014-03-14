#!/usr/bin/env python

import time


class MWhoisUtil():

    def __init__(self):
        pass

    #Copied from pywhois source code. Found at https://code.google.com/p/pywhois/
    @staticmethod
    def parser_date(date_str):
        """
        Convert any date string found in WHOIS to a time object.
        """

        date_str2 = str(date_str)

        known_formats = [
            '%d-%b-%Y', # 02-jan-2000
            '%Y-%m-%d', # 2000-01-02
            '%d-%b-%Y %H:%M:%S %Z',	# 24-Jul-2009 13:20:03 UTC
            '%a %b %d %H:%M:%S %Z %Y', # Tue Jun 21 23:59:59 GMT 2011
            '%Y-%m-%dT%H:%M:%SZ', # 2007-01-26T19:10:31Z
        ]

        for date_format in known_formats:
            try:
                return time.strptime(date_str2.strip(), date_format)
            except ValueError, e:
                pass

        return date_str2
