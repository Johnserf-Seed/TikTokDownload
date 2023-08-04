#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:__init__.py
@Date       :2022/07/29 23:20:56
@Author     :JohnserfSeed
@version    :1.4.0.0
@License    :MIT License
@Github     :https://github.com/johnserf-seed
@Mail       :johnserfseed@gmail.com
-------------------------------------------------
Change Log  :
2022/07/29 23:20:56 : Init
2022/08/16 18:34:27 : Add moudle Log
2023/03/10 15:27:18 : Add rich download progress
-------------------------------------------------
'''

# 标准库
import re
import io
import os
import sys
import json
import time
import math
import signal
import random
import asyncio
import logging
import platform
import argparse
import base64
from urllib import parse
from urllib.request import urlopen
from functools import partial
from typing import Union, Optional
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

# 第三方库
import aiohttp
import requests

from PIL import Image
from lxml import etree
import rich
import qrcode
from configobj import ConfigObj
from rich.progress import (
    BarColumn,
    DownloadColumn,
    Progress,
    TaskID,
    TextColumn,
    TimeRemainingColumn,
    TransferSpeedColumn,
)
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# 自定义模块
from TikTokUpdata import Updata
from .XB import XBogus
from .Log import Log
from .Urls import Urls
from .Lives import Lives
from .Login import *
from .Check import Check
from .Config import Config
from .Command import Command
from .Cookies import Cookies
from .Profile import Profile
from .Download import Download
from .NickMapper import NickMapper
from . import __version__


# 日志记录
log = Log()

def replaceT(obj):
    """
    替换文案非法字符
    Args:
        obj (_type_): 传入对象
    Returns:
        new: 处理后的内容
    """
    if len(obj) > 100:
        obj = obj[:100]
    reSub = r"[^\u4e00-\u9fa5^a-z^A-Z^0-9^#]"
    new = []
    if type(obj) == list:
        for i in obj:
            # 替换为下划线
            retest = re.sub(reSub, "_", i)
            new.append(retest)
    elif type(obj) == str:
        # 替换为下划线
        new = re.sub(reSub, "_", obj, 0, re.MULTILINE)
    return new


def reFind(strurl):
    """
    匹配分享的url地址
    Args:
        strurl (string): 带文案的分享链接
    Returns:
        result: url短链
    """
    # 空数据判断
    if strurl == '':
        return strurl
    result = re.findall(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', strurl)
    return result


table = Table.grid(padding=1, pad_edge=True)
table.add_column(no_wrap=True, justify="left")
table.add_row(__version__.__help__)


console = Console(width=150)    # 显示字符宽度
console = rich.console.Console(color_system="truecolor")    # 真彩
console.print(f"{__version__.__logo__}", justify="center")
console.print(f"\n:rocket: [bold]TikTokDownload [bright_yellow]{__version__.__version__}[/bright_yellow] :rocket:", justify="center")
console.print(f":zap: [i]{__version__.__description_cn__} :zap:", justify="center")
console.print(f":fire: [i]{__version__.__description_en__} :fire:", justify="center")
console.print(f":computer: [i]Repo {__version__.__repourl__} :computer:\n", justify="center")
console.print(Panel(table, border_style="bold", title="使用说明"))


if (platform.system() == 'Windows'):
    # 💻
    console.print('[   💻   ]:Windows平台')
elif (platform.system() == 'Linux'):
    # 🐧
    console.print('[   🐧   ]:Linux平台')
else:
    # 🍎
    console.print('[   🍎   ]:MacOS平台')


# 输出操作系统版本
log.info(platform.system())
