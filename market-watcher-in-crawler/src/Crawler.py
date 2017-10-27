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
        urls.add({"city": "Vancouver", "url": "https://vancouver.craigslist.ca/search/rea?s="})
        urls.add({"city": "Montreal", "url": "https://montreal.craigslist.ca/search/rea?s="})
        urls.add({"city": "Toronto", "url": "https://toronto.craigslist.ca/search/rea?s="})
        
        
        for url in urls:
            html = self.htmlDownloader(url)
            size = self.htmlParser.parse_for_size(html)
            self.urlManager.generate_new_urls(url, size, 120)
        
    def execute(self):
        posts = []
        repRep = RealEstatePostRepo()     
        count = 0
        while (self.urlManager.has_new_url()):
            try:
                url =  self.urlManager.get_new_url()
                html = self.htmlDownloader.download(url.url)
                post = self.htmlParser.parser(html)
                post.city = url.city
                posts.add(post)
                
                if count > 100:
                    repRep.save(posts)
                    posts = []
                    count = 0
                    
                count += 1
            except Exception:
                print("crawler failed")
        
        if (posts.size() > 0):
            repRep.save(posts)
        print("end!")
        

if __name__ == '__main__':
    crawler = Crawler()
    crawler.execute()
    
    
    
    