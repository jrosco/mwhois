#!/usr/bin/env python 


class WhoException(Exception):
    
    def __init__(self, error):
        self.error = error
        Exception.__init__(self, 'Error: %s' % self.error)
        pass