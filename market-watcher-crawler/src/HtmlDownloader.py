'''
Created on Oct 26, 2017

@author: xiaolongchen
'''

import requests
from Proxy import Proxy

class HtmlDownloader(object):
    
    
    def download(self, url):
        proxy = Proxy()
        
        if url is None:
            return None 
        user_agent = 'Mozilla/ 4. 0 (compatible; MSIE 5. 5; Windows NT)'
        headers = {'User-Agent': user_agent}
        r = requests.get(url, headers, proxy.pick(), proxy.auth())
        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text
        return None