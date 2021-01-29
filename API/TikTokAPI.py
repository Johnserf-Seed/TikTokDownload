#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:TikTokAPI
@Date       :2021/01/29 13:34:54
@Author     :JohnserfSeed
@version    :1.0
@License    :(C)Copyright 2017-2020, Liugroup-NLPR-CASIA
@Mail       :johnserfseed@gmail.com
'''

import requests,json,re,os
from TikTokMulti import TikTok


class TikTokAPI():

    def __init__(self) -> None:
        self.PCheader = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
        self.iPXheader = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}
        #抖音热榜API
        self.Billboard_Share = 'https://www.iesdouyin.com/share/billboard/?id=0'
        self.Billboard_Hot = 'https://aweme-hl.snssdk.com/aweme/v1/hot/search/list/?detail_list=0&mac_address=08:00:27:29:D2:F5&os_api=23&device_type=MI%205s&device_platform=android&ssmix=a&iid=92152480453&manifest_version_code=860&dpi=320&uuid=008796750074613&version_code=860&app_name=aweme&version_name=8.6.0&ts=1577932778&openudid=c055533a0591b2dc&device_id=69918538596&resolution=810*1440&os_version=6.0.1&language=zh&device_brand=Xiaomi&app_type=normal&ac=wifi&update_version_code=8602&aid=1128&channel=tengxun_new&_rticket=1577932779592'
        self.Billboard_Video = 'https://aweme-hl.snssdk.com/aweme/v1/hot/search/list/?detail_list=1&mac_address=08:00:27:29:D2:F5&os_api=23&device_type=MI%205s&device_platform=android&ssmix=a&iid=92152480453&manifest_version_code=860&dpi=320&uuid=008796750074613&version_code=860&app_name=aweme&version_name=8.6.0&ts=1577932778&openudid=c055533a0591b2dc&device_id=69918538596&resolution=810*1440&os_version=6.0.1&language=zh&device_brand=Xiaomi&app_type=normal&ac=wifi&update_version_code=8602&aid=1128&channel=tengxun_new&_rticket=1577932779592'
        pass

    def Get_Tk_Billboard(self):
        
        pass

    def Set_Tk_Billboard(self):

        pass


if __name__ == "__main__":
    pass