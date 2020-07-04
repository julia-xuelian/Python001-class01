# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class MysqlPipeline(object):
    def __init__(self):
        self.db=pymysql.connect(host='localhost',user='root',passwd='123456',
                                db='maoyanmovie',charset='utf8mb4',port=3306)
        self.cur=self.db.cursor()
    def process_item(self, item, spider):
        sql='INSERT INTO maoyan(title,link,plan_date,classifications) VALUES(%s,%s,%s,%s) '
        self.cur.execute(sql,(item['title'],item['link'],item['plan_date'],item['classifications']))
        self.db.commit()
        return item
      
    def close_spider(self, spider):
        self.cur.close()
        self.db.close()

# class MaoyanmoviePipeline:
#     def process_item(self, item, spider):
#         title = item['title']
#         link = item['link']
#         plan_date = item['plan_date']
#         classifications = item['classifications']
#         output = f'|{title}|\t|{link}|\t|{plan_date}|\t|{classifications}|\t|\n\n'
#         with open('./maoyanmovie.txt', 'a+', encoding='utf-8') as article:
#             article.write(output)
#         return item
