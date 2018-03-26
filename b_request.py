# -*- coding:UTF-8 -*-
import requests

#不带参数的
# url = 'http://www.baidu.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}


# r = requests.get(url,headers=headers)

# 带参数的
url = 'https://www.baidu.com/s?'

data={
    'wd':'美女'
}
r = requests.get(url=url,headers=headers,params=data)
# print(r.text)
# print(r.content)
# print(r.status_code)
# print(headers)






