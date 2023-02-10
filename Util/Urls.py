#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:Urls.py
@Date       :2023/02/08 18:14:47
@Author     :JohnserfSeed
@version    :0.0.1
@License    :MIT License
@Github     :https://github.com/johnserf-seed
@Mail       :johnserf-seed@foxmail.com
-------------------------------------------------
Change Log  :
2023/02/08 18:14:47 - Create Urls from https://langyue.cc/APIdocV1.0.html
-------------------------------------------------
'''

import Util


class Urls:
    def __init__(self):
        ######################################### WEB #########################################
        # 首页推荐
        self.TAB_FEED = 'https://www.douyin.com/aweme/v1/web/tab/feed/?'

        # 用户短信息（给多少个用户secid就返回多少的用户信息）
        self.USER_SHORT_INFO = 'https://www.douyin.com/aweme/v1/web/im/user/info/?'

        # 用户详细信息
        self.USER_DETAIL = 'https://www.douyin.com/aweme/v1/web/user/profile/other/?'

        # 用户作品
        self.USER_POST = 'https://www.douyin.com/aweme/v1/web/aweme/post/?'

        # 作品信息
        self.POST_DETAIL = 'https://www.douyin.com/aweme/v1/web/aweme/detail/?'

        # 用户喜欢A
        self.USER_FAVORITE_A = 'https://www.douyin.com/aweme/v1/web/aweme/favorite/?'

        # 用户喜欢B
        self.USER_FAVORITE_B = 'https://www.iesdouyin.com/web/api/v2/aweme/like/?'

        # 用户历史
        self.USER_HISTORY = 'https://www.douyin.com/aweme/v1/web/history/read/?'

        # 用户收藏
        self.USER_COLLECTION = 'https://www.douyin.com/aweme/v1/web/aweme/listcollection/?'

        # 用户评论
        self.COMMENT = 'https://www.douyin.com/aweme/v1/web/comment/list/?'

        # 首页朋友作品
        self.FRIEND_FEED = 'https://www.douyin.com/aweme/v1/web/familiar/feed/?'

        # 关注用户作品
        self.FOLLOW_FEED = 'https://www.douyin.com/aweme/v1/web/follow/feed/?'

        # X-Bogus Path
        self.GET_XB_PATH = 'http://47.115.200.238/xg/path?url='

        # X-Bogus Dict
        self.GET_XB_DICT = 'http://47.115.200.238/xg/dict/?params='

        # X-Bogus Login
        self.GET_XB_LOGIN = 'http://47.115.200.238/login'

        # X-Bogus Register
        self.GET_XB_REGISTER = 'http://47.115.200.238/register'

        # X-Bogus Token
        self.GET_XB_TOKEN = 'http://47.115.200.238/token'
        #######################################################################################

        ######################################### APP #########################################
        # X-Gorgon Path
        self.GET_XG_LOGIN = 'http://47.115.200.238/xog/path?url='

        #######################################################################################

if __name__ == '__main__':
    Urls()
