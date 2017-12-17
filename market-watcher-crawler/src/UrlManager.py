'''
Created on Oct 26, 2017

@author: xiaolongchen
'''

class UrlManager(object):
    def __init__(self):
            self.new_urls = list()
            self.old_urls = list()
            
    def has_new_url(self):
        return len(self.new_urls) > 0
    
    def get_new_url(self): 
        if (self.has_new_url()):
            new_url = self.new_urls.pop()
            self.old_urls.insert(0, new_url)
            return new_url
        else:
            return ""
    
    def add_new_url(self, url):
        self.new_urls.insert(0, url)
        
    
    def add_new_urls(self, urls):
        for url in urls:
            self.add_new_url(url)
               
    
    def get_new_url_size(self):
        return len(self.new_urls) 
    
    def get_old_url_size(self):
        return len(self.old_urls)
    
    def generate_new_urls(self, url, query_range, step_size):
        position = 0
        while position < query_range:
            new_url = url + str(position)
            self.add_new_url(new_url)
            position += step_size