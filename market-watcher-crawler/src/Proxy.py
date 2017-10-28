'''
Created on Oct 28, 2017

@author: xiaolongchen
'''
import random
from requests.auth import HTTPProxyAuth

class Proxy(object):
    def __init__(self):
        self.proxies = [{"https": "http://199.101.97.130:60099"}, {"https": "http://199.101.97.146:60099"}]
        
        self.auth = {
            "username": "bittiger", "password": "cs504"
        }
    
    def pick(self):
        return random.choice(self.proxies)
        
        
    def auth(self):
        return HTTPProxyAuth(self.auth["username"], self.auth["password"])
    
    