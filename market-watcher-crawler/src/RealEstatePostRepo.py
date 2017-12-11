'''
Created on Oct 14, 2017

@author: xiaolongchen
'''

import pymysql
import time
import pika
import json

class RealEstatePostRepo:
    
    def __init__(self):
        self.db_conn = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='',
                             db='market_watch',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        self.mq_credentials = pika.PlainCredentials('guest', 'guest')
        self.mq_conn = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672,'/', self.mq_credentials))
        #self.mq_conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=15672))
        self.mq_channel = self.mq_conn.channel()
        self.mq_queue_name = "real_estate_post_queue"
        self.mq_channel.queue_declare(queue=self.mq_queue_name)        
        
    def save_to_db(self, posts):
            with self.db_conn.cursor() as cursor:
                for post in posts:
                    try:
                        sql = "INSERT INTO real_estate (title, hood, price, size, bedroom_nr, date_posted, detail_url, city) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
                        #datetime =  h.date_posted.strftime('%Y-%m-%d %H:%M:%S')
                        cursor.execute(sql, (post.title, post.postood, post.price, post.size, post.bedroom_nr,post.date_posted, post.detail_url, post.city))
                    except Exception as ex:
                        print(ex)
                                        
                self.db_conn.commit()
                
    def send_to_mq(self, posts):
        for post in posts:
            self.mq_channel.basic_publish(exchange='', routing_key=self.mq_queue_name, body=json.dumps(post))
                    
            
    def __del__(self):
        self.db_conn.close()
        self.mq_conn.close()
        
        
        
        