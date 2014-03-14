#!/usr/bin/env python 

import re
import logging

from whomap import WhoisServerMap
import util
import const as CONST
from exception import WhoException


class WhoisInfo(WhoisServerMap):

    def __init__(self):

        WhoisServerMap.__init__(self)

        self.logger = logging.getLogger(__name__)

        self.logger.debug('constructor: __init__()')

        self.domain = ''
        self.tld = ''
        self.whoisserver = ''
        self.response = ''
        self.not_found = ''
        self.exceeded = ''
        self.emails = ''
        self.second_server = False
        self.tld_type = ''

        self.mwhois_util = util.MWhoisUtil()

    def get_whois_server(self):

        self.logger.debug('called get_whois_server() domain = %s', self.domain)

        if self.second_server is False:

            self.logger.debug('no second server needed')
            list_number = 0

        else:

            self.logger.debug('second server needed, must have exceeded limit!!')
            list_number = 1

        try:
            if self.domain is not None:
                self.logger.debug('%s domain is set', self.domain)
                self.get_domain_tld()

            self.whoisserver = self.all_server_map[self.tld][list_number]
            #self.whoisserver =  server_map[self.tld]
            self.logger.debug('return %s', self.whoisserver)

            #self.logger.info('Querying %s' % self.whoisserver)

        except WhoException:

            if self.second_server is True:
                self.logger.info("problem mapping second whois server")
            else:
                self.logger.info("problem mapping whois server with %s please use a different tld to search for.",
                                 self.tld)
        return self.whoisserver

    def tld_not_found_text(self):

        self.logger.debug('called tld_not_found_text()')

        try:
            self.not_found = self.all_server_map[self.tld][2]
            self.logger.debug('return not found text = %s', self.not_found)

            return self.not_found

        except WhoException, e:
            self.logger.error("dead domain text not found")

    def exceeded_limit(self):

        self.logger.debug('called exceeded_limit()')

        try:
            self.exceeded = self.all_server_map[self.tld][3]
            self.logger.debug('return exceeded text = %s for tld %s', self.exceeded, self.tld)

        except WhoException, e:

            self.logger.debug("exceeded text not found")

        return self.exceeded

    def get_domain_tld(self):

        self.logger.debug('called get_domain_tld()')

        self.tld = re.split('[. :]', self.domain)
        self.tld = self.tld[-1]
        self.logger.debug('return %s', self.tld)

        return self.tld

    def get_list_supported_tlds(self):

        self.logger.debug('called get_list_supported_tlds()')

        return self.all_server_map

    def get_tld_type(self):

        self.logger.debug('called get_tld_type()')

        try:

            self.tld_type = self.all_server_map[self.tld]
            self.logger.debug('tld type is %s' % self.tld_type)

        except WhoException, e:

            self.logger.error('tld type error: %s' % e)

        return self.tld_type[4]

    #TODO: Fix typo should be named get_response()
    def get_repsonse(self):

        self.logger.debug('called get_repsonse()')

        return self.response

    def get_whois_attr(self, whois_attr):

        self.logger.debug('called get_whois_attr()')

        if self.get_tld_type() is CONST.GTLD_DONUTS:
            self.tld = CONST.GTLD_DONUTS
        elif self.get_tld_type() is CONST.GTLD_UNITED:
            self.tld = CONST.GTLD_UNITED
        elif self.get_tld_type() is CONST.GTLD_UNIREG:
            self.tld = CONST.GTLD_UNIREG

        try:

            if whois_attr is CONST.CDATE:
                whois_attr = self.all_info_map[self.tld][0]

            elif whois_attr is CONST.EDATE:
                whois_attr = self.all_info_map[self.tld][1]

            elif whois_attr is CONST.UPDATE:
                whois_attr = self.mwhois_util.parser_date(whois_attr)

            elif whois_attr is CONST.REGISTRANT:
                whois_attr = self.all_info_map[self.tld][3]

            elif whois_attr is CONST.NAMESERVER:
                whois_attr = self.all_info_map[self.tld][4]

            elif whois_attr is CONST.WHOIS_STATUS:
                whois_attr = self.all_info_map[self.tld][5]

            self.logger.debug('return %s', whois_attr)

            whois_attr_list = []

            for item in re.findall(whois_attr, self.response):
                whois_attr_list.append(item)

        except WhoException:

            self.logger.info('No attr %s', self.whois_attr)

        return whois_attr_list

    def get_all_emails(self):

        self.logger.debug('called get_all_emails()')

        self.emails = re.findall(self.list_of_emails, self.response)

        return self.emails

    def is_domain_alive(self):

        self.logger.debug('called is_domain_alive()')

        self.tld_not_found_text()
        self.exceeded_limit()

        if not self.response:
            self.logger.error('%s status is unknown, try again' % self.domain)
            return CONST.DOMAIN_STATUS_UNKNOWN

        if re.search(self.exceeded, self.response) and self.exceeded != '':

            self.second_server = True
            self.logger.info('%s you have exceeded your quota of queries (oops)', self.domain)
            self.logger.info('Lets try a different server...')

            return CONST.DOMAIN_SEARCH_EXCEEDED

        if re.search(self.not_found, self.response):

            self.logger.debug('%s domain is dead', self.domain)
            return CONST.DOMAIN_DEAD

        else:

            self.logger.debug('%s domain is alive', self.domain)
            return CONST.DOMAIN_ALIVE
