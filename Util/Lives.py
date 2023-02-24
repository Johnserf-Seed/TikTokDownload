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

        odin_tt = 'a09d8eb0d95b7b9adb4b6fc6591918bfb996096967a7aa4305bd81b5150a8199d2e29ed21883cdd7709c5beaa2be3baa'

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            'Cookie': f'ttwid={Util.generate_ttwid};{odin_tt}'
            }

        response = Util.requests.request("GET", live_api, headers=headers)
        if response.text == '':
            input('[   🎦   ]:获取直播信息失败，请从web端获取新ttwid\r')
            exit()
        live_json = Util.json.loads(response.text)

        return live_json

if __name__ == '__main__':
    Lives()
