#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:Command.py
@Date       :2022/07/30 18:38:09
@Author     :JohnserfSeed
@version    :1.0
@License    :(C)Copyright 2019-2022, Liugroup-NLPR-CASIA
@Github     :https://github.com/johnserf-seed
@Mail       :johnserfseed@gmail.com
-------------------------------------------------
Change Log  :
2022/07/30 18:38:09 : Init
2022/08/16 18:34:27 : change to class Command
2023/03/08 15:33:45 : add more arguments
-------------------------------------------------
'''

import Util

class Command:

    def __init__(self):
        # 初始化配置文件
        self.cfgs = Util.Config()
        # 检查配置文件是否存在
        self.cfg = self.cfgs.check()

    def argument(self):
        """
        获取命令行参数
        Returns:
            args: 返回命令行对象
        """
        parser = Util.argparse.ArgumentParser(
            description='TikTokTool V1.3.0.70 使用帮助')
        parser.add_argument('--uid', '-u', type=str,
                            help='为用户主页链接，支持长短链', required=False)
        # parser.add_argument('--dir','-d', type=str,help='视频保存目录，非必要参数， 默认./Download', default='./Download/')
        # parser.add_argument('--single', '-s', type=str, help='单条视频链接，非必要参数，与--user参数冲突')
        parser.add_argument('--music', '-m', type=str,
                            help='是否下载视频原声， 默认no 可选yes', default='no')
        # parser.add_argument('--count', '-c', type=int, help='单页下载的数量，默认参数 35 无须修改', default=35)
        parser.add_argument('--mode', '-M', type=str,
                            help='下载模式选择，默认post:发布的视频 like:点赞视频(需要开放权限) collection:收藏夹视频(需要登录账号详情看cookie帮助)', default='post')
        parser.add_argument('--cookie', '-cookie', type=str,
                            help='请求接口需要cookie，个性化推荐内容填入sessionid_ss，其他填入odin_tt、passport_csrf_token', default='')
        parser.add_argument('--interval', '-I', type=str,
                            help='根据作品发布日期区间下载作品，例如2022-01-01|2023-01-01下载的是2022年所有作品，0为下载全部', default='0')
        parser.add_argument('--update', '-U', type=str,
                            help='选择是否自动升级，由于更新频率快，默认yes 可选no', default='yes')
        args = parser.parse_args()
        return args

    def setting(self):
        """
        设置配置
        Returns:
            tuple: 返回uid,music,mode,cookie,interval,update
        """
        args = self.argument()
        # 检测是否为命令行调用
        if args.uid == None:
            print('[  警告  ]:未检测到命令，将使用配置文件进行批量下载!')
            self.uid = self.cfg.get('uid', 'uid')
            self.music = self.cfg.get('music', 'music')
            self.mode = self.cfg.get('mode', 'mode')
            self.cookie = self.cfg.get('cookie', 'cookie')
            self.interval = self.cfg.get('interval', 'interval')
            self.update = self.cfg.get('update', 'update')
            print('[  提示  ]:读取本地配置完成!\r')
            Util.log.info('[  提示  ]:读取本地配置完成!')
        else:
            self.uid = args.uid
            self.music = args.music
            self.mode = args.mode
            self.cookie = args.cookie
            self.interval = args.interval
            self.update = args.update
            print('[  提示  ]:读取命令完成!\r')
            Util.log.info('[  提示  ]:读取命令完成!')
        return [self.uid, self.music, self.mode, self.cookie, self.interval, self.update]


if __name__ == '__main__':
    Command()
