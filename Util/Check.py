#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:Check.py
@Date       :2022/08/16 18:34:27
@Author     :JohnserfSeed
@version    :1.0
@License    :(C)Copyright 2019-2022, Liugroup-NLPR-CASIA
@Github     :https://github.com/johnserf-seed
@Mail       :johnserfseed@gmail.com
-------------------------------------------------
Change Log  :
2022/08/16 18:34:27 : Init
-------------------------------------------------
'''

import Util

class CheckInfo():

    def __init__(self):
        pass

    # 检测视频是否已经下载过
    def test(self, path, creat_time, file_name, file_type):
        return Util.os.path.exists(path + creat_time + file_name + file_type)
if __name__ == '__main__':
    CheckInfo()
