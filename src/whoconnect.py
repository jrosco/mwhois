#!/usr/bin/env python 

import socket
import time
import logging
from exception import WhoException


class WhoisServerConnection():
    
    def __init__(self, whoinfo):

        self.logger = logging.getLogger(__name__)

        self.logger.debug('constructor: __init__()')
        
        self.whoinfo = whoinfo
        self.sleep = 0
        self.no_of_attempts = 0
        self.timeout = 10
        self.proxy = False
        self.proxy_host = None
        self.proxy_port = 0
        self.proxy_type = None
        self.proxy_user = None
        self.proxy_password = None
        
    def connection(self):

        self.logger.debug('called connection(%s)' % self.whoinfo.whoisserver)

        if self.proxy is True:
            try:
                import socks
                self.logger.debug('called setup proxy()')
                socks.setdefaultproxy(proxy_type=self.proxy_type, addr=self.proxy_host, port=self.proxy_port,
                                      username=self.proxy_user, password=self.proxy_password)
                socket.socket = socks.socksocket
            except Exception, e:
                raise WhoException(e)

        if str(self.whoinfo.whoisserver):
            
            self.logger.debug('sleep for %f', self.sleep)
            time.sleep(self.sleep)
            
            try:
                self.logger.debug('socket: creating socket: fingers crossed ')
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

                sock.settimeout(self.timeout)

                self.logger.debug('socket: %s', sock)
            
            except socket.error as e:
                #self.logger.error('socket: open socket error %s', e)
                raise WhoException(e)
                sock.close()
                
            try:
                self.logger.debug('connecting to server: %s', self.whoinfo.whoisserver)
                sock.connect((self.whoinfo.whoisserver, 43))
            
            except socket.error as e:
                #self.logger.error('socket: connect socket error %s', e, exc_info=True)
                raise WhoException(e)
                sock.close()
                
            try:
                self.logger.debug('socket: now sending data to server (data:%s)', self.whoinfo.domain)
                sock.send(self.whoinfo.domain + '\r\n')
            
            except socket.error as e:
                #self.logger.error('socket: send error %s', e, exc_info=True)
                raise WhoException(e)
                sock.close()
                    
            try:
                
                self.logger.debug('socket: lets clear self.response so we get fresh data')
                self.whoinfo.response = ''
                
                while True:
                    data = sock.recv(4096)
                    self.logger.debug('socket: receiving data')
                    self.whoinfo.response += data
                    if data == '':
                        self.logger.debug('socket: end of data sequence')
                        break     
                
                self.logger.debug('socket: closing socket object %s', sock)
                sock.close()
            
            except Exception as e:
                    raise WhoException(e)
                    sock.close()
        else:
                self.logger.debug('no whois server is set :( ')

        return
