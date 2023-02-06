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
2023/01/14 17:35:31 : 更换接口
-------------------------------------------------
'''

import Util


class Images():
    def __init__(self):
        # 作品接口
        self.apiUrl = 'https://www.iesdouyin.com/aweme/v1/web/aweme/detail/?aweme_id={id}&aid=1128&version_name=23.5.0&device_platform=android&os_version=2333'        # 作品id
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
            r = Util.requests.get(self.apiUrl.format(id = str(id)),
                                    headers=Util.headers).text
            js = Util.json.loads(r)

            self.nickname = js['aweme_detail']['author']['nickname']
            self.nickname = Util.replaceT(self.nickname)
            self.desc = js['aweme_detail']['desc']
            self.create_time = js['aweme_detail']['create_time']
            self.number = len(js['aweme_detail']['images'])

            # 有的作品不会带定位
            try:
                self.position = js['aweme_detail']['aweme_poi_info']['poi_name']
            except:
                self.position = ''

            for i in range(self.number):
                self.images.append(js['aweme_detail']
                                    ['images'][i]['url_list'][3])

            datas.append([self.nickname, self.desc, self.create_time,
                            self.position, self.number, self.images])
            # 清除上一个作品
            self.images = []
        return datas
