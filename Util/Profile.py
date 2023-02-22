#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:Profile.py
@Date       :2022/08/11 23:13:22
@Author     :JohnserfSeed
@version    :1.0
@License    :(C)Copyright 2019-2022, Liugroup-NLPR-CASIA
@Github     :https://github.com/johnserf-seed
@Mail       :johnserfseed@gmail.com
-------------------------------------------------
Change Log  :
2022/08/11 23:13:22 : Init
-------------------------------------------------
'''

import Util

############ apis############
# /aweme/v1/web/aweme/detail/       'aweme_detail'
# /aweme/v1/web/aweme/post/         'aweme_list'
###########################


class Profile():

    def __init__(self):
        # 抓获所有视频
        self.Isend = False
        # 第一次访问页码
        self.max_cursor = 0
        # 全局IOS头部
        self.headers = Util.headers
        # 系统分隔符
        self.sprit = Util.sprit
        # 输出日志
        Util.log.info(Util.platform.system())
        # 接口
        self.urls = Util.Urls()

    def getProfile(self, param):
        """判断个人主页api链接

        Args:
            param (tuple): uid,music,mode | ('https://v.douyin.com/efrHYf2/', 'no', 'post')

        Returns:
            None
        """
        self.music = param[1]
        self.mode = param[2]
        try:
            r = Util.requests.post(url=Util.reFind(param[0])[0])
        except:
            print('[  提示  ]:请检查你的配置链接填写是否正确!\r')
            input('[  提示  ]：按任意键退出程序!\r')
            exit()

        print('[  提示  ]:批量获取所有视频中!\r')
        Util.log.info('[  提示  ]:批量获取所有视频中!')

        # 获取用户sec_uid
        # 2022/08/24: 直接采用request里的path_url，用user\/([\d\D]*)([?])过滤出sec
        if '?' in r.request.path_url:
            for id in Util.re.finditer(r'user\/([\d\D]*)([?])', str(r.request.path_url)):
                self.sec = id.group(1)
        else:
            for id in Util.re.finditer(r'user\/([\d\D]*)', str(r.request.path_url)):
                self.sec = id.group(1)
        print('[  提示  ]:用户的sec_id=%s\r' % self.sec)
        Util.log.info('[  提示  ]:用户的sec_id=%s' % self.sec)

        # 用户主页
        self.homepage = "https://www.douyin.com/user/" + self.sec

        # 旧接口于22/12/23失效
        # post_url = 'https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid=%s&count=35&max_cursor=0&aid=1128&_signature=PDHVOQAAXMfFyj02QEpGaDwx1S&dytk=' % (
        #     self.sec)
        # 23/02/09
        # 获取xg参数
        # datas 为元组 (params, xb)
        datas = Util.XBogus('sec_user_id=%s&count=35&max_cursor=0&aid=1128&version_name=23.5.0&device_platform=android&os_version=2333' % (
            self.sec))
        response = Util.requests.get(
            url=self.urls.USER_POST + datas.params, headers=self.headers, timeout=3)

        if response.text == '':
            input('[  提示  ]:获取用户数据失败，请从web端获取新ttwid\r')
            exit()

        post_name_json = Util.json.loads(response.content.decode())
        # 2022/09/05
        # 因为抖音页面分离技术，最初获取的网页信息没有经过js渲染，无法获取like模式下的用户名，故均用post模式获取用户名
        try:
            self.nickname = post_name_json['aweme_list'][0]['author']['nickname']
            self.nickname = Util.replaceT(self.nickname)
            # self.nickname = Util.etree.HTML(r.text).xpath('//*[@id="douyin-right-container"]/div[2]/div/div/div[1]/div[2]/div[1]/h1/span/span/span/span/span/span/text()')[0]
            # self.nickname = html['aweme_list'][0]['author']['nickname']
        except Exception as e:
            # 2022/10/19
            # like模式需要保存该账户昵称的文件夹下，如果是空作品则最少需要发布一条作品方可获取该账户昵称
            print('[  提示  ]：获取用户昵称失败! 请检查是否发布过作品，发布后请重新运行本程序！\r')
            # 输出日志
            Util.log.error('[  提示  ]：获取用户昵称失败! 请检查是否发布过作品，发布后请重新运行本程序！')
            Util.log.error(e)
            # ERROR: list index out of range
            # {'status_code': 0, 'aweme_list': [], 'max_cursor': 0, 'min_cursor': xxx, 'extra': {'now': xxx, 'logid': 'xxx'}, 'has_more': False}
            input('[  提示  ]：按任意键退出程序!\r')
            exit()

        # 构造第一次访问链接
        datas = Util.XBogus('sec_user_id=%s&count=35&max_cursor=0&aid=1128&version_name=23.5.0&device_platform=android&os_version=2333' % (
            self.sec))
        if self.mode == 'post':
            self.api_post_url = self.urls.USER_POST + datas.params
        else:
            self.api_post_url = self.urls.USER_FAVORITE_A + datas.params

        # 创建用户文件夹
        self.path = "." + self.sprit + "Download" + self.sprit + \
            param[2] + self.sprit + self.nickname + self.sprit
        if not Util.os.path.exists(self.path):
            Util.os.makedirs(self.path)

        # 保存用户主页地址
        self.s_homepage()
        # 获取用户数据
        self.getData(self.api_post_url)
        return  # self.api_post_url,self.max_cursor,self.sec

    def getData(self, api_post_url):
        """获取第一次api数据

        Args:
            api_post_url (str): 传入api链接

        Returns:
            result: api数据
        """
        # 尝试次数
        times = 0
        # 存储api数据
        result = []
        while result == []:
            times += 1
            print('[  提示  ]:正在进行第 %d 次尝试\r' % times)
            # 输出日志
            Util.log.info('[  提示  ]:正在进行第 %d 次尝试' % times)
            Util.time.sleep(0.5)
            response = Util.requests.get(
                url=api_post_url, headers=self.headers)
            # 接口不稳定，有时会返回空数据
            while response.text == '':
                print('[  提示  ]:获取作品数据失败，正在重新获取\r')
                response = Util.requests.get(
                    url=api_post_url, headers=self.headers)
            html = Util.json.loads(response.content.decode())
            if self.Isend == False:
                # 下一页值
                print('[  用户  ]:%s\r' % str(self.nickname))
                # 输出日志
                Util.log.info('[  用户  ]:%s\r' % str(self.nickname))

                try:
                    self.max_cursor = html['max_cursor']
                except:
                    input('[  提示  ]:该用户未开放喜欢页，请开放后重新运行!\r')
                    Util.log.info('[  提示  ]:该用户未开放喜欢页，请开放后重新运行!\r')
                    exit(0)

                result = html['aweme_list']
                print('[  提示  ]:抓获用户主页数据成功!\r')

                # 输出日志
                Util.log.info('[  提示  ]:抓获用户主页数据成功!')

                # 处理第一页视频信息
                self.getVideoInfo(result)
            else:
                self.max_cursor = html['max_cursor']
                self.getNextData()
                # self.Isend = True
                # 输出日志
                Util.log.info('[  提示  ]:此页无数据，为您跳过......')
                print('[  提示  ]:此页无数据，为您跳过......\r')
        return result

    def getNextData(self):
        """获取下一页api数据
        """
        datas = Util.XBogus('sec_user_id=%s&count=35&max_cursor=%s&aid=1128&version_name=23.5.0&device_platform=android&os_version=2333' % (
            self.sec, self.max_cursor))
        # 构造下一次访问链接
        if self.mode == 'post':
            api_naxt_post_url = self.urls.USER_POST + datas.params
        else:
            api_naxt_post_url = self.urls.USER_FAVORITE_A + datas.params

        index = 0
        result = []

        while self.Isend == False:
            # 回到首页，则结束
            if self.max_cursor == 0:
                self.Isend = True
                return
            index += 1
            print('[  提示  ]:正在对', self.max_cursor, '页进行第 %d 次尝试！\r' % index)
            # 输出日志
            Util.log.info('[  提示  ]:正在对 %s 页进行第 %d 次尝试！' %
                            (self.max_cursor, index))
            Util.time.sleep(0.5)
            response = Util.requests.get(
                url=api_naxt_post_url, headers=self.headers)
            # 接口不稳定，有时会返回空数据
            while response.text == '':
                print('[  提示  ]:获取作品数据失败，正在重新获取\r')
                response = Util.requests.get(
                    url=api_naxt_post_url, headers=self.headers)
            html = Util.json.loads(response.content.decode())
            if self.Isend == False:
                # 下一页值
                self.max_cursor = html['max_cursor']
                result = html['aweme_list']
                # 输出日志
                Util.log.info('[  提示  ]:第 %d 页抓获数据成功!' % self.max_cursor)
                print('[  提示  ]:第 %d 页抓获数据成功!\r' % self.max_cursor)
                # 处理下一页视频信息
                self.getVideoInfo(result)
            else:
                self.Isend == True
                # 输出日志
                Util.log.info('[  提示  ]:%d页抓获数据失败!' % self.max_cursor)
                print('[  提示  ]:%d页抓获数据失败!\r' % self.max_cursor)

    def getVideoInfo(self, result):
        """获取视频信息
        """
        # 作者信息
        self.author_list = []
        # 无水印视频链接
        # self.video_list = []
        # 作品id
        self.aweme_id = []
        # 唯一视频标识
        self.uri_list = []
        # 图集
        self.image_list = []
        # 封面大图
        # self.dynamic_cover = []
        for v in range(len(result)):
            try:
                # url_list < 4 说明是图集
                # 2022/11/27 aweme_type是作品类型 2：图集 4：视频
                # 2023/01/19 aweme_type是作品类型 68：图集 0：视频
                if result[v]['aweme_type'] == 68:
                    # if len(result[v]['video']['play_addr']['url_list']) < 4:
                    self.image_list.append(result[v]['aweme_id'])
                else:
                    self.author_list.append(str(result[v]['desc']))
                    # 2022/04/22
                    # 如果直接从 /web/api/v2/aweme/post 这个接口拿数据，那么只有720p的清晰度
                    # 如果在 /web/api/v2/aweme/iteminfo/ 这个接口拿视频uri
                    # 拼接到 aweme.snssdk.com/aweme/v1/play/?video_id=xxxx&radio=1080p 则获取到1080p清晰的
                    # self.video_list.append(
                    #     str(result[v]['video']['play_addr']['url_list'][0]))
                    self.uri_list.append(
                        str(result[v]['video']['play_addr']['uri']))
                    self.aweme_id.append(str(result[v]['aweme_id']))
                    # nickname.append(str(result[v]['author']['nickname']))
                    # self.dynamic_cover.append(str(result[v]['video']['dynamic_cover']['url_list'][0]))
            except Exception as e:
                # 输出日志
                Util.log.info('%s,因为每次不一定完全返回35条数据！' % (e))
                print('[  🚩  ]:%s,因为每次不一定完全返回35条数据！' % (e))
                break
        if self.max_cursor == 0:
            return
        # 过滤视频文案和作者名中的非法字符
        print('[  提示  ]:正在替换当页所有作品非法字符，耐心等待!\r')
        self.author_list = Util.replaceT(self.author_list)
        # 输出日志
        Util.log.info('[  提示  ]:正在替换当页所有作品非法字符，耐心等待!')

        print('[  提示  ]:正在替换作者非法字符，耐心等待!\r')
        self.nickname = Util.replaceT(self.nickname)
        # 输出日志
        Util.log.info('[  提示  ]:正在替换作者非法字符，耐心等待!')
        # 下载主页所有图集
        datas = Util.Images().get_all_images(self.image_list)
        Util.Download().VideoDownload(self)
        Util.Download().ImageDownload(datas)
        self.getNextData()
        return  # self,author_list,video_list,uri_list,aweme_id,nickname,max_cursor

    def s_homepage(self):
        with open(self.path + self.sprit + self.nickname + '.txt', 'w') as f:
            f.write(self.homepage)


if __name__ == '__main__':
    Profile()
