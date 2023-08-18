#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:Command.py
@Date       :2022/07/30 18:38:09
@Author     :JohnserfSeed
@version    :1.0
@License    :MIT License
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
        # 字典类型配置文件
        self.config_dict = {}
        # 全局headers
        self.dyheaders = {
            'Cookie': '',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            'Referer':'https://www.douyin.com/'
        }
        self.setting()

    def argument(self):
        """
        获取命令行参数
        Returns:
            args: 返回命令行对象
        """
        parser = Util.argparse.ArgumentParser(
            description='TikTokTool V1.4.2.2 使用帮助')
        parser.add_argument('--uid', '-u', type=str,
                            help='为用户主页链接，支持长短链', required=False)
        parser.add_argument('--save','-s', type=str,help='视频保存目录，非必要参数， 默认Download', default='Download')
        # parser.add_argument('--single', '-s', type=str, help='单条视频链接，非必要参数，与--user参数冲突')
        parser.add_argument('--music', '-m', type=str,
                            help='是否下载视频原声， 默认no 可选yes', default='no')
        parser.add_argument('--cover', type=str,
                            help='是否下载视频封面， 默认no 可选yes', default='no')
        parser.add_argument('--desc', type=str,
                            help='是否保存视频文案， 默认no 可选yes', default='no')
        parser.add_argument('--folderize', type=str,
                            help='是否将作品保存到单独的文件夹，默认yes 可选no', default='yes')
        parser.add_argument('--mode', '-M', type=str,
                            help='下载模式选择，默认post 可选post|like|listcollection|wix', default='post')
        parser.add_argument('--naming', type=str,
                            help='作品文件命名格式，默认为{create}_{desc}', default='{create}_{desc}')
        parser.add_argument('--cookie', '-cookie', type=str,
                            help='大部分请求需要cookie，请调用扫码登录填写cookie', default='', required=False)
        parser.add_argument('--interval', '-I', type=str,
                            help='根据作品发布日期区间下载作品，例如2022-01-01|2023-01-01', default='all')
        parser.add_argument('--update', '-U', type=str,
                            help='选择是否自动升级，由于更新频率快，默认yes 可选no', default='yes')
        parser.add_argument('--limit', type=str,
                            help='仅下载多少个视频，填all即是下载全部。实际比设置多3倍', default='all')
        parser.add_argument('--max_connections', type=int,
                            help='网络请求的并发连接数，不宜设置过大', default=10)
        parser.add_argument('--max_tasks', type=int,
                            help='异步的任务数，不宜设置过大', default=10)

        return parser.parse_args()

    def setting(self):
        """
        设置配置
        Returns:
            dict: 返回字典类型配置文件
        """

        # 检查配置文件是否存在
        cfg = Util.Config().check()
        if cfg['cookie'] == '':
            # sso登录
            login = Util.Login()
            self.dyheaders = login.loginHeaders
        else:
            self.dyheaders['Cookie'] = cfg['cookie']

        # 检测是否为命令行调用
        args = self.argument()
        # 如果args中有任何非None的值则设置为命令行
        if len(Util.sys.argv) > 1:  # 如果命令行参数列表的长度大于1，说明有提供命令行参数
            args = self.argument()
            self.config_dict = vars(args)
            Util.progress.console.print('[  配置  ]:获取命令行完成!\r')
            Util.log.info('[  配置  ]:获取命令行完成!')
        else:
            self.config_dict = cfg
            Util.progress.console.print('[  配置  ]:读取本地配置完成!\r')
            Util.log.info('[  配置  ]:读取本地配置完成!')