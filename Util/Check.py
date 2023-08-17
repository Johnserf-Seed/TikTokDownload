#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:Check.py
@Date       :2022/08/16 18:34:27
@Author     :JohnserfSeed
@version    :1.0
@License    :MIT License
@Github     :https://github.com/johnserf-seed
@Mail       :johnserfseed@gmail.com
-------------------------------------------------
Change Log  :
2022/08/16 18:34:27 : Init
-------------------------------------------------
'''

import Util

class Check():


    # 检测视频是否已经下载过
    def file_exists(self, save_dir: str, file_name: str, file_type: str) -> bool:
        """
        检测文件是否已经存在

        Args:
            save_dir (str): 保存的目录，应为绝对路径
            file_name (str): 文件名
            file_type (str): 文件类型

        Return:
            bool: 如果文件存在则返回True，否则返回False
        """
        try:
            # 验证输入
            if not all(isinstance(i, str) for i in [save_dir, file_name, file_type]):
                Util.progress.console.print("[  提示  ]: 所有参数必须是字符串。")
                return False, None

            # 使用os.path.join()来进行路径拼接
            full_path = Util.os.path.join(save_dir, file_name) + file_type
            # 检查文件是否存在
            return Util.os.path.isfile(full_path), full_path

        except Exception as e:
            Util.progress.console.print(f"[  异常  ]: {e}")
            return False, None