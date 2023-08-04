#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:V1.py
@Date       :2022/07/29 23:19:14
@Author     :JohnserfSeed
@version    :1.0
@License    :MIT License
@Github     :https://github.com/johnserf-seed
@Mail       :johnserfseed@gmail.com
-------------------------------------------------
Change Log  :
2022/07/29 23:19:14 : Init
2023/03/10 16:22:19 : gen dyheaders
2023/08/04 02:09:31 : async download
-------------------------------------------------
'''

import Util

if __name__ == '__main__':
    # 获取命令行和配置文件
    cmd = Util.Command()
    config = cmd.config_dict
    dyheaders = cmd.dyheaders

    # 异步下载作品
    Util.asyncio.run(Util.Profile(config, dyheaders).get_Profile())
    input("[  提示  ]:下载完成，输入任意键退出。")