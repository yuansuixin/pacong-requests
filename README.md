



- 古诗文网的登录
    - requests库的使用
    - urllib库的使用

- 微薄登录，使用的是requests库


- 下载阳光宽频网的视频，
    - 视频资源是通过ajax请求动态加载的
    - 首先抓包得到json数据
    - 对json数据进行解析，获取到需要下载视频的url
    - 由于是ajax请求的，动态添加的，所以需要使用phantomjs进行请求
    - 获取到内容，在进行xpath提取，然后下载

