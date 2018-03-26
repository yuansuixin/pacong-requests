# -*- coding:UTF-8 -*-
import http.cookiejar
import urllib
import urllib.request
import urllib.parse
from lxml import etree

# 提取表单令牌函数
def catch_data(opener):
    url = 'http://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
    headers =  {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    request = urllib.request.Request(url=url, headers=headers)
    response = opener.open(request)
    tree = etree.HTML(response.read())
    #
    view_state = tree.xpath('//input[@id="__VIEWSTATE"]/@value')[0]
    view_state_generator = tree.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value')[0]
    return view_state,view_state_generator


def generator_session():
    cj = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(handler)
    return opener


def login():
    # 经分析发现，验证码网址是同一个网址，不带参数，因该是通过会话进行控制的，所以需要通过会话来实现登录
    opener = generator_session()
    # 登录页面中需要提取参数,需要发送get请求
    view_state, view_state_generator = catch_data(opener)
    post_url = 'http://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
    request = urllib.request.Request(url=post_url,headers=headers)
    image_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
    code_url = 'http://so.gushiwen.org/RandCode.ashx'
    image_request = urllib.request.Request(url=code_url,headers=image_header)
    ret = opener.open(image_request)
    with open('code.png','wb',) as f:
        f.write(ret.read())
    code = input('请输入验证码')


    # 表单数据
    data = {
        ' __VIEWSTATE': 'grUgpURYzMVZgwBQndAH9WrdCSGpmqyQmKQCUcRA / WrPs1Z3WCETjqFK4EKanLgu8aWJ7nEiMadyykhFygh2NkNJcKR3a1uOhyHGBSXXLxUmCAIQsYaU1RkaC3E =',
        '__VIEWSTATEGENERATOR': 'C93BE1AE',
        'from': 'http: // so.gushiwen.org / user / collect.aspx',
        'email': '1090509990@qq.com',
        'pwd': '123456',
        'code': code,
        'denglu': ' 登录',
    }
    data = urllib.parse.urlencode(data).encode()
    response = opener.open(request,data=data)

    with open('gushi.html', 'w',encoding='utf8') as f:
        f.write(response.read().decode())


def main():
    login()

if __name__ == '__main__':
    main()
