# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from maoyanmovie.items import MaoyanmovieItem
from scrapy.selector import Selector

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/4']

    # def parse(self, response):
    #     pass

    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        for i in range(0, 1):
            url = f'https://maoyan.com/board/4?offset={i*10}'
            yield scrapy.Request(url=url, callback=self.parse)
            # url 请求访问的网址
            # callback 回调函数，引擎会将下载好的页面(Response对象)发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # 解析函数
    # 2a. 在items.py定义
    # def parse(self, response):
    #     items = []
    #     soup = BeautifulSoup(response.text, 'html.parser')
    #     title_list = soup.find_all('div', attrs={'class': 'movie-item-info'})
       
    #     for i in range(len(title_list)):
    #         item = MaoyanmovieItem()
    #         title = title_list[i].find('a').get('title')
    #         link = 'https://maoyan.com' + title_list[i].find('a').get('href')
    #         plan_date = title_list[i].find('p', attrs={'class': 'releasetime'}).get_text()
    #         item['title'] = title
    #         item['link'] = link
    #         item['plan_date'] = plan_date
    #         items.append(item)
    #     return items
        
    # 2b. 在items.py定义
    def parse(self, response):
        items = []
        soup = BeautifulSoup(response.text, 'html.parser')
        title_list = soup.find_all('div', attrs={'class': 'movie-item-info'})
       
        for i in title_list:
            item = MaoyanmovieItem()
            title = i.find('a').get('title')
            link = 'https://maoyan.com' + i.find('a').get('href')
            plan_date = i.find('p', attrs={'class': 'releasetime'}).get_text()
            item['title'] = title
            item['link'] = link
            item['plan_date'] = plan_date
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        soup = BeautifulSoup(response.text, 'html.parser')
        classifications = soup.find('li', attrs={'class': 'ellipsis'}).get_text().strip()
        item['classifications'] = classifications
        yield item

    # # 2c. 使用scrapy选择器
    # def parse(self, response):
    #     items = []
    #     # 打印网页的url
    #     print(response.url)
    #     movies = Selector(response=response).xpath('//div[@class="movie-item-info"]')

    #     for movie in movies:
    #         item = MaoyanmovieItem()
    #         title = movie.xpath('./p/a/@title')
    #         link = 'https://maoyan.com' + (movie.xpath('./p/a/@href')).extract()[0]
    #         plan_date = movie.xpath('./p[@class="releasetime"]/text()')
    #         # print('-----------')
    #         # print(title.extract_first())
    #         # print(link)
    #         # print(plan_date.extract_first())
    #         item['title'] = title
    #         item['link'] = link
    #         item['plan_date'] = plan_date
    #         yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    # def parse2(self, response):
    #     item = response.meta['item']
    #     movies = Selector(response=response).xpath('//li[@class="ellipsis"]')
    #     classifications = movies.xpath('./a/text()')
    #     item['classifications'] = classifications
    #     yield item

