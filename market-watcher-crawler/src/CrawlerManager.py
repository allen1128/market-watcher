'''
Created on Oct 14, 2017

@author: xl
'''

from RealEstatePostRepo import RealEstatePostRepo
from UrlManager import UrlManager
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from CrawlerThread import CrawlerThread

class CrawlerManager:
    threadSize = 5
    def __init__(self):
        self.urlManager = UrlManager()
        self.htmlDownloader = HtmlDownloader()
        self.htmlParser = HtmlParser()
        self.repo = RealEstatePostRepo()
        urls = []
        urls.append("https://vancouver.craigslist.ca/search/rea?s=")
        urls.append("https://montreal.craigslist.ca/search/rea?s=")
        urls.append("https://toronto.craigslist.ca/search/rea?s=")
                
        for url in urls:
            html = self.htmlDownloader.download(url)
            size = self.htmlParser.parse_for_size(html)
            self.urlManager.generate_new_urls(url, size, 120)
            
        print("total size of urls:", self.urlManager.get_new_url_size())
            
        
    def execute(self):
        for i in range(CrawlerManager.threadSize):
            t = CrawlerThread(self.urlManager, self.repo, self.htmlDownloader, self.htmlParser)
            t.setDaemon(False)
            t.start()

if __name__ == '__main__':
    crawler = CrawlerManager()
    crawler.execute()
    
    
    
    