#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:TikTokUpdata.py
@Date       :2022/11/30 15:58:51
@Author     :JohnserfSeed
@version    :1.0
@License    :MIT License
@Github     :https://github.com/johnserf-seed
@Mail       :johnserfseed@gmail.com
-------------------------------------------------
Change Log  :
2022/11/30 : 通过版本文件检查是否有更新
2023/08/04 : 完成了以下更新：
    - 引入了 "update" 参数来决定是否每次进行版本更新
    - 自定义URL常量，方便修改
    - 使用 os.path.join() 代替手动拼接路径，以提高跨平台兼容性
    - 提取了进度条显示功能，简化了 zip_Download 方法
    - 优化了对用户输入的处理，改用循环重新询问，直到用户输入有效值为止
    - 使用 shutil.move() 和 shutil.rmtree() 代替 os.rename() 和 os.removedirs()，以解决部分情况下无法移动或删除文件的问题
-------------------------------------------------
'''

import os
import sys
import shutil
import zipfile
import requests

from rich.console import Console
from rich.progress import Progress

# 在文件顶部定义 URL 和其他常量，方便修改
VERSION_URL = 'https://gitee.com/johnserfseed/TikTokDownload/raw/main/version'
ZIP_DOWNLOAD_URL = 'https://ghps.cc/https://github.com/Johnserf-Seed/TikTokDownload/archive/master.zip'
VERSION_FILE_NAME = 'version'
ZIP_FILE_NAME = 'TikTokDownload-main.zip'
EXTRACT_DIR_NAME = 'TikTokDownload-main'


class Updata:
    def __init__(self, update: str) -> None:
        # 使用rich打印输出
        self.console = Console()
        # 检查更新参数
        if update.lower() != 'yes':
            self.console.print('[   🚩   ]:更新已被禁止')
            return

        # 检查版本文件是否存在
        if os.path.exists(VERSION_FILE_NAME):
            try:
                with open(VERSION_FILE_NAME, 'r') as file:
                    version_str = file.read()
                self.l_Version = int(version_str)
            except:
                self.console.print('[   🌋   ]:获取本地版本号失败!')
                self.zip_Download()  # 如果获取本地版本号失败，则直接下载新版本
                return
        else:
            self.zip_Download()  # 如果版本文件不存在，直接下载新版本
            return

        try:
            self.console.print('[   🗻   ]:获取最新版本号中!')
            self.g_Version = int(requests.get(VERSION_URL).text)
        except:
            self.console.print('[   🌋   ]:获取网络版本号失败!')
            self.g_Version = self.l_Version

        self.get_Updata()

    def get_Updata(self):
        while True:
            if self.l_Version == self.g_Version:
                self.console.print('[   🚩   ]:目前 %i 版本已是最新' % self.l_Version)
                return
            elif self.l_Version < self.g_Version:
                isUpdata = input('[   🌋   ]:当前不是最新版本,需要升级吗? (y/n) :')
                if isUpdata.lower() == 'y':
                    self.console.print('[   🚩   ]:正在为你下载 %i 版本中，升级前请确保关闭所有打开的项目文件' % self.g_Version)
                    self.zip_Download()
                    return
                elif isUpdata.lower() == 'n':
                    self.console.print('[   🚩   ]:取消升级,旧版可能会出现没有修复的bug')
                    return
                else:
                    self.console.print('[   🌋   ]:无法识别的输入，请重新输入')
            elif self.l_Version > self.g_Version:
                self.console.print('[   🚩   ]:本地版本异常，即将更新')
                self.zip_Download()
                return

    def zip_Download(self):
        try:
            response = requests.get(ZIP_DOWNLOAD_URL, stream=True)
            response.raise_for_status()  # 检查请求是否成功
            filesize = int(response.headers['content-length'])
        except requests.RequestException:
            self.console.print('[   🚧   ]:下载文件失败，请检查网络连接并重试')
            return
        except KeyError:
            self.console.print('[   🚧   ]:获取文件大小失败，请检查网络连接并重试')
            return

        with Progress() as progress:
            task = progress.add_task("[cyan][  下载  ]", total=filesize)
            with open(ZIP_FILE_NAME, 'wb') as f:
                for chunk in response.iter_content(chunk_size=512):
                    if not chunk:
                        break
                    f.write(chunk)
                    progress.update(task, advance=len(chunk))
        self.zip_Extract()

    def zip_Extract(self):
        zip_file = zipfile.ZipFile(ZIP_FILE_NAME)
        self.console.print('[  提示  ]:开始解压缩升级包')
        zip_file.extractall()
        target = os.getcwd()
        last = os.path.join(os.getcwd(), EXTRACT_DIR_NAME)
        self.move_File(last, target)

    def move_File(self, oripath, tardir):
        if not os.path.exists(oripath):
            self.console.print('[   🚩   ]:升级目录不存在,请重新运行')
            status = 0
        else:
            for i in os.listdir(oripath):
                ori_file_path = os.path.join(oripath, i)
                tar_file_path = os.path.join(tardir, i)
                try:
                    self.console.print('[  删除  ]:' + tar_file_path)
                    if os.path.isdir(tar_file_path):
                        shutil.rmtree(tar_file_path)
                    else:
                        os.remove(tar_file_path)
                except Exception as e:
                    self.console.print(f'[  异常  ]: {e}')
                self.console.print('[  移动  ]:' + ori_file_path)
                self.console.print('[  移到  ]:' + tar_file_path)
                shutil.move(ori_file_path, tar_file_path)
            self.console.print('[   🚩   ]:删除更新临时目录')
            with open('version', 'r') as file:
                self.l_Version = int(file.read())
            shutil.rmtree(oripath)
            status = 1
        return status


if __name__ == '__main__':
    # 根据需要，向 Updata 实例传入 "yes" 或 "no"
    Updata('yes')