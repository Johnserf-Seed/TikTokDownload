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
-------------------------------------------------
'''

import Util

class Command:

    def __init__(self):
        # 打印logo
        self.showLogo()
        self.showNote()
        # 初始化配置文件
        self.cfgs = Util.Config()
        # 检查配置文件是否存在
        self.cfg = self.cfgs.check()

    def showLogo(self):
        print('''
  ████████╗██╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗
  ╚══██╔══╝██║██║ ██╔╝╚══██╔══╝██╔═══██╗██║ ██╔╝██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗
     ██║   ██║█████╔╝    ██║   ██║   ██║█████╔╝ ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║
     ██║   ██║██╔═██╗    ██║   ██║   ██║██╔═██╗ ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║
     ██║   ██║██║  ██╗   ██║   ╚██████╔╝██║  ██╗██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝
     ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝
     ''')

    def showNote(self):
        print("#" * 120)
        print(
            """
                                                TikTokDownload V1.3.0
        使用说明：
                1、本程序目前支持命令行调用和配置文件操作，GUI预览版本已经发布
                2、命令行操作方法：1）将本程序路径添加到环境变量
                                2）控制台输入 TikTokMulti -u https://v.douyin.com/jqwLHjF/

                3、配置文件操作方法：1）运行软件前先打开目录下 conf.ini 文件配置用户主页和音乐下载模式
                                2）按照控制台输出信息操作

                4、如有您有任何bug或者意见反馈请在 https://github.com/Johnserf-Seed/TikTokDownload/issues 发起
                5、GUI预览版本现已发布，操作更简单 https://github.com/Johnserf-Seed/TikTokDownload/tags 下载

        注意：  目前已经支持app内分享短链和web端长链识别。
    """
        )
        print("#" * 120)
        print('\r')

    def argument(self):
        """获取命令行参数

        Returns:
            args: 返回命令行对象
        """
        parser = Util.argparse.ArgumentParser(
            description='TikTokMulti V1.2.5 使用帮助')
        parser.add_argument('--uid', '-u', type=str,
                            help='为用户主页链接，非必要参数', required=False)
        # parser.add_argument('--dir','-d', type=str,help='视频保存目录，非必要参数， 默认./Download', default='./Download/')
        # parser.add_argument('--single', '-s', type=str, help='单条视频链接，非必要参数，与--user参数冲突')
        parser.add_argument('--music', '-m', type=str,
                            help='视频音乐下载，非必要参数， 默认no可选yes', default='no')
        # parser.add_argument('--count', '-c', type=int, help='单页下载的数量，默认参数 35 无须修改', default=35)
        parser.add_argument('--mode', '-M', type=str,
                            help='下载模式选择，默认post:发布的视频 可选like:点赞视频(需要开放权限)', default='post')
        args = parser.parse_args()
        return args

    def setting(self):
        """设置配置

        Returns:
            list: 返回uid,music,mode
        """
        args = self.argument()
        if args.uid == None:
            print('[  警告  ]:未检测到命令，将使用配置文件进行批量下载!')
            self.uid = self.cfg.get('uid', 'uid')
            self.music = self.cfg.get('music', 'music')
            self.mode = self.cfg.get('mode', 'mode')
            print('[  提示  ]:读取本地配置完成!\r')
        else:
            self.uid = args.uid
            self.music = args.music
            self.mode = args.mode
            print('[  提示  ]:读取命令完成!\r')
        return [self.uid, self.music, self.mode]


if __name__ == '__main__':
    Command()
