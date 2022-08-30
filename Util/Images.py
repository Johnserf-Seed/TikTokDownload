#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:Images.py
@Date       :2022/08/30 01:04:34
@Author     :JohnserfSeed
@version    :1.0
@License    :(C)Copyright 2019-2022, Liugroup-NLPR-CASIA
@Github     :https://github.com/johnserf-seed
@Mail       :johnserfseed@gmail.com
-------------------------------------------------
Change Log  :
2022/08/29 22:02:49 : Init
-------------------------------------------------
'''

import Util


class Images():
    def __init__(self):
        # 作品接口
        self.apiUrl = 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids='
        # 作品id
        self.aweme_id = ''
        # 作者id
        self.nickname = ''
        # 作品文案
        self.desc = ''
        # 发布时间
        self.create_time = 0
        # 发布地点
        self.position = ''
        # 图集数量
        self.number = 0
        # 图集链接
        self.images = []

    def get_all_images(self, aweme_id):
        datas = []
        for id in aweme_id:
            r = Util.requests.get(self.apiUrl + str(id),
                                    headers=Util.headers).text
            js = Util.json.loads(r)

            self.nickname = js['item_list'][0]['author']['nickname']
            self.desc = js['item_list'][0]['desc']
            self.create_time = js['item_list'][0]['create_time']
            self.number = len(js['item_list'][0]['images'])

            # 有的作品不会带定位
            try:
                self.position = js['item_list'][0]['aweme_poi_info']['poi_name']
            except:
                self.position = ''

            for i in range(self.number):
                self.images.append(js['item_list'][0]['images'][i]['url_list'][3])

            datas.append([self.nickname, self.desc, self.create_time,
                        self.position, self.number, self.images])
            # 清除上一个作品
            self.images = []
        return datas
