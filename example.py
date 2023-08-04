#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:example.py
@Date       :2023/08/04 01:35:15
@Author     :JohnserfSeed
@version    :0.0.1
@License    :MIT License
@Github     :https://github.com/johnserf-seed
@Mail       :johnserf-seed@foxmail.com
-------------------------------------------------
Change Log  :
2023/08/04 01:35:15 - 生成测试用例
-------------------------------------------------
'''

import Util.NickMapper as NickMapper
import Util

def example_NickMapper():
    mapper = NickMapper('nickname_mapping.db')
    mapper.connect()

    # 添加昵称映射
    mapper.add_mapping('123456', 'UserA')
    mapper.add_mapping('789012', 'UserB')

    # 更新昵称映射
    mapper.update_mapping('123456', 'NewUserA')

    # 获取昵称映射
    nickname = mapper.get_nickname('123456')
    Util.console.print(nickname)  # 输出: NewUserA

    # 删除昵称映射
    mapper.delete_mapping('789012')

    mapper.close()


def exception_handling_example():
    mapper = NickMapper('nickname_mapping.db')
    mapper.connect()

    try:
        # 更新一个不存在的映射
        mapper.update_mapping('non_existent_id', 'SomeNickname')
    except ValueError as e:
        Util.console.print(f'Caught an exception: {str(e)}')

    # 尝试添加一个已经存在的映射
    mapper.add_mapping('123456', 'UserA')  # 已经存在
    Util.console.print(mapper.get_nickname('123456'))  # 应该输出 UserA，因为映射不应该被修改

    # 尝试获取一个不存在的映射
    Util.console.print(mapper.get_nickname('non_existent_id'))  # 应该输出 None

    # 尝试删除一个不存在的映射
    mapper.delete_mapping('non_existent_id')  # 应该不会抛出任何异常

    mapper.close()


# 异常处理示例
exception_handling_example()



# async def main():
#     # 测试 re_match 方法
#     async with Util.aiohttp.ClientSession() as session:
#         match = await profile.re_match(session, 'https://v.douyin.com/iJ8WnuY3/')
#         Util.console.print(f"re_match 方法返回的结果: {match.group()}")
#     # 测试 get_all_sec_user_id 方法
#     sec_user_id = await profile.get_all_sec_user_id('https://v.douyin.com/iJ8WnuY3/')
#     Util.console.print(f"get_all_sec_user_id 方法返回的结果: {sec_user_id}")
#     # 测试 get_diff_type_url 方法
#     url = await profile.get_diff_type_url(config, sec_user_id, 35, 0)
#     Util.console.print(f"get_diff_type_url 方法返回的结果: {url}")
#     # 测试 get_user_base_info 方法
#     user_info = await profile.get_user_base_info(dyheaders, sec_user_id)
#     Util.console.print(f"get_user_base_info 方法返回的结果: {user_info}")

#     # 测试 get_user_profile_info 方法
#     profile_info = await profile.get_user_profile_info(dyheaders, sec_user_id)
#     Util.console.print(f"get_user_profile_info 方法返回的结果: {profile_info}")

#     # 测试 get_request_data 方法
#     if config['mode'] == 'listcollection':
#         dyheaders['Content-Type'] = 'application/x-www-form-urlencoded'
#         aweme_list, max_cursor, has_more = await profile.get_request_data('POST', url, dyheaders , 'count=20&cursor=0')
#     else:
#         aweme_list, max_cursor, has_more = await profile.get_request_data('GET', url, dyheaders)
#     Util.console.print(f"get_request_data 方法返回的结果: {aweme_list}, {max_cursor}, {has_more}")



if __name__ == '__main__':
    # # 获取命令行和配置文件
    # cmd = Util.Command()
    # config = cmd.config_dict
    # dyheaders = cmd.dyheaders

    # # 创建 Profile 类实例
    # profile = Util.Profile(config, dyheaders)

    # # 运行测试代码
    # Util.asyncio.run(main())

    # # 昵称映射表
    # example_NickMapper()

    # 昵称映射表异常处理示例
    exception_handling_example()