#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:V1.py
@Date       :2022/07/29 23:19:14
@Author     :JohnserfSeed
@version    :1.0
@License    :(C)Copyright 2019-2022, Liugroup-NLPR-CASIA
@Github     :https://github.com/johnserf-seed
@Mail       :johnserfseed@gmail.com
-------------------------------------------------
Change Log  :
2022/07/29 23:19:14 : Init
2023/03/10 16:22:19 : gen dyheaders
-------------------------------------------------
'''

import Util

class Tool():
    def __init__(self):
        pass

if __name__ == '__main__':
    # 获取命令行参数
    cmd = Util.Command()
    # 获取headers
    headers = Util.Cookies(cmd.setting()).dyheaders
    # 获取主页内容
    profile = Util.Profile(headers)
    # 使用参数并下载
    profile.getProfile(cmd.setting())

    input('[  完成  ]:已完成批量下载，输入任意键后退出:')
