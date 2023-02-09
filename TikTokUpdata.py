#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:TikTokUpdata.py
@Date       :2022/11/30 15:58:51
@Author     :JohnserfSeed
@version    :1.0
@License    :(C)Copyright 2019-2022, Liugroup-NLPR-CASIA
@Github     :https://github.com/johnserf-seed
@Mail       :johnserfseed@gmail.com
-------------------------------------------------
Change Log  :22/11/30 通过版本文件检查是否有更新
-------------------------------------------------
'''

import os
import sys
import shutil
import zipfile
import platform
import requests

# from retrying import retry


class Updata:
    # 防止网络问题导致获取更新版本号失败
    # 但是会重复下载
    # @retry(stop_max_attempt_number=3)
    def __init__(self) -> None:
        # 根据操作系统生成文件分隔符
        if (platform.system() == 'Windows'):
            self.sprit = '\\'
        elif (platform.system() == 'Linux'):
            self.sprit = '/'
        else:
            self.sprit = '/'

        # 本地版本
        try:
            with open('version', 'r') as file:
                self.l_Version = int(file.read())
        except:
            print('[   🌋   ]:获取本地版本号失败!')
            # 获取失败则使用网络版本-1
            self.l_Version = int(requests.get(
                'https://cdn.jsdelivr.net/gh/Johnserf-Seed/TikTokDownload@main/version').text) - 1
            # 获取失败强制升级
            # self.get_Updata()
            # 本地没有版本文件则生成当前版本的文件
            with open('version', 'w') as file:
                file.write(str(self.l_Version))

        # 仓库版本
        try:
            print('[   🗻   ]:获取最新版本号中!')
            self.g_Version = int(requests.get(
                'https://cdn.jsdelivr.net/gh/Johnserf-Seed/TikTokDownload@main/version').text)
        except:
            print('[   🌋   ]:获取网络版本号失败!')

    def get_Updata(self):
        if self.l_Version == self.g_Version:
            print('[   🚩   ]:目前 %i 版本已是最新' % self.l_Version)
            return
        elif self.l_Version < self.g_Version:
            isUpdata = input('[   🌋   ]:当前不是最新版本,需要升级吗? (y/n) :')
            if isUpdata == 'Y' or isUpdata == 'y':
                print('[   🚩   ]:正在为你下载 %i 版本中，升级前请确保关闭所有打开的项目文件' %
                        self.g_Version)
                self.zip_Download()
            if isUpdata == 'N' or isUpdata == 'n':
                print('[   🚩   ]:取消升级,旧版可能会出现没有修复的bug')
                return
            else:
                self.get_Updata()

    # @retry(stop_max_attempt_number=3)
    def zip_Download(self):
        # 删除加速下载
        url = 'https://github.com/Johnserf-Seed/TikTokDownload/archive/master.zip'
        try:
            zip = requests.get(url, stream=True)
            filesize = int(zip.headers['content-length'])
        except:
            input('[   🚧   ]:网络不太通畅，请重新运行')
            sys.exit(0)

        with open('TikTokDownload-main.zip', 'wb') as f:
            # 写入文件
            offset = 0
            for chunk in zip.iter_content(chunk_size=512):
                if not chunk:
                    break
                f.seek(offset)
                f.write(chunk)
                offset = offset + len(chunk)
                proess = offset / int(filesize) * 100
                print('\r' + '[下载进度]:%s%.2f%%' % (
                    '>' * int(offset * 50 / filesize), proess), end=' ')
        print('\r')
        # 解压缩升级包
        self.zip_Extract()

    def zip_Extract(self):
        zip_file = zipfile.ZipFile('TikTokDownload-main.zip')
        print('[  提示  ]:开始解压缩升级包')
        zip_file.extractall()
        # 目标文件夹
        target = os.getcwd()
        # 需要移动的目录
        last = os.getcwd() + self.sprit + 'TikTokDownload-main' + self.sprit
        # 移动更新文件
        self.move_File(last, target)

    def move_File(self, oripath, tardir):
        # 判断原始文件路劲是否存在
        if not os.path.exists(oripath):
            print('[   🚩   ]:升级目录不存在,请重新运行' % oripath)
            status = 0
        else:
            # 移动文件
            for i in os.listdir(oripath):
                try:
                    print('[  删除  ]:' + tardir + self.sprit + i)
                    shutil.rmtree(tardir + self.sprit + i)
                except:
                    pass
                print('[  移动  ]:' + oripath + i)
                print('[  移到  ]:' + tardir + self.sprit + i)
                shutil.move(oripath + i, tardir + self.sprit + i)
            print('[   🚩   ]:删除更新临时目录')
            # 重新读取本地版本
            with open('version', 'r') as file:
                self.l_Version = int(file.read())
            shutil.rmtree(oripath)
            status = 1
        return status


if __name__ == '__main__':
    Updata().get_Updata()
