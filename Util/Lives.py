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
        live_api = 'https://live.douyin.com/webcast/room/web/enter/?aid=6383&device_platform=web&web_rid=%s' % (web_rid)

        headers = {
            'Cookie': 'msToken=tsQyL2_m4XgtIij2GZfyu8XNXBfTGELdreF1jeIJTyktxMqf5MMIna8m1bv7zYz4pGLinNP2TvISbrzvFubLR8khwmAVLfImoWo3Ecnl_956MgOK9kOBdwM=; odin_tt=6db0a7d68fd2147ddaf4db0b911551e472d698d7b84a64a24cf07c49bdc5594b2fb7a42fd125332977218dd517a36ec3c658f84cebc6f806032eff34b36909607d5452f0f9d898810c369cd75fd5fb15; ttwid=1%7CfhiqLOzu_UksmD8_muF_TNvFyV909d0cw8CSRsmnbr0%7C1662368529%7C048a4e969ec3570e84a5faa3518aa7e16332cfc7fbcb789780135d33a34d94d2'
        }

        response = Util.requests.request("GET", live_api, headers=headers)
        while response.text == '':
            print('[   🎦   ]:获取直播信息失败，正在重新获取\r')
            response = Util.requests.request("GET", live_api, headers=headers)
        live_json = Util.json.loads(response.text)

        return live_json

if __name__ == '__main__':
    Lives()
