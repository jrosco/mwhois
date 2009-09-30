# parser.py - Module for parsing whois response data
# Copyright (c) 2008 Andrey Petrov
#
# This module is part of pywhois and is released under
# the MIT license: http://www.opensource.org/licenses/mit-license.php

import re
import exceptions

import time

def cast_date(date_str):
    "Convert any date string found in WHOIS to a time object."
    known_formats = [
        '%d-%b-%Y', # 02-jan-2000
        '%Y-%m-%d', # 2000-01-02
    ]

    r = None
    for fmt in known_formats:
        try:
            r = time.strptime(date_str.strip(), fmt)
        except ValueError, e:
            pass # Wrong format, keep trying

    return r

class WhoisEntry(object):
    """
    Parent class for parsing a Whois entries. Whois entries of different types
    will implement the interface provided by this class.
    """
    _attributes = ['domain_name',
                   'registrar',
                   'whois_server',
                   'referral_url', # http url of whois_server
                   'name_servers', # list of name servers
                   'status',       # list of statuses
                   'updated_date',
                   'creation_date',
                   'expiration_date']
    _parsing_re = {}

    @staticmethod
    def load(domain, text):
        """
        Given whois output in ``text``, return an instance of ``WhoisEntry`` that represents its parsed contents.
        """
        if '/' in domain:
            raise ValueError("'%s' is not a domain." % domain)
        if '.com' in domain:
            return Whois_Com(domain, text)
        else:
            raise exceptions.UnknownTLD(domain)


class Whois_Com(WhoisEntry):
    "Whois parser for .com domains"
    _whois_re = {
            # NOTE: These should all be found following the domain_name match.
            'domain_name':      'Domain Name:\s?(.+)',
            'registrar':        'Registrar:\s?(.+)',
            'whois_server':     'Whois Server:\s?(.+)',
            'referral_url':     'Referral URL:\s?(.+)',
            'updated_date':     'Updated Date:\s?(.+)',
            'creation_date':    'Creation Date:\s?(.+)',
            'expiration_date':  'Expiration Date:\s?(.+)',
            'name_servers':     'Domain Name:\s?(.+)', # There can be many of these
            'status':           'Status:\s?(.+)', # There can be many of these
        }

    # Compile the regular expressions (this occurs on import)
    for key in _whois_re:
        _whois_re[key] = re.compile(_whois_re[key])

    def __init__(self, domain, text):
        self.domain = domain
        self.text = text

    def get(self, attribute):
        """
        Given an attribute, return all matches in the Whois text.
        """
        re_attr = self._whois_re.get(attribute)
        if not re_attr:
            raise KeyError("Unknown attribute: %s" % attribute)

        return re_attr.findall(self.text)
