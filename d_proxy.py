# -*- coding:UTF-8 -*-
import requests

proxy = {
    'https':'190.207.207.114:8080'
}

url = 'https://www.baidu.com/s?ie=utf-8'

params = {
    'wd':'ip',
}
headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

r = requests.get(url=url,headers=headers,proxies=proxy,params=params)

with open('daili.html','w',encoding='utf-8') as f:
    f.write(r.text)











