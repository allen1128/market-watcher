'''
Created on Oct 26, 2017

@author: xiaolongchen
'''

class UrlManager(object):
    def __init__(self):
            self.new_urls = set()
            self.old_urls = set()
            
    def has_new_url(self):
        return self.new_urls.size() > 0;
    
    def get_new_url(self): 
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
    
    def add_new_url(self, url):
        self.new_urls.add(url)
        
    
    def add_new_urls(self, urls):
        for url in urls:
            self.add_new_url(url)
               
    
    def get_new_url_size(self):
        return self.new_urls.size() 
    
    def get_old_url_size(self):
        return self.old_urls.size()
    
    def generate_new_urls(self, base_url, query_range, step_size):
        for position in range(query_range):
            new_url = base_url + "?s=" + position
            self.add_new_url(new_url)
            position += step_size