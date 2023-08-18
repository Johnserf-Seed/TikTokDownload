#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:Log.py
@Date       :2022/08/17 00:10:38
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

# 创建logs文件夹
cur_path = Util.os.path.abspath(
    Util.os.path.join(Util.os.path.dirname("__file__")))
log_path = Util.os.path.join(cur_path, 'logs')
# 如果不存在这个logs文件夹，就自动创建一个
if not Util.os.path.exists(log_path):
    Util.os.mkdir(log_path)


class Log(object):
    def __init__(self):
        # 文件的命名
        self.logname = Util.os.path.join(log_path, '%s.log' % Util.time.strftime(
            "%Y-%m-%d_%H%M%S", Util.time.localtime()))
        Util.logging.basicConfig()
        self.logger = Util.logging.getLogger("TikTokDownload")
        self.logger.setLevel(Util.logging.INFO)
        self.logger.propagate = False
        # 日志输出格式
        self.formatter = Util.logging.Formatter(
            '[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')

    def __console(self, level, message):
        """传入控制台日志

        Args:
            level (str): 日志等级
            message (str): 日志消息
        """
        # 创建一个FileHandler，用于写到本地
        fh = Util.logging.FileHandler(
            self.logname, 'a', encoding='utf-8')  # 这个是python3的
        fh.setLevel(Util.logging.INFO)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = Util.logging.StreamHandler()
        ch.setLevel(Util.logging.ERROR)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)
