# -*- coding:UTF-8 -*-
import requests

# 通过requests创建一个会话，然后，后续都通过这个会话访问
# 这个对象有get和post方法，方法的使用和requests.get的使用方式一样
session = requests.Session()

# post
post_url = 'https://passport.weibo.cn/sso/login/'

data ={
'username': '17701256561',
	'password': 'lizhibin666',
	'savestate': '1',
	'r': 'http://weibo.cn/',
	'ec': '0',
	'pagerefer': '',
	'entry': 'mweibo',
	'wentry': '',
	'loginfrom': '',
	'client_id': '',
	'code': '',
	'qq': '',
	'mainpageflag': '1',
	'hff': '',
	'hfp': ''
}
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
	'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&r=http%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt='
}


r = session.post(url=post_url,data=data,headers=headers)

# 访问登录后的页面

url = 'https://weibo.cn/6388179289/info'
headers1 = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
r = session.get(url=url,headers=headers,)
print(r.text)



