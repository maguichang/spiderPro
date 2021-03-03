# -*- coding: utf-8 -*-
# @Time    : 2021/3/3 20:22
# @Author  : Ma gui chang
# @FileName: request_02.py

import requests
import json


if __name__ == "__main__":

    # 1、指定url
    post_url = 'https://fanyi.baidu.com/sug'
    # 2、UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 FS'
    }
    # 3、post请求参数处理
    data = {
        'kw': 'dog'
    }
    # 4、请求发送
    response = requests.post(url=post_url, data=data, headers=headers)
    # 5、获取响应数据：json() 方法返回的是obj（如果确认返回是json数据类型）
    dic_obj = response.json()
    # 6、持久化数据
    fp = open('./dog.json', 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)
    print("over!!!")
