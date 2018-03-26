# -*- coding:UTF-8 -*-
import requests

post_url = 'https://www.bing.com/ttranslationlookup?'


headers = {
	'origin': 'https://www.bing.com',
	'referer': 'https://www.bing.com/',
	'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
data = {
	'text': '大象',
	'from': 'zh-CHS',
	'to': 'en',
}

r = requests.post(url=post_url,headers=headers,data=data)
print(r.text)