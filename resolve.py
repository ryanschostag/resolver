#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 16:11:35 2018

@author: Ryan Schostag
"""

import socket


class IPMapper(object):
    """ Maps IPv4 addresses to hosts """
    def __init__(self, host):
        super()
        self.host_map = self.resolve(host)

    def resolve(self, host):
        """ 
        Returns the IPv4 address of a given host
        """
        
        results = {}
        
        if isinstance(host, list) or isinstance(host, tuple):
            for h in host:
                results[h] = socket.gethostbyname(h)
        
        if isinstance(host, str):
            results[host] = socket.gethostbyname(host)
            
        return results

        
if __name__ == "__main__":
    hosts = ['google.com', 'yahoo.com', 'purple.com', 'localhost']
    mapper = IPMapper(hosts)
    hosts_map = mapper.host_map
    print(hosts_map)
