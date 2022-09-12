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

class Profile():

    def __init__(self):
        # 抓获所有视频
        self.Isend = False
        # 第一次访问页码
        self.max_cursor = 0
        # 全局IOS头部
        self.headers = Util.headers

        self.sprit = Util.sprit

        # 输出日志
        Util.log.info(Util.platform.system())

    def reFind(self, strurl):
        """匹配分享的url地址

        Args:
            strurl (string): 带文案的分享链接

        Returns:
            result: url短链
        """
        result = Util.re.findall(
            'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', strurl)
        return result

    def getProfile(self, param):
        """判断个人主页api链接

        Args:
            param (tuple): uid,music,mode | ('https://v.douyin.com/efrHYf2/', 'no', 'post')

        Returns:
            _type_: _description_
        """
        self.music = param[1]
        self.mode = param[2]

        r = Util.requests.post(url=self.reFind(param[0])[0])

        print('[  提示  ]:为您下载多个视频!\r')

        # 输出日志
        Util.log.info('[  提示  ]:为您下载多个视频!')

        # 获取用户sec_uid
        # 2022/08/24: 直接采用request里的path_url，用user\/([\d\D]*)([?])过滤出sec
        if '?' in r.request.path_url:
            for one in Util.re.finditer(r'user\/([\d\D]*)([?])', str(r.request.path_url)):
                self.sec = one.group(1)
        else:
            for one in Util.re.finditer(r'user\/([\d\D]*)', str(r.request.path_url)):
                self.sec = one.group(1)

        print('[  提示  ]:用户的sec_id=%s\r' % self.sec)

        # 输出日志
        Util.log.info('[  提示  ]:用户的sec_id=%s' % self.sec)

        post_url = 'https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid=%s&count=35&max_cursor=0&aid=1128&_signature=PDHVOQAAXMfFyj02QEpGaDwx1S&dytk=' % (
            self.sec)
        post_name_json = Util.json.loads(Util.requests.get(url = post_url, headers=self.headers).content.decode())
        # 2022/09/05
        # 因为抖音页面分离技术，最初获取的网页信息没有经过js渲染，无法获取like模式下的用户名，故均用post模式获取用户名
        try:
            self.nickname = post_name_json['aweme_list'][0]['author']['nickname']
            # self.nickname = Util.etree.HTML(r.text).xpath('//*[@id="douyin-right-container"]/div[2]/div/div/div[1]/div[2]/div[1]/h1/span/span/span/span/span/span/text()')[0]
            # self.nickname = html['aweme_list'][0]['author']['nickname']
        except Exception as e:
            print('[  提示  ]：获取用户昵称失败! 请重新运行本程序！\r')
            # 输出日志
            Util.log.error('[  提示  ]：获取用户昵称失败! 请重新运行本程序！')
            Util.log.error(e)
            input('[  提示  ]：按任意键退出程序!\r')
            exit()

        # 构造第一次访问链接
        self.api_post_url = 'https://www.iesdouyin.com/web/api/v2/aweme/%s/?sec_uid=%s&count=%s&max_cursor=%s&aid=1128&_signature=PDHVOQAAXMfFyj02QEpGaDwx1S&dytk=' % (
            self.mode, self.sec, 35, self.max_cursor)

        # 创建用户文件夹
        self.path = "." + self.sprit + "Download" + self.sprit + \
            param[2] + self.sprit + self.nickname + self.sprit
        if not Util.os.path.exists(self.path):
            Util.os.makedirs(self.path)
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
            html = Util.json.loads(response.content.decode())
            if self.Isend == False:
                # 下一页值
                print('[  用户  ]:%s\r' % str(self.nickname))
                # 输出日志
                Util.log.info('[  用户  ]:%s\r' % str(self.nickname))

                try:
                    self.max_cursor = html['max_cursor']
                except:
                    input('[  提示  ]:该用户未开放喜欢页!\r')
                    Util.log.info('[  提示  ]:该用户未开放喜欢页!\r')
                    exit(0)

                result = html['aweme_list']
                print('[  提示  ]:抓获数据成功!\r')

                # 输出日志
                Util.log.info('[  提示  ]:抓获数据成功!')

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
        # 构造下一次访问链接
        api_naxt_post_url = 'https://www.iesdouyin.com/web/api/v2/aweme/%s/?sec_uid=%s&count=%s&max_cursor=%s&aid=1128&_signature=RuMN1wAAJu7w0.6HdIeO2EbjDc&dytk=' % (
            self.mode, self.sec, 35, self.max_cursor)

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
                if len(result[v]['video']['play_addr']['url_list']) < 4:
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
        print('[  提示  ]:等待替换文案非法字符!\r')
        self.author_list = Util.replaceT(self.author_list)
        # 输出日志
        Util.log.info('[  提示  ]:等待替换文案非法字符!')

        print('[  提示  ]:等待替换作者非法字符!\r')
        self.nickname = Util.replaceT(self.nickname)
        # 输出日志
        Util.log.info('[  提示  ]:等待替换作者非法字符!')
        # 下载主页所有图集
        datas = Util.Images().get_all_images(self.image_list)
        Util.Download().VideoDownload(self)
        Util.Download().ImageDownload(datas)
        self.getNextData()
        return  # self,author_list,video_list,uri_list,aweme_id,nickname,max_cursor

if __name__ == '__main__':
    Profile()
