#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:Config.py
@Date       :2022/07/29 23:18:47
@Author     :JohnserfSeed
@version    :1.0
@License    :(C)Copyright 2019-2022, Liugroup-NLPR-CASIA
@Github     :https://github.com/johnserf-seed
@Mail       :johnserfseed@gmail.com
-------------------------------------------------
Change Log  :
2022/07/29 23:18:47 : Init
2022/08/16 18:34:27 : Add log moudle
-------------------------------------------------
'''

import Util

class Config:

    def __init__(self):
        self.headers = Util.headers
        self.default = {
            'uid': 'https://v.douyin.com/k9NXNcH/',
            'music': 'yes',
            'path': 'Download',
            'mode': 'post'
        }

    def check(self):
        """检查配置文件，不存在就生成默认配置文件

        Returns:
            self.cf: 配置文件对象
        """
        # 实例化读取配置文件
        self.cf = Util.configparser.ConfigParser()

        if Util.os.path.isfile("conf.ini") == True:
            # 用utf-8防止出错
            self.cf.read("conf.ini", encoding="utf-8")
        else:
            print('[  提示  ]:没有检测到配置文件，生成中!\r')
            Util.log.info('[  提示  ]:没有检测到配置文件，生成中!')
            try:
                # 往配置文件写入内容
                self.cf.add_section("uid")
                self.cf.set("uid", "uid", "https://v.douyin.com/JcjJ5Tq/")
                self.cf.add_section("music")
                self.cf.set("music", "music", "yes")
                # self.cf.add_section("path")
                # self.cf.set("path", "path", ".\\Download\\")
                self.cf.add_section("mode")
                self.cf.set("mode", "mode", "post")
                with open("conf.ini", "w") as f:
                    self.cf.write(f)
                print('[  提示  ]:生成成功!\r')
                Util.log.info('[  提示  ]:生成成功!')
            except Exception as e:
                Util.log.error(e)
                self.download()
        return self.cf

    def download(self):
        """下载配置文件
        """
        try:
            print('[  提示  ]:从GitHub为您下载配置文件!\r')
            Util.log.info('[  提示  ]:从GitHub为您下载配置文件!')
            r = Util.requests.get(
                'https://cdn.jsdelivr.net/gh/Johnserf-Seed/TikTokDownload@main/conf.ini')
            with open("conf.ini", "w") as f:
                f.write(r.content)
            print('[  提示  ]:下载成功!\r')
            Util.log.info('[  提示  ]:下载成功!')
        except Exception as e:
            print('[  提示  ]:下载失败，请检查网络!\r')
            Util.log.info('[  提示  ]:下载失败，请检查网络!')
        return

if __name__ == '__main__':
    Config()
