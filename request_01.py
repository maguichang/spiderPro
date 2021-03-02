# -*- coding: utf-8 -*-
# @Time    : 2021/3/2 15:55
# @Author  : ma gui chang
# @FileName: request_01.py

"""
UA: User-Agent(请求载体的身份标识)
UA检测：门户网站的服务器会检测对应请求的身份标识，如果检测到请求载体身份标识为某一款浏览器，说明
该请求是一个正常的请求。否则为不正常的请求（爬虫），服务器可能拒绝该请求。
UA伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器。
"""
import requests


if __name__ == "__main__":

    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 FS'
    }
    # 处理Url携带的参数
    url = "https://www.sogou.com/web"
    kw = input('enter a word:')
    param = {
        'query': kw
    }
    # 对指定的url发起请求
    response = requests.get(url=url, params=param, headers=headers).text
    file_name = kw+'.html'
    with open(file_name, 'w', encoding='utf-8') as fp:
        fp.write(response)
    print("爬虫结束!!!")



