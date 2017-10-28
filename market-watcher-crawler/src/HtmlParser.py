'''
Created on Oct 26, 2017

@author: xiaolongchen
'''
from bs4 import BeautifulSoup

class HtmlParser(object):
    def __init__(self):
        pass   
    
    def get_bedroom_nr(self, house_types):
        bedroom_nr = 0
        if (len(house_types) > 0):
            bedroom_nr_str = house_types[0].strip()
            bedroom_nr = int(bedroom_nr_str[0 : bedroom_nr_str.find("br")])
        return bedroom_nr
    
        
    def get_size(self, house_types):
        size = 0        
        #area is not mandatory field and it would appear in the middle of the "price -  [area size] -  hood"
        if (len(house_types) == 2):
            size_str = house_types[1].strip()
            size = int(size_str[0 : size_str.find("ft")])
        return size
    
    def get_hood(self, hood):      
        if (hood.find("(") == 0):
            hood = hood[1:len(hood) - 1]
            
        if (hood.find(")") == len(hood) - 1):
            hood = hood[0:len(hood)-2]
            
        return hood
    
    def get_price(self, price_str):
        price = 0
        if (len(price_str) > 0):
            price = int(price_str[1:len(price_str)])
            
        return price
    
    def parse_for_size(self, content):
        soup = BeautifulSoup(content, 'html.parser')        
        size = soup.find('span', attrs={'class':'totalcount'}).contents[0].strip()
        return int(size)
    
    def parser(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        results = soup.find(id='sortable-results').find('ul').find_all('li')
        
        posts = []
        
        for result in results:
            try:
                print(' '.join(format(ord(x), 'b') for x in result.text))
                post = {}
                post["title"] = result.p.a.contents[0]
                post["detail_url"] = result.p.a['href']
                post["city"] = post["detail_url"][post["detail_url"].index('//')+2:post["detail_url"].index('.')].capitalize()
                post["price"] = self.get_price(result.p.find('span', attrs={'class':'result-price'}).contents[0].strip())
                postType = result.p.find('span', attrs={'class':'housing'}).contents[0].strip()
                postTypes = postType.split("-")
                post["bedroom_nr"] = self.get_bedroom_nr(postTypes)
                post["size"] = self.get_size(postTypes)
                post["hood"] = self.get_hood(result.p.find('span', attrs={'class':'result-hood'}).contents[0].strip())
                external_id = result.p.find('span', attrs={'class':'maptag'})
                post["external_id"] = result.p.find('span', attrs={'class':'maptag'})['data-pid']
                post["date_posted"] = result.p.time['datetime']
                posts.append(post)
            except Exception as e:
                print(e)
        
        return posts
            