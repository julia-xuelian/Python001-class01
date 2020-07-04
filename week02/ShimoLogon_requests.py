import time
import requests
from fake_useragent import UserAgent
import lxml.etree

ua = UserAgent(verify_ssl=False)
headers = {
'User-Agent' : ua.random,
'Referer' : 'https://shimo.im/login?from=home'
}

s = requests.Session()
# 会话对象：在同一个 Session 实例发出的所有请求之间保持 cookie， 
# 期间使用 urllib3 的 connection pooling 功能。
# 向同一主机发送多个请求，底层的 TCP 连接将会被重用，从而带来显著的性能提升。
login_url = 'https://arms-retcode.aliyuncs.com/r.png?t=api&times=1&page=shimo.im%2Flogin&tag=&release=&environment=prod&begin=1593782961975&api=shimo.im%2Flizard-api%2Fauth%2Fpassword%2Flogin&success=0&time=254&code=400&msg=&traceId=45eaad61159378296197510015f9ff&pv_id=7nkkwc9k66z9yt6kq2v0epevyyk0&domain=shimo.im&sr=1280x720&vp=1280x616&ct=4g&uid=9Lk3jbvgyU2dqe5ppz1Iv9asg8ht&sid=1mkvLcIm6kb7nIwqglXmeOj4esL3&pid=cuvx0xni1o%401a8e4117575f9ff&_v=1.8.16&sampling=1&z=kc6962et&post_res='
form_data = {
'mobile': '8613500600789',
'password': '111111'
}

s_get = requests.get('https://shimo.im/login?from=home', headers=headers)
s_html = lxml.etree.HTML(s_get.text)
s_text = s_html.xpath('/html/head/meta[13]/@content')
print(s_text)