#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:懒得优化这一块
@Date       :2020/12/28 13:14:29
@Author     :JohnserfSeed
@version    :1.0
@License    :(C)Copyright 2017-2020, Liugroup-NLPR-CASIA
@Mail       :johnserfseed@gmail.com
'''

import re
import sys
import json
import Util
import getopt
import requests

# from retrying import retry


def printUsage():
    print('''
        使用方法: 1、添加为环境变量 2、输入命令
        -u<url 抖音复制的链接:https://v.douyin.com/JtcjTwo/>
        -m<music 是否下载音频,默认为yes可选no>
        -n<name 用于自定义视频文件名，默认不设置>

        例如：TikTokDownload.exe -u https://v.douyin.com/JtcjTwo/ -m yes -n 下载1

    ''')
# TikTokDownLoad.exe --url=<抖音复制的链接> --music=<是否下载音频,默认为yes可选no> --name=<用于自定义视频文件名，默认不设置>


def Find(string):
    # findall() 查找匹配正则表达式的字符串
    url = re.findall(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
    return url


def main():
    url = ""
    music = "yes"
    name = ""
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:u:m:n:", [
                                    "url=", "music=", "name="])
    except getopt.GetoptError:
        printUsage()
        sys.exit(-1)
    try:
        if opts == []:
            printUsage()
            url = str(input("请输入抖音链接:"))
            return url, music, name
    except:
        pass
    for opt, arg in opts:
        if opt == '-h':
            printUsage()
            sys.exit(-1)
        elif opt in ("-u", "--url"):
            url = arg
        elif opt in ("-m", "--music"):
            music = arg
        elif opt in ("-n", "--name"):
            name = arg
    return url, music, name


# @retry(stop_max_attempt_number=3)
def download(video_url, music_url, video_title, music_title, headers, music, name):
    # 视频下载
    if video_url == '':
        print('[  提示  ]:该视频可能无法下载哦~\r')
        return
    else:
        r = requests.get(url=video_url, headers=headers)
        if not Util.Status_Code(r.status_code):
            if video_title == '':
                video_title = '[  提示  ]:此视频没有文案_%s\r' % music_title
            video_title = Util.replaceT(video_title)
            music_title = Util.replaceT(music_title)
            if name == "":
                name = video_title
            with open(f'{name}.mp4', 'wb') as f:
                f.write(r.content)
                print('[  视频  ]:%s.mp4 下载完成\r' % name)

    if music_url == '':
        print('[  提示  ]:下载出错\r')
        # return
    else:
        # 原声下载
        if music != 'yes':
            print('[  提示  ]:不下载%s视频原声\r' % video_title)
            # return
        else:
            r = requests.get(url=music_url, headers=headers)
            with open(f'{music_title}.mp3', 'wb') as f:
                f.write(r.content)
                print('[  音频  ]:%s.mp3 下载完成\r' % music_title)
            # return


def video_download(url, music, name):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'referer':'https://www.douyin.com/',
        'Cookie': 'msToken=%s;odin_tt=324fb4ea4a89c0c05827e18a1ed9cf9bf8a17f7705fcc793fec935b637867e2a5a9b8168c885554d029919117a18ba69;' % Util.generate_random_str(107)
    }
    r = requests.get(url=Find(url)[0])
    key = re.findall('video/(\d+)?', str(r.url))[0]
    # 官方接口
    # 旧接口22/12/23失效
    # jx_url = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={self.aweme_id[i]}'
    # 23/01/11
    # 此ies domian暂时不需要xg参数
    # 单作品接口 'aweme_detail'
    # 主页作品 'aweme_list'
    jx_url = Util.Urls().POST_DETAIL + Util.XBogus(
        f'aweme_id={key}&aid=1128&version_name=23.5.0&device_platform=android&os_version=2333').params

    js = Util.json.loads(Util.requests.get(
        url=jx_url, headers=headers).text)

    try:
        video_url = str(js['aweme_detail']['video']['play_addr']
                        ['url_list'][2])  # .replace('playwm', 'play')  # 去水印后链接
    except:
        print('[  提示  ]:视频链接获取失败\r')
        video_url = ''
    try:
        music_url = str(js['aweme_detail']['music']['play_url']['url_list'][0])
    except:
        print('[  提示  ]:该音频目前不可用\r')
        music_url = ''
    try:
        video_title = str(js['aweme_detail']['desc'])
        music_title = str(js['aweme_detail']['music']['author']) + '创作的视频原声'
    except:
        print('[  提示  ]:标题获取失败\r')
        video_title = '视频走丢啦~'
        music_title = '音频走丢啦~'
    download(video_url, music_url, video_title,
                music_title, headers, music, name)


if __name__ == "__main__":
    url, music, name = main()
    video_download(url, music, name)
    input('[  提示  ]:按任意键退出')
    sys.exit()
