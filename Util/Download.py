#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:Download.py
@Date       :2022/08/11 22:02:49
@Author     :JohnserfSeed
@version    :1.0
@License    :(C)Copyright 2019-2022, Liugroup-NLPR-CASIA
@Github     :https://github.com/johnserf-seed
@Mail       :johnserfseed@gmail.com
-------------------------------------------------
Change Log  :
2022/08/11 22:02:49 : Init
2022/08/30 00:30:09 : Add ImageDownload()
-------------------------------------------------
'''

import Util


class Download():

    def __init__(self):
        self.urls = Util.Urls()

    def VideoDownload(self, profileData):
        # 生成1080p分辨率的视频链接
        self.like_counts = 0
        self.new_video_list = []
        self.uri_url = 'https://aweme.snssdk.com/aweme/v1/play/?video_id=%s&radio=1080p&line=0'
        self.music = profileData.music
        self.headers = Util.headers
        self.mode = profileData.mode
        self.author_list = profileData.author_list
        # self.video_list = profileData.video_list
        self.uri_list = profileData.uri_list
        self.aweme_id = profileData.aweme_id
        self.nickname = profileData.nickname
        self.max_cursor = profileData.max_cursor
        self.path = profileData.path                                 # 下载路径
        self.sprit = profileData.sprit                               # 系统分隔符
        # self.v_info = profileData.v_info
        # self.size = 0                                              # 初始化已下载大小
        # self.chunk_size = 1024                                     # 每次下载的数据大小
        #self.profile = Profile()
        self.check = Util.CheckInfo()

        for i in range(len(self.author_list)):
            # 点赞视频排序
            # self.like_counts += 1
            # 获取单部视频接口信息
            try:
                # 官方接口
                # 旧接口22/12/23失效
                # jx_url = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={self.aweme_id[i]}'
                # 23/01/11
                # 此ies domian暂时不需要xg参数
                # 单作品接口 'aweme_detail'
                # 主页作品 'aweme_list'
                # 23/02/09 更新xg参数

                jx_url = Util.Urls().POST_DETAIL + Util.XBogus(
                    f'aweme_id={self.aweme_id[i]}&aid=1128&version_name=23.5.0&device_platform=android&os_version=2333').params

                js = Util.json.loads(Util.requests.get(
                    url=jx_url, headers=self.headers).text)

                creat_time = Util.time.strftime(
                    "%Y-%m-%d %H.%M.%S", Util.time.localtime(js['aweme_detail']['create_time']))
            except Exception as e:
                Util.log.warning(e)
                print('[  🚩  ]:%s\r' % e)
                Util.log.warning(
                    f'[  🚩  ]: {self.nickname} 的视频 {self.aweme_id[i]} 下载失败')
                pass

            # Code From RobotJohns https://github.com/RobotJohns
            # 移除文件名称  /r/n
            self.author_list[i] = ''.join(self.author_list[i].splitlines())
            if len(self.author_list[i]) > 182:
                print("[  提示  ]:", "文件名称太长 进行截取")
                self.author_list[i] = self.author_list[i][0:180]
                print("[  提示  ]:", "截取后的文案：{0}，长度：{1}".format(
                    self.author_list[i], len(self.author_list[i])))

            # 检查视频下载情况
            file_state = self.check.test(
                self.path, creat_time, self.author_list[i],".mp4")
            if file_state == True:
                print('[  提示  ]: %s%s [文件已存在，为您跳过]' %
                        (creat_time, self.author_list[i]), end="")
                Util.log.info('[  提示  ]:%s[文件已存在，为您跳过]' % self.author_list[i])
                # 在PyQt中无法使用flush进行消息传输
                # for _ in range(20):
                #     print(">",end = '', flush = True)
                #     Util.time.sleep(0.01)
                print('\r')
                continue
            else:
                print('\r')
                # continue

            # 尝试下载音频
            try:
                if self.music == "yes":                                 # 保留音频
                    music_url = str(js['aweme_detail']['music']
                                    ['play_url']['url_list'][0])
                    music_title = str(js['aweme_detail']['music']['author']) + '创作的视频原声'
                    music = Util.requests.get(
                        music_url)                                      # 保存音频
                    start = Util.time.time()                            # 下载开始时间
                    size = 0                                            # 初始化已下载大小
                    chunk_size = 1024                                   # 每次下载的数据大小
                    content_size = int(
                        music.headers['content-length'])                # 下载文件总大小
                    if music.status_code == 200:                        # 判断是否响应成功
                        print('[  音频  ]:' + creat_time + self.author_list[i]+'[文件 大小]:{size:.2f} MB'.format(
                            size=content_size / chunk_size / 1024))     # 开始下载，显示下载文件大小

                        m_url = self.path + self.sprit + creat_time + Util.re.sub(
                                r'[\\/:*?"<>|\r\n]+', "_", music_title) + '_' + self.author_list[i] + '.mp3'

                        with open(m_url, 'wb') as file:                 # 显示进度条
                            for data in music.iter_content(chunk_size=chunk_size):
                                file.write(data)
                                size += len(data)
                                print('\r' + '[下载进度]:%s%.2f%%' % (
                                    '>' * int(size * 50 / content_size), float(size / content_size * 100)), end=' ')

                        end = Util.time.time()                          # 下载结束时间
                        print('\n' + '[下载完成]:耗时: %.2f秒\n' % (
                            end - start))                               # 输出下载用时时间
                        Util.log.info(m_url)
                        Util.log.info('[下载完成]:耗时: %.2f秒\n' % (end - start))

            except Exception as e:
                Util.log.error(e)
                print('[  ❌  ]:%s\r' % e)
                print('\r[  警告  ]:下载音频出错!\r')
                Util.log.error('[  ❌  ]:下载音频出错!')
            # 尝试下载视频
            try:                                                        # 生成1080p视频链接
                self.new_video_list.append('https://aweme.snssdk.com/aweme/v1/play/?video_id=%s&ratio=1080p&line=0' % self.uri_list[i])
                t_video = Util.requests.get(url=self.new_video_list[0],
                                            headers=self.headers)       # 视频内容
                start = Util.time.time()                                # 下载开始时间
                size = 0                                                # 初始化已下载大小
                chunk_size = 1024                                       # 每次下载的数据大小
                content_size = int(
                    t_video.headers['content-length'])                  # 下载文件总大小
                try:
                    if t_video.status_code == 200:                      # 判断是否响应成功
                        print('[  视频  ]:' + creat_time + self.author_list[i] + '[文件 大小]:{size:.2f} MB'.format(
                            size=content_size / chunk_size / 1024))     # 开始下载，显示下载文件大小

                        v_url = self.path + self.sprit + creat_time + Util.re.sub(
                                r'[\\/:*?"<>|\r\n] + ', "_", self.author_list[i]) + '.mp4'

                        with open(v_url, 'wb') as file:                 # 显示进度条
                            for data in t_video.iter_content(chunk_size=chunk_size):
                                size += len(data)
                                print('\r' + '[下载进度]:%s%.2f%%' % (
                                    '>' * int(size * 50 / content_size), float(size / content_size * 100)), end=' ')
                            file.write(t_video.content)

                        end = Util.time.time()                          # 下载结束时间
                        print('\n' + '[下载完成]:耗时: %.2f秒\n' % (
                            end - start))                               # 输出下载用时时间
                        Util.log.info(v_url)
                        Util.log.info('[下载完成]:耗时: %.2f秒\n' % (end - start))
                        self.new_video_list = []                        # 清除每个旧的视频列表

                except Exception as e:
                    Util.log.error(e)
                    print('[  ❌  ]:%s\r' % e)
                    print('[  警告  ]:下载视频出错!')

            except Exception as e:
                Util.log.error(e)
                print('[  ❌  ]:%s\r' % e)
                print('[  提示  ]:该页视频资源没有35个,已为您跳过！\r')
                break

    def ImageDownload(self, datas):
        self.check = Util.CheckInfo()

        for i in range(len(datas)):
            self.nickname = datas[i][0]
            self.desc = Util.replaceT(datas[i][1])
            self.create_time = Util.time.strftime(
                '%Y-%m-%d %H.%M.%S', Util.time.localtime(datas[i][2]))
            self.position = datas[i][3]
            self.number = datas[i][4]
            self.images = datas[i][5]
            self.sprit = Util.sprit

            path = "Download" + self.sprit + "pic" + self.sprit + \
                self.nickname + self.sprit + self.create_time + self.desc
            # 检测下载目录是否存在
            if not Util.os.path.exists(path):
                Util.os.makedirs(path)

            for i in range(self.number):
                # 图片目录
                p_url = 'Download' + self.sprit + 'pic' + self.sprit + self.nickname + self.sprit + \
                        self.create_time + self.desc + self.sprit + \
                            self.create_time + self.desc + \
                        '_' + str(i) + '.jpeg'
                # 检查图片下载情况
                if Util.os.path.exists(p_url):
                    print('[  提示  ]: %s%s [文件已存在，为您跳过]' %
                            (self.create_time, self.create_time + self.desc + '_' + str(i) + '.jpeg'), end="")
                    Util.log.info('[  提示  ]:%s[文件已存在，为您跳过]' % self.create_time + self.desc + '_' + str(i) + '.jpeg')
                    print('\r')
                    continue
                else:
                    print('\r')
                    pass

                # 尝试下载图片
                try:
                    picture = Util.requests.get(
                        url=self.images[i], headers=Util.headers)
                    with open(p_url, 'wb') as file:
                        file.write(picture.content)
                        print('[  提示  ]: %s%s_%s.jpeg下载完毕!\r' %
                                (self.create_time, self.desc, str(i+1)))
                except Exception as error:
                    print('[  错误  ]:%s\r' % error)
                    print('[  提示  ]:发生了点意外!\r')

if __name__ == '__main__':
    Download()
