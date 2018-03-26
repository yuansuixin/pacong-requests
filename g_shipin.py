# -*- coding:UTF-8 -*-
import json

import os
import requests
import time
from lxml import etree


# 下载今日头条的视频
from selenium import webdriver


def get_video_list(widen):
    url = 'https://365yg.com/'
    ajax_url = 'https://365yg.com/api/pc/feed/?category=video&utm_source=toutiao&widen=%s' % widen
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
    #向url发送请求，获取响应，并解析
    r = requests.get(url=ajax_url, headers=headers)
    # 获取到的都是json数据，抓包得到
    # 解析json数据的两种方式：jsonpath、 转化为Python对象进行遍历
    obj = json.loads(r.text)
    video_lt = obj['data']
    for video_dict in video_lt:
        video_name = video_dict['video_id']
        # 获取视频里的a连接
        video_url = url + video_dict['source_url']
        # 根据name和url下载视频
        print('%s.mp4正在下载' % video_name)
        download_video(video_name, video_url)
        print('%s.mp4下载结束' % video_name)




def download_video(video_name, video_url):
    video_name = video_name+'.mp4'
    dirname = 'jinri'
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    file_path = os.path.join(dirname,video_name)
    # 发送请求，找到src属性，根据这个属性去下载视频
    # 获取视频src属性,直接获取不对，video标签是动态添加的，要通过phantomjs进行请求，并且执行其中的js代码
    # 创建浏览器对象
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
    path = r'F:\qf第三阶段\day05\day05_下午\ziliao\phantomjs-2.1.1-windows\bin\phantomjs.exe'
    brower = webdriver.PhantomJS(path)
    brower.get(video_url)
    time.sleep(3)
    # 首先将页面内容保存到本地，查看有没有video标签，有的话在进行你自己的提取
    # with open('test.html', 'w', encoding='utf8') as fp:
    # 	fp.write(brower.page_source)
    tree = etree.HTML(brower.page_source)
    print(brower.page_source)
    src = tree.xpath('//video/source/@src')[0]
    r = requests.get(url=src,headers=headers)
    with open(file_path,'wb') as f:
        f.write(r.content)


def main():
    start = 1
    end = 1
    for widen in range(start, end + 1):
        print('第%s页开始下载' % widen)
        get_video_list(widen)
        print('第%s页结束下载' % widen)


if __name__ == '__main__':
    main()
