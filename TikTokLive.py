#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:TikTokLive.py
@Date       :2022/09/15 17:29:10
@Author     :JohnserfSeed
@version    :1.0
@License    :MIT License
@Github     :https://github.com/johnserf-seed
@Mail       :johnserfseed@gmail.com
-------------------------------------------------
Change Log  :
-------------------------------------------------
'''

import Util

cmd = Util.Command()

live_url = Util.reFind(input('[   📺   ]:输入抖音直播间web端链接，例如 https://live.douyin.com/176819813905：'))

while live_url == '':
    live_url = Util.reFind(input('[   📺   ]:请输入正确的链接：'))

Util.Lives(cmd).get_Live(live_url)