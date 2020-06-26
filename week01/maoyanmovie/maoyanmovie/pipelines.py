# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        title = item['title']
        link = item['link']
        plan_date = item['plan_date']
        classifications = item['classifications']
        output = f'|{title}|\t|{link}|\t|{plan_date}|\t|{classifications}|\t|\n\n'
        with open('./maoyanmovie.txt', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item
