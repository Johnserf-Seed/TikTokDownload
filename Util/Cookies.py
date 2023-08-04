#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:Cookies.py
@Date       :2023/07/29 20:13:24
@Author     :JohnserfSeed
@version    :0.0.1
@License    :MIT License
@Github     :https://github.com/johnserf-seed
@Mail       :johnserf-seed@foxmail.com
-------------------------------------------------
Change Log  :
2023/07/29 20:13:24 - 添加不同类型的cookies生成
2023/08/01 15:19:38 - 对response.cookies进行拆分
-------------------------------------------------
'''

import re
import time
import random
import requests


class Cookies:

    def __init__(self) -> None:
        pass

    def generate_random_str(self, randomlength=16) -> str:
        """
        根据传入长度产生随机字符串
        param :randomlength
        return:random_str
        """
        random_str = ''
        base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789='
        length = len(base_str) - 1
        for _ in range(randomlength):
            random_str += base_str[random.randint(0, length)]
        return random_str

    def generate_ttwid(self) -> str:
        """
        生成请求必带的ttwid
        param :None
        return:ttwid
        """
        url = 'https://ttwid.bytedance.com/ttwid/union/register/'
        data = '{"region":"cn","aid":1768,"needFid":false,"service":"www.ixigua.com","migrate_info":{"ticket":"","source":"node"},"cbUrlProtocol":"https","union":true}'
        response = requests.request("POST", url, data=data)
        # j = ttwid  k = 1%7CfPx9ZM.....
        for j, k in response.cookies.items():
            return k

    def get_fp(self) -> str:
        """
        生成verifyFp

        Returns:
            str: verifyFp
        """
        e = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        t = len(e)
        milliseconds = int(round(time.time() * 1000))
        base36 = ''
        while milliseconds > 0:
            remainder = milliseconds % 36
            if remainder < 10:
                base36 = str(remainder) + base36
            else:
                base36 = chr(ord('a') + remainder - 10) + base36
            milliseconds = int(milliseconds / 36)
        r = base36
        o = [''] * 36
        o[8] = o[13] = o[18] = o[23] = '_'
        o[14] = '4'

        for i in range(36):
            if not o[i]:
                n = 0 or int(random.random() * t)
                if i == 19:
                    n = 3 & n | 8
                o[i] = e[n]
        ret = "verify_" + r + "_" + ''.join(o)
        return ret

    def get_s_v_web_id(self) -> str:
        """
        生成s_v_web_id

        Returns:
            str: s_v_web_id
        """

        e = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
        t = len(e)
        n = self.base36_encode(int(time.time()*1000))  # 生成时间戳的36进制

        r = [''] * 36
        r[8] = r[13] = r[18] = r[23] = "_"
        r[14] = "4"

        for i in range(36):
            if not r[i]:
                o = int(random.random() * t)
                r[i] = e[3 & o | 8 if i == 19 else o]

        return "verify_" + n + "_" + "".join(r)

    def base36_encode(self, number) -> str:
        """
        转换整数为base36字符串

        Returns:
            str: base36 string
        """

        alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
        base36 = []

        while number:
            number, i = divmod(number, 36)
            base36.append(alphabet[i])

        return ''.join(reversed(base36))

    def split_cookies(self, cookie_str:str) -> str:
        """
        拆分Set-Cookie字符串并拼接

        Args:
            cookie_str (str): _description_
        """

        # 判断是否为字符串
        if not isinstance(cookie_str, str):
            raise TypeError("cookie_str must be str")

        # 拆分Set-Cookie字符串,避免错误地在expires字段的值中分割字符串。
        cookies_list = re.split(', (?=[a-zA-Z])', cookie_str)

        # 拆分每个Cookie字符串，只获取第一个分段（即key=value部分）
        cookies_list = [cookie.split(';')[0] for cookie in cookies_list]

        # 拼接所有的Cookie
        cookie_str = ";".join(cookies_list)

        return cookie_str
