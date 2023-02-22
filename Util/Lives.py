#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:Live.py
@Date       :2022/09/15 16:48:34
@Author     :JohnserfSeed
@version    :1.0
@License    :(C)Copyright 2019-2022, Liugroup-NLPR-CASIA
@Github     :https://github.com/johnserf-seed
@Mail       :johnserfseed@gmail.com
-------------------------------------------------
Change Log  :
-------------------------------------------------
'''
import Util

class Lives():

    def __init__(self):
        pass
    def get_Live(live_url:str):

        web_rid = live_url.replace('https://live.douyin.com/','')
        # 2023/02/06 https://live.douyin.com/webcast/room/web/enter/

        live_api = Util.Urls().LIVE + Util.XBogus('aid=6383&device_platform=web&web_rid=%s' % (web_rid)).params

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            'Cookie': 'ttwid=1%7Ch5y5kqyWCBm-83nsJVded8JSFUBP6_6NqHUmPoZPbsk%7C1677073080%7Ca5a22c1959315d00a8d89cf1d088fb4de5720e45c262d53f389ec0f6373c8475;'
            }

        response = Util.requests.request("GET", live_api, headers=headers)
        if response.text == '':
            input('[   🎦   ]:获取直播信息失败，请从web端获取新ttwid\r')
            exit()
        live_json = Util.json.loads(response.text)

        return live_json

if __name__ == '__main__':
    Lives()
