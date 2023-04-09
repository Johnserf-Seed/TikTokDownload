#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:TikTokLive.py
@Date       :2022/09/15 17:29:10
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

live_url = Util.reFind(input('[   📺   ]:输入抖音直播间web端链接，例如 https://live.douyin.com/176819813905：'))[0]

if live_url == '':
    Util.reFind(input('[   📺   ]:请输入正确的链接：'))[0]

json = Util.Lives.get_Live(live_url)

# 是否在播
status = json['data']['data'][0]['status']

if status == 4:
    input('[   📺   ]:当前直播已结束，按回车退出')
    exit(0)

# 直播标题
title = json['data']['data'][0]['title']

# 观看人数
user_count = json['data']['data'][0]['user_count_str']

# 昵称
nickname = Util.replaceT(json['data']['data'][0]['owner']['nickname'])
# sec_uid
sec_uid = json['data']['data'][0]['owner']['sec_uid']

# 直播间观看状态
display_long = json['data']['data'][0]['room_view_stats']['display_long']

# 推流
flv_pull_url = json['data']['data'][0]['stream_url']['flv_pull_url']

try:
    # 分区
    partition = json['data']['partition_road_map']['partition']['title']
    sub_partition = json['data']['partition_road_map']['sub_partition']['partition']['title']
except Exception as e:
    partition = '无'
    sub_partition = '无'

info = '[   💻   ]:直播间：%s  当前%s  主播：%s  分区：%s-%s\r' % (
    title, display_long, nickname, partition, sub_partition)
print(info)

flv = []
print('[   🎦   ]:直播间清晰度')
for i, f in enumerate(flv_pull_url.keys()):
    print('[   %s   ]: %s' % (i, f))
    flv.append(f)

rate = int(input('[   🎬   ]输入数字选择推流清晰度：'))

# ld = 标清

# sd = 高清

# hd = 超清

# uhd = 蓝光

# or4 = 原画

# 显示清晰度列表
print('[   %s   ]:%s' % (flv[rate], flv_pull_url[flv[rate]]))

input('[   📺   ]:复制链接使用下载工具下载，按回车退出')