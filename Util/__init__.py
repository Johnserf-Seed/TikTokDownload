#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:__init__.py
@Date       :2022/07/29 23:20:56
@Author     :JohnserfSeed
@version    :1.0
@License    :(C)Copyright 2019-2022, Liugroup-NLPR-CASIA
@Github     :https://github.com/johnserf-seed
@Mail       :johnserfseed@gmail.com
-------------------------------------------------
Change Log  :
2022/07/29 23:20:56 : Init
2022/08/16 18:34:27 : Add moudle Log
-------------------------------------------------
'''

import re
import os
import json
import time
import logging
import requests
import platform
import argparse
import configparser

from .Log import Log
from .Check import CheckInfo
from .Config import Config
from .Command import Command
from .Profile import Profile
from .Download import Download
from .Images import Images

# 日志记录
log = Log()

headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.66'
        }

def replaceT(obj):
        """替换文案非法字符

        Args:
            obj (_type_): 传入对象

        Returns:
            new: 处理后的内容
        """
        # '/ \ : * ? " < > |'
        reSub = r"[\/\\n\:\*\?\"\<\>\|]"
        new = []
        if type(obj) == list:
            for i in obj:
                # 替换为下划线
                retest = re.sub(reSub, "_", i)
                new.append(retest)
        elif type(obj) == str:
            obj.replace('\\','')
            obj.replace('\/','')
            obj.replace(':','')
            obj.replace('*','')
            obj.replace('?','')
            obj.replace('<','')
            obj.replace('>','')
            obj.replace('|','')
            obj.replace('"','')
            new = obj.replace('\n','')
            # 替换为下划线
            # new = re.sub(reSub, "_", obj, 0, re.MULTILINE)
        return new

if (platform.system() == 'Windows'):
    sprit = '\\'
    # 💻
    print('[   💻   ]:Windows平台')
elif (platform.system() == 'Linux'):
    sprit = '/'
    # 🐧
    print('[   🐧   ]:Linux平台')
else:
    sprit = '/'
    # 🍎
    print('[   🍎   ]:MacOS平台')