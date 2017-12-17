import threading

class CrawlerThread(threading.Thread):
    urlLock = threading.Lock()
    mqLock = threading.Lock()
    
    def __init__(self, urlManager, repRep, downloader, parser):
        threading.Thread.__init__(self)
        self.urlManager = urlManager
        self.repRep = repRep
        self.downloader = downloader
        self.parser = parser

    def run(self):
        print(self.getName() + " started")
        
        while (self.urlManager.has_new_url()):
            #print("has new url to crawl")
            try:
                CrawlerThread.urlLock.acquire()
                #print("lock is acquired by" + self.getName())
                url =  self.urlManager.get_new_url()
                CrawlerThread.urlLock.release()
                #print("lock is released by" + self.getName())
                
                if (url != ""):
                    html = self.downloader.download(url)
                    post = self.parser.parser(html)
                    print("getting the posts of size: %d" %len(post))
                    print("%s is crawled in %s" %(url, self.getName()))
                    CrawlerThread.mqLock.acquire()
                    self.repRep.send_to_mq(post)    
                    CrawlerThread.mqLock.release()
                else:
                    print("empty url string")
                    
                
            except Exception as e:
                print(e)
        
        print("end")
        