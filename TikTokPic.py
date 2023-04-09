#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:下载无水印图集
@Date       :2022/04/23 21:01:22
@Author     :JohnserfSeed
@version    :1.0.0
@License    :(C)Copyright 2019-2022, Liugroup-NLPR-CASIA
@Github     :https://github.com/johnserf-seed
@Mail       :johnserfseed@gmail.com
'''
import os
import re
import sys
import json
import time
import Util
import getopt
import random
import requests

from Util.XB import XBogus
from Util.Urls import Urls

def printUsage():
    print('''
                                                    TikTokPic V1.0.0
            使用说明：
                    1、本程序目前仅支持命令行调用，只能用于图集下载
                    2、命令行操作方法：
                            1）将本程序路径添加到环境变量
                            2）控制台输入 TikTokPic -u https://v.douyin.com/Fdf4RWq/
                                -u < url 抖音复制的链接:https://v.douyin.com/Fdf4RWq/ >
                                -h < 帮助说明 >

                    3、如有您有任何bug或者意见反馈请在 https://github.com/Johnserf-Seed/TikTokDownload/issues 发起
                    4、GUI预览版本现已发布，操作更简单 https://github.com/Johnserf-Seed/TikTokDownload/tags 下载
                    5、批量下载用户主页图集已在TikTokTool中适配

            注意：  目前已经支持app内分享短链和web端长链识别。
    ''')


def out_Print():
    print(r'''
████████╗     ██╗     ██╗  ██╗      ████████╗       ██████╗       ██╗  ██╗       ██████╗       ██╗       ██████╗
╚══██╔══╝     ██║     ██║ ██╔╝      ╚══██╔══╝      ██╔═══██╗      ██║ ██╔╝       ██╔══██╗      ██║      ██╔════╝
   ██║        ██║     █████╔╝          ██║         ██║   ██║      █████╔╝        ██████╔╝      ██║      ██║
   ██║        ██║     ██╔═██╗          ██║         ██║   ██║      ██╔═██╗        ██╔═══╝       ██║      ██║
   ██║        ██║     ██║  ██╗         ██║         ╚██████╔╝      ██║  ██╗       ██║           ██║      ╚██████╗
   ╚═╝        ╚═╝     ╚═╝  ╚═╝         ╚═╝          ╚═════╝       ╚═╝  ╚═╝       ╚═╝           ╚═╝       ╚═════╝''')

    # TikTokPic.exe --url=<抖音复制的链接> --music=<是否下载音频,默认为yes可选no>


def Find(string):
    # findall() 查找匹配正则表达式的字符串
    return re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)


def get_args():
    urlarg = ""
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hu:m:", ["url=", "music="])
    except getopt.GetoptError:
        printUsage()
        sys.exit(0)

    try:
        if opts == []:
            printUsage()
            urlarg = str(input("[  提示  ]:请输入图集链接:"))
            return urlarg
    except:
        pass

    for opt, arg in opts:
        if opt == '-h':
            printUsage()
            sys.exit(0)
        elif opt in ("-u", "--url"):
            urlarg = arg

    return urlarg

def replaceT(obj):
    """替换文案非法字符

    Args:
        obj (_type_): 传入对象

    Returns:
        new: 处理后的内容
    """
    if len(obj) > 80:
        obj = obj[:80]
    # '/ \ : * ? " < > |'
    reSub = r"[^\u4e00-\u9fa5^a-z^A-Z^0-9^#]"  # '/ \ : * ? " < > |'
    new = []
    if type(obj) == list:
        for i in obj:
            # 替换为下划线
            retest = re.sub(reSub, "_", i)
            new.append(retest)
    elif type(obj) == str:
        # new = eval(repr(obj).replace('\\', '_').replace('/','_').replace(':','_').replace('*','_').replace('?','_').replace('<','_').replace('>','_').replace('|','_').replace('"','_'))
        # 替换为下划线
        new = re.sub(reSub, "_", obj, 0, re.MULTILINE)
    return new

def now2ticks(type):
    """
    @description  : 获取当前时间戳
    ---------
    @param  : type，返回值类型
    -------
    @Returns  : 1650721580 || '1650721580'
    -------
    """
    if type == 'int':
        return int(round(time.time() * 1000))
    elif type == 'str':
        return str(int(round(time.time() * 1000)))

# 下载图集
def pic_download(urlarg, headers):
    try:
        r = requests.get(url=Find(urlarg)[0])
    # 如果输入链接不正确，则重新输入
    except Exception as error:
        print('[  警告  ]:输入链接有误！\r')
        urlarg = get_args()
        while urlarg == '':
            print('[  提示  ]:请重新输入图集链接!\r')
            urlarg = get_args()
        pic_download(urlarg)

    # 2022/05/31 抖音把图集更新为note
    # 2023/01/14 第一步解析出来的链接是share/video/{id}
    key = re.findall('note/(\d+)?', str(r.url))[0]


    # 官方接口
    # 旧接口22/12/23失效
    # jx_url = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={self.aweme_id[i]}'
    # 23/01/11
    # 此ies domian暂时不需要xg参数
    # 单作品接口 'aweme_detail'
    # 主页作品 'aweme_list'
    jx_url = Urls().POST_DETAIL + XBogus(
        f'aweme_id={key}&aid=1128&version_name=23.5.0&device_platform=android&os_version=2333').params

    js = json.loads(requests.get(
        url=jx_url, headers=headers).text)

    if js == '':
        input('[  提示  ]:获取图集数据失败，请从web端获取新ttwid填入配置文件\r')
        exit()

    try:
        creat_time = time.strftime("%Y-%m-%d %H.%M.%S", time.localtime(js['aweme_detail']['create_time']))

        pic_title = str(js['aweme_detail']['desc'])
        nickname = replaceT(str(js['aweme_detail']['author']['nickname']))
        # 检测下载目录是否存在
        if not os.path.exists('Download\\' + 'pic\\' + nickname + '\\' + creat_time + pic_title):
            os.makedirs('Download\\' + 'pic\\' + nickname + '\\' + creat_time + pic_title)
        with Util.progress:
            with Util.ThreadPoolExecutor(max_workers=10) as pool:
                for i in range(len(js['aweme_detail']['images'])):
                    # 尝试下载图片
                    try:
                        pic_url = str(js['aweme_detail']['images'][i]['url_list'][0])
                        p_url = 'Download\\' + 'pic\\' + nickname + '\\' + creat_time + \
                            pic_title + '\\' + pic_title + '_' + str(i) + '.jpeg'  # + now2ticks()
                        if len(pic_title) > 20:
                            filename = creat_time[:10] + pic_title[:20] + "..."
                        else:
                            filename = creat_time[:10] + pic_title
                        task_id = Util.progress.add_task(
                            "[  图集  ]:", filename=filename, start=False)
                        pool.submit(Util.copy_url, task_id,
                                    pic_url, pic_title, p_url)
                    except Exception as picError:
                        print('[  错误  ]:' + picError + '\r')
                        print('[  提示  ]:发生了点意外！\r')
                        break
    except Exception as error:
        print('[  错误  ]:' + error + '\r')
        print('[  提示  ]:获取图集失败\r')
        return


if __name__ == "__main__":
    # 设置控制台大小
    # os.system("mode con cols=120 lines=25")
    # 输出logo
    out_Print()
    # 获取命令行
    urlarg = get_args()
    # 内容为空则重新输入
    while urlarg == '':
        print('[  提示  ]:请重新输入图集链接!\r')
        urlarg = get_args()
    # 获取命令行参数
    cmd = Util.Command()
    # 获取headers
    headers = Util.Cookies(cmd.setting()).dyheaders
    # 调用下载
    pic_download(urlarg, headers)
