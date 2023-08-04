#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:NickMapper.py
@Date       :2023/07/17 16:56:50
@Author     :JohnserfSeed
@version    :0.0.1
@License    :MIT License
@Github     :https://github.com/johnserf-seed
@Mail       :johnserf-seed@foxmail.com
-------------------------------------------------
Change Log  :
2023/07/17 16:56:50 - 初始化用户昵称与作品映射
-------------------------------------------------
'''

import sqlite3

class NickMapper:
    def __init__(self, db_name: str) -> None:
        """
        初始化 NickMapper 对象

        Args:
            db_name (str): 昵称映射表的数据库名称
        """
        self.db_name = db_name
        self.conn = None

    def connect(self) -> None:
        """
        连接到数据库并创建昵称映射表
        """
        self.conn = sqlite3.connect(self.db_name)
        self._create_table()

    def _create_table(self) -> None:
        """
        在数据库中创建昵称映射表
        """
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS nickname_mapping
                        (sec_user_id TEXT PRIMARY KEY, nickname TEXT)''')

    def add_mapping(self, sec_user_id: str, nickname: str) -> None:
        """
        添加昵称映射

        Args:
            sec_user_id (str): 用户唯一标识
            nickname (str): 可变昵称
        """
        c = self.conn.cursor()

        # 检查用户 ID 是否已经存在
        c.execute('SELECT * FROM nickname_mapping WHERE sec_user_id=?', (sec_user_id,))
        result = c.fetchone()

        if result:
            # 用户 ID 已存在，更新昵称映射
            c.execute('UPDATE nickname_mapping SET nickname=? WHERE sec_user_id=?', (nickname, sec_user_id))
        else:
            # 用户 ID 不存在，插入新的昵称映射
            c.execute('INSERT INTO nickname_mapping VALUES (?, ?)', (sec_user_id, nickname))

        self.conn.commit()

    def update_mapping(self, sec_user_id: str, new_nickname: str) -> None:
        """
        更新昵称映射

        Args:
            sec_user_id (str): 用户唯一标识
            new_nickname (str): 新的可变昵称
        """
        c = self.conn.cursor()

        # 检查用户 ID 是否已经存在
        c.execute('SELECT * FROM nickname_mapping WHERE sec_user_id=?', (sec_user_id,))
        result = c.fetchone()

        if result:
            # 用户 ID 存在，更新昵称映射
            c.execute('UPDATE nickname_mapping SET nickname=? WHERE sec_user_id=?', (new_nickname, sec_user_id))
        else:
            # 用户 ID 不存在，可抛出异常
            raise ValueError(f"User ID '{sec_user_id}' does not exist in the nickname mapping table.")

        self.conn.commit()

    def get_nickname(self, sec_user_id: str) -> str:
        """
        获取昵称映射

        Args:
            sec_user_id (str): 用户唯一标识

        Returns:
            str: 对应的可变昵称，如果不存在则返回 None
        """
        c = self.conn.cursor()
        c.execute('SELECT nickname FROM nickname_mapping WHERE sec_user_id=?', (sec_user_id,))
        result = c.fetchone()
        return result[0] if result else None

    def delete_mapping(self, sec_user_id: str) -> None:
        """
        删除昵称映射

        Args:
            sec_user_id (str): 用户唯一标识
        """
        c = self.conn.cursor()
        c.execute('DELETE FROM nickname_mapping WHERE sec_user_id=?', (sec_user_id,))
        self.conn.commit()

    def close(self) -> None:
        """
        关闭与数据库的连接
        """
        if self.conn:
            self.conn.close()
