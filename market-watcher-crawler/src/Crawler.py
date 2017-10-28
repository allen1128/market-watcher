'''
Created on Oct 14, 2017

@author: xl
'''

from RealEstatePostRepo import RealEstatePostRepo
from UrlManager import UrlManager
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser

class Crawler:
    
    def __init__(self):
        self.urlManager = UrlManager()
        self.htmlDownloader = HtmlDownloader()
        self.htmlParser = HtmlParser()
        urls = []
        urls.append("https://vancouver.craigslist.ca/search/rea?s=")
        #urls.append("base": "https://montreal.craigslist.ca/search/rea?s=")
        #urls.append("https://toronto.craigslist.ca/search/rea?s=")
                
        for url in urls:
            html = self.htmlDownloader.download(url)
            size = self.htmlParser.parse_for_size(html)
            self.urlManager.generate_new_urls(url, size, 120)
            
        
    def execute(self):
        repRep = RealEstatePostRepo()
        
        while (self.urlManager.has_new_url()):
            try:
                url =  self.urlManager.get_new_url()
                html = self.htmlDownloader.download(url)
                post = self.htmlParser.parser(html)
                repRep.send_to_mq(post)
            except Exception as e:
                print(e)
                
        print("end!")
        

if __name__ == '__main__':
    crawler = Crawler()
    crawler.execute()
    
    
    
    