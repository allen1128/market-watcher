'''
Created on Oct 14, 2017

@author: xiaolongchen
'''

import pymysql
import time

class RealEstatePostRepo:
    conn = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='',
                             db='market_watch',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    def save(self, posts):
            with self.conn.cursor() as cursor:
                for post in posts:
                    try:
                        sql = "INSERT INTO real_estate (title, hood, price, size, bedroom_nr, date_posted, detail_url, city) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
                        #datetime =  h.date_posted.strftime('%Y-%m-%d %H:%M:%S')
                        cursor.execute(sql, (post.title, post.postood, post.price, post.size, post.bedroom_nr,post.date_posted, post.detail_url, post.city))
                    except Exception as ex:
                        print(ex)
                                        
                self.conn.commit()        
            
    def __del__(self):
        self.conn.close()
        
        
        
        