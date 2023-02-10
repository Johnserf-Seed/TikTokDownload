#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:XB.py
@Date       :2023/02/09 00:29:30
@Author     :JohnserfSeed
@version    :0.0.1
@License    :Apache License 2.0
@Github     :https://github.com/johnserf-seed
@Mail       :johnserf-seed@foxmail.com
-------------------------------------------------
Change Log  :
2023/02/09 00:29:30 - Create XBogus class
-------------------------------------------------
'''
import json
import requests
from .Urls import Urls
from urllib.parse import urlencode, unquote, parse_qsl


class XBogus:
    def __init__(self, url, cookie=None, referer="https://www.douyin.com/") -> None:
        self.urls = Urls()
        self.headers = {
            "cookie": cookie,
            "referer": referer,
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
        }
        self.getXbogus(url)

    def getXbogus(self, url):
        try:
            if isinstance(url, dict):
                params = eval(unquote(url, 'utf-8'))
                url = urlencode(params, safe="=")
                response = json.loads(requests.post(
                    self.urls.GET_XB_DICT + url,
                        headers = self.headers).text)
            if isinstance(url, str):
                url = url.replace('&','%26')
                response = json.loads(requests.post(
                    self.urls.GET_XB_PATH + url,
                        headers = self.headers).text)
            else:
                print('[  提示  ]:传入的参数有误')
        except Exception as e:
            print('[  错误  ]:%s' % e)

        self.params = response["result"][0]["paramsencode"]
        self.xb = response["result"][0]["X-Bogus"]["0"]
        # print('[  调试  ]:%s' % self.params)
        return (self.params, self.xb)