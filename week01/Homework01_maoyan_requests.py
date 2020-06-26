import requests
from bs4 import BeautifulSoup as bs
import lxml.etree
import pandas as pd

# 定义函数，抓取一部电影的名称、上映时间、类型
def get_url_details(myurl):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    header = {}
    header['user-agent'] = user_agent
    header['cookie'] = '152008582.1592924402976.1593048500190.1593048507765.11; uuid_n_v=v1; uuid=3606CFE0B56211EAAD7CEBC74F78E0F9A2C76C9C7FC84565B9FA67AE92E55BB5; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=172e1b1717bc8-043b1ff79af337-d373666-e1000-172e1b1717b54; _lxsdk=3606CFE0B56211EAAD7CEBC74F78E0F9A2C76C9C7FC84565B9FA67AE92E55BB5; mojo-uuid=189d9c124920320156cc1678e233e012; __mta=152008582.1592924402976.1593010507873.1593010510232.11; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1592924402,1592957478,1593008378,1593045087; _csrf=2b07d75bc2bafea352f2e7a3eb313e4ceecbe8b327d15e4953e41979b272044a; mojo-session-id={"id":"494f9aaf09996adcf635660aed391b6a","time":1593048168568}; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593048514; mojo-trace-id=13; _lxsdk_s=172e911f826-1db-ddf-740%7C%7C22'
    response = requests.get(myurl, headers=header)
    bs_info = bs(response.text, 'html.parser')

    selector = lxml.etree.HTML(response.text)
    # 1、电影名称
    film_name = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')
    # print(f'电影名称：{film_name}')
    # 2、上映时间
    plan_date = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
    # print(f'上映时间：{plan_date}')
    # 3、电影类型
    film_type = []
    for tags in bs_info.find_all('li', attrs={'class': 'ellipsis'}):
        for atags in tags.find_all('a'):
            film_type.append(atags.get_text())
    # print(f'电影类型：{film_type}')
    mylist = [film_name, plan_date, film_type]

    # 将抓取结果存入csv文件
    movie10 = pd.DataFrame(data=mylist)
    # print(movie1)
    movie10.to_csv('./movie10.csv', encoding='utf8', index=False, header=False, mode='a')

# 获取前10名电影的url
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
header = {'user-agent': user_agent, 'cookie':'152008582.1592924402976.1593010194678.1593010730819.6; uuid_n_v=v1; uuid=3606CFE0B56211EAAD7CEBC74F78E0F9A2C76C9C7FC84565B9FA67AE92E55BB5; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=172e1b1717bc8-043b1ff79af337-d373666-e1000-172e1b1717b54; _lxsdk=3606CFE0B56211EAAD7CEBC74F78E0F9A2C76C9C7FC84565B9FA67AE92E55BB5; mojo-uuid=189d9c124920320156cc1678e233e012; _csrf=8ce7169a70b43838417d47a361b90a880e8906f6ac9f5e22cc5e55a9bbbdc294; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1592924402,1592957478,1593008378; mojo-session-id={"id":"e816e24f5c974d3b617efea27625c4bf","time":1593008377946}; __mta=152008582.1592924402976.1593010507873.1593010510232.11; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593010738; mojo-trace-id=20; _lxsdk_s=172e6b2d06f-02b-4b4-36a%7C%7C32'}
myurl = "https://maoyan.com/board/4"
response = requests.get(myurl, headers=header)
bs_info = bs(response.text, 'html.parser')

for tags in bs_info.find_all('div', attrs={'class': 'movie-item-info'}):
    url_index = []
    for atag in tags.find_all('a',):
        url_index = atag.get('href')
        urls = 'https://maoyan.com/' + url_index[1:]
        get_url_details(urls)
     