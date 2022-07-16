#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:TikTokMulti.py
@Date       :2022/01/29 20:23:37
@Author     :JohnserfSeed
@version    :1.2.5
@License    :(C)Copyright 2019-2022, Liugroup-NLPR-CASIA
@Github     :https://github.com/johnserf-seed
@Mail       :johnserfseed@gmail.com
@Thanks     :RobotJohns
'''

import requests, json, os, time, configparser, re, sys, argparse


class TikTok():
    # 初始化
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.66'
        }

        # 抓获所有视频
        self.Isend = False

        # 用户主页      # 保存路径      # 单页下载数        # 下载音频      # 下载模式      # 保存用户名            # 点赞个数
        self.uid = ''
        self.save = ''
        self.count = ''
        self.musicarg = ''
        self.mode = ''
        self.nickname = ''
        self.like_counts = 0

        self.sleep_sec = 0.3
        self.down_count = 0
        self.zero_count = 0
        self.max_retry_count = 10
        self.v_info = None
        self.rootpath = ''
        self.musicpath = ''
        self.videopath = ''
        self.imagepath = ''

        # 用户唯一标识
        self.sec = ''
        self.crawlmode = "1"
        self.firstsignature = "PDHVOQAAXMfFyj02QEpGaDwx1S&dytk="
        self.nextsignature = "RuMN1wAAJu7w0.6HdIeO2EbjDc&dytk="

    def setting(self, uid, music, count, savepath, mode, crawlmode, pic):
        """
        @description  : 设置命令行参数
        ---------
        @param  : uid 用户主页,music 下载音频,count 单页下载数,dir 目录,mode 模式
        -------
        @Returns  : None
        -------
        """
        if uid == None:
            print('[  警告  ]:--user不能为空')
            pass
        else:
            self.uid = uid
            self.save = savepath
            self.count = count
            self.musicarg = music
            self.picarg = pic
            self.mode = mode
            self.crawlmode = crawlmode
            self.judge_link()

    # 匹配粘贴的url地址
    def Find(self, string):
        # findall() 查找匹配正则表达式的字符串
        url = re.findall(
            'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
        return url

    def replaceT(self, obj):
        """
        @description  : 替换文案非法字符
        ---------
        @param  : ojb 传入对象
        -------
        @Returns  : n 处理后的内容
        -------
        """
        r = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
        if type(obj) == list:
            new = []
            for i in obj:
                # 替换为下划线
                retest = re.sub(r, "_", i)
                new.append(retest)
        elif type(obj) == str:
            # 替换为下划线
            new = re.sub(r, "_", obj)
        return new

    # 判断个人主页api链接
    def judge_link(self):
        self.fill_user_sec()
        # 判断长短链
        #r = requests.get(url=self.Find(self.uid)[0])
        # print('[  提示  ]:为您下载多个视频!\r')
        # 获取用户sec_uid
        #for one in re.finditer(r'user\/([\d\D]*)', str(r.url)):
        #    self.sec = one.group(1)
        # key = re.findall('/user/(.*?)\?', str(r.url))[0]
        # print('[  提示  ]:用户的sec_id=%s\r' % self.sec)
        # else:
        #    r = requests.get(url = self.Find(self.uid)[0])
        #    print('[  提示  ]:为您下载多个视频!\r')
        #    # 获取用户sec_uid
        #    # 因为某些情况链接中会有?previous_page=app_code_link参数，为了不影响key结果做二次过滤
        #    # 2022/03/02: 用户主页链接中不应该出现?previous_page,?enter_from参数
        #    # 原user/([\d\D]*?)([?])
        #    # try:
        #    #     for one in re.finditer(r'user\/([\d\D]*)([?])',str(r.url)):
        #    #         key = one.group(1)
        #    # except:
        #    for one in re.finditer(r'user\/([\d\D]*)',str(r.url)):
        #        self.sec = one.group(1)
        #    print('[  提示  ]:用户的sec_id=%s\r' % self.sec)

        # 第一次访问页码
        max_cursor = 0

        html = self.downpageinfo(max_cursor, 1);
        self.nickname = self.getnickname(html)
        self.rootpath = os.path.join(self.save, self.mode, self.nickname)
        self.musicpath = os.path.join(self.rootpath, "music")
        self.videopath = os.path.join(self.rootpath, "video")
        self.imagepath = os.path.join(self.rootpath, "image")
        self.createdefaultpath()

        self.get_data(max_cursor)
        return max_cursor, self.sec

    def createdefaultpath(self):
        self.check_path(self.rootpath)
        self.check_path(self.musicpath)
        self.check_path(self.videopath)
        self.check_path(self.imagepath)

    def getnickname(self, html):
        return html['aweme_list'][0]['author']['nickname']

    def downpageinfo(self, max_cursor, isfirst):
        api_post_url = self.createurl(max_cursor, isfirst)
        response = requests.get(url=api_post_url, headers=self.headers)
        html = json.loads(response.content.decode())
        return html

    def createurl(self, max_cursor, isfirst):
        if isfirst == 1:
            signature = self.firstsignature
        else:
            signature = self.nextsignature
        return 'https://www.iesdouyin.com/web/api/v2/aweme/%s/?sec_uid=%s&count=%s&max_cursor=%s&aid=1128&_signature=%s=' % (
            self.mode, self.sec, str(self.count), max_cursor, signature)

    # 获取第一次api数据
    def get_data(self, max_cursor):
        html = self.download_html(max_cursor, 1)
        if html == '':
            print('[  提示  ]:抓获数据失败!\r')
            return
        print('[  用户  ]:', str(self.nickname), '\r')
        self.crawl_info(html)

        return max_cursor

    def download_html(self, max_cursor, isfirst):
        # 尝试次数
        index = 0
        # 存储api数据
        result = []
        success = False
        while success == False and self.Isend == False:
            index += 1
            if index > 1:
                print('[  提示  ]:正在进行第 %d 次尝试\r' % index)
            time.sleep(self.sleep_sec)
            try:
                html = self.downpageinfo(max_cursor, isfirst)
                success = True
            except Exception as error:
                print('[  提示  ]:sleep:', self.sleep_sec)
                time.sleep(self.sleep_sec)
                if index >= self.max_retry_count:
                    print('[  提示  ]:最大下载出错次数 %d , 停止下载。 \r', index)
                    return
                continue
        if success:
            return html
        return ''

    def computer_sleep_time(self):
        if self.down_count == 0:
            self.zero_count = self.zero_count + 1
        else:
            self.zero_count = self.zero_count - 1
        if self.zero_count > 10:
            self.zero_count = 10
        if self.zero_count < 0:
            self.zero_count = 0

        if self.down_count < 20:
            self.sleep_sec = 0.3
        else:
            self.sleep_sec = 0.3
            self.zero_count = 0

        self.sleep_sec = self.sleep_sec * (self.zero_count + 1)

        self.down_count = 0

    def fill_user_sec(self):
        # 获取解码后原地址
        r = requests.get(url=self.Find(self.uid)[0])
        for one in re.finditer(r'user\/([\d\D]*)', str(r.url)):
            self.sec = one.group(1)

    # 下一页
    def next_data(self, max_cursor):
        self.computer_sleep_time()
        self.fill_user_sec()
        html = self.download_html(max_cursor, 2)

        if html == '':
            print('[  提示  ]:%d页抓获数据失败!\r' % max_cursor)
            return

        if max_cursor == 0:
            self.Isend = True
            return

        self.crawl_info(html)

    def crawl_info(self, html):
        max_cursor = html['max_cursor']
        result = html['aweme_list']
        # print('[  提示  ]:抓获数据成功!\r')
        # 处理第一页视频信息
        self.video_info(result, max_cursor)

    # 处理视频信息
    def video_info(self, result, max_cursor):
        # 作者信息      # 无水印视频链接    # 作品id        # 作者id      # 唯一视频标识# 封面大图
        author_list = []
        video_list = []
        aweme_id = []
        nickname = []
        uri_list = []  # dynamic_cover = []

        list_count = self.count;
        if len(result) < self.count:
            list_count = len(result)
        for v in range(list_count):
            try:
                author_list.append(str(result[v]['desc']))
                # 2022/04/22
                # 如果直接从 /web/api/v2/aweme/post 这个接口拿数据，那么只有720p的清晰度
                # 如果在 /web/api/v2/aweme/iteminfo/ 这个接口拿视频uri
                # 拼接到 aweme.snssdk.com/aweme/v1/play/?video_id=xxxx&radio=1080p 则获取到1080p清晰的
                video_list.append(str(result[v]['video']['play_addr']['url_list'][0]))
                uri_list.append(str(result[v]['video']['play_addr']['uri']))
                aweme_id.append(str(result[v]['aweme_id']))
                nickname.append(str(result[v]['author']['nickname']))
                # dynamic_cover.append(str(result[v]['video']['dynamic_cover']['url_list'][0]))
            except Exception as error:
                # print(error)
                pass
        # 过滤视频文案和作者名中的非法字符
        if list_count >0:
            # print('[  提示  ]:等待替换文案非法字符!\r')
            author_list = self.replaceT(author_list)
            # print('[  提示  ]:等待替换作者非法字符!\r')
            nickname = self.replaceT(nickname)
            self.videos_download(author_list, video_list, uri_list, aweme_id, nickname, max_cursor)
        else:
            print('[  提示  ]:无采集数据!\r')
        return self, author_list, video_list, uri_list, aweme_id, nickname, max_cursor

    # 检测视频是否已经下载过
    def check_info(self, nickname):
        if nickname == []:
            return
        else:
            v_info = self.fillfileinfo(self.musicpath, [])
            v_info = self.fillfileinfo(self.videopath, v_info)
            v_info = self.fillfileinfo(self.imagepath, v_info)
        return v_info

    def fillfileinfo(self, currentpath, info):
        v_info = os.listdir(currentpath)
        for i in range(len(v_info)):
            info.append(v_info[i][19:len(v_info[i])])
        return info

    def check_path(self, savepath):
        if not os.path.exists(savepath):
            os.makedirs(savepath)

    def down_info(self, aweme_id):
        jx_url = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={aweme_id}'  # 官方接口
        js = json.loads(requests.get(url=jx_url, headers=self.headers).text)
        return js

    # 音视频下载
    def videos_download(self, author_list, video_list, uri_list, aweme_id, nickname, max_cursor):
        if self.v_info == None:
            self.v_info = self.check_info(self.nickname)

        # self.count值可能大于实际api的长度，所以用len(author_list) 2022/03/22改
        for i in range(len(author_list)):

            # Code From RobotJohns https://github.com/RobotJohns
            # 移除文件名称  /r/n
            author_list[i] = self.getfilename(author_list[i])

            # 每次判断视频是否已经下载过
            length = len(video_list[i])
            video_not_exist = not (author_list[i] + '.mp4' in self.v_info) and video_list[i][length-4:length] != ".mp3"
            music_not_exist = not (author_list[i] + '.mp3' in self.v_info) and self.musicarg == "yes"
            download_image = self.picarg == "yes"
            js = None
            if video_not_exist or music_not_exist or download_image:
                try:
                    jx_url = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={aweme_id[i]}'  # 官方接口
                    js = json.loads(requests.get(url=jx_url, headers=self.headers).text)

                    creat_time = time.strftime("%Y-%m-%d %H.%M.%S", time.localtime(js['item_list'][0]['create_time']))
                except Exception as error:
                    print(error)
                    pass
            # 点赞视频排序
            self.like_counts += 1

            if download_image:
                self.downimage(js, creat_time)

            if music_not_exist:  # 保留音频
                self.downloadmusic(author_list[i], nickname[i], creat_time, js)

            if video_not_exist:
                self.downloadvideo(author_list[i], nickname[i], creat_time, video_list[i], uri_list[i])

        if self.crawlmode == "2":
            # 获取下一页信息
            self.next_data(max_cursor)

    def downimage(self, js, creat_time):
        image_url_list = self.getImageList(js)
        if len(image_url_list) == 0:
            return
        for j in range(len(image_url_list)):
            pic_title = str(js['item_list'][0]['desc'])
            try:
                picture = requests.get(url=image_url_list[j], headers=self.headers)
                p_url = self.createfilename(creat_time, pic_title + '_' + str(j), ".jpeg")
                if self.check_file_exists(pic_title + '_' + str(j), ".jpeg"):
                    return
                p_url = os.path.join(self.imagepath, p_url)
                not (p_url in self.v_info)
                with open(p_url, 'wb') as file:
                    file.write(picture.content)
                    print('[  提示  ]:' + p_url + '下载完毕\r')
            except Exception as error:
                print('[  错误  ]:' + error + '\r')
                print('[  提示  ]:发生了点意外！\r')

    def getImageList(self, js):
        imagelist = []
        if js['item_list'][0]['images'] is None:
            return imagelist

        for i in range(len(js['item_list'][0]['images'])):
            pic_url = str(js['item_list'][0]['images'][i]['url_list'][0])
            imagelist.append(pic_url)
        return imagelist

    def getfilename(self,filename):
        filename = ''.join(filename.splitlines())
        if len(filename) > 182:
            # print("[  提示  ]:", "文件名称太长 进行截取")
            filename = filename[0:180]
            # print("[  提示  ]:", "截取后的文案：{0}，长度：{1}".format(filename, len(filename)))
        return filename
    def downloadvideo(self,filename, nickname, creat_time, videoinfo, vurl):
        # 尝试下载视频
        uri_url = 'https://aweme.snssdk.com/aweme/v1/play/?video_id=%s&radio=1080p&line=0'
        try:
            start = time.time()  # 下载开始时间
            # new_video_list.append(uri_url % uri_list[i])  # 生成1080p视频链接
            video = requests.get(videoinfo)  # 视频信息
            # t_video = requests.get(url=new_video_list[i],
            #                       headers=self.headers).content  # 视频内容
            if video.status_code == 200:  # 判断是否响应成功
                result = self.downloadvideofile(video, creat_time, filename, nickname, vurl)
                end = time.time()  # 下载结束时间
                if result:
                    self.down_count = self.down_count + 1;
                    print('\n' + '[下载完成]:耗时: %.2f秒, 成功下载：%d\n' % (end - start, self.down_count))
                else:
                    print('\n' + '[下载出错]:耗时: %.2f秒\n' % (end - start))
            else:
                print('[  警告  ]:视频信息获取出错，跳过!')

        except Exception as error:
            print(error)
            print('[  提示  ]:该页视频资源没有', self.count, '个,已为您跳过！\r')

    def downloadvideofile(self, video, creat_time, filename, nickname, vurl):
        uri_url = 'https://aweme.snssdk.com/aweme/v1/play/?video_id=%s&radio=1080p&line=0'
        try:
            content_size = int(video.headers['content-length'])  # 下载文件总大小
            print('[  ' + '视频' + '  ]:' + creat_time + filename + '[文件 大小]:{size:.2f} MB'.format(
                size=content_size / 1024 / 1024))  # 开始下载，显示下载文件大小
            v_url = self.createfilename(creat_time, re.sub(r'[\\/:*?"<>|\r\n] + ', "_", filename),
                                        '.mp4')
            v_url = os.path.join(self.videopath, v_url)
            t_video = self.downloadfile(uri_url % vurl, 3)
            if t_video == None:
                print('[  警告  ]:下载视频出错,跳过!')
                return False

            with open(v_url, 'wb') as file:  # 显示进度条
                file.write(t_video)
            return True

        except Exception as error:
            print('[  警告  ]:下载视频出错!')
            print('[  警告  ]:', error, '\r')

    def downloadmusic(self, filename, nickname, creat_time, js):
        try:
            if self.musicarg == "yes":  # 保留音频
                music_url = str(js['item_list'][0]['music']['play_url']['url_list'][0])
                music_title = re.sub(r'[\\/:*?"<>|\r\n] + ', "_", filename) #str(js['item_list'][0]['music']['author'])
                music = requests.get(music_url)  # 保存音频
                if music.status_code == 200:  # 判断是否响应成功
                    m_url = self.createfilename(creat_time, music_title)
                    self.savefile(music, os.path.join(self.musicpath, m_url), creat_time, filename)

        except Exception as error:
            print(error)
            print('\r[  警告  ]:下载音频出错!\r')

    def savefile(self,urlfileinfo, m_url,creat_time, filename, tag = '音频', content_size = 0):
        start = time.time()  # 下载开始时间
        size = 0  # 初始化已下载大小
        chunk_size = 1024  # 每次下载的数据大小
        if content_size ==0 :
            content_size = int(urlfileinfo.headers['content-length'])  # 下载文件总大小
        print('[  ' + tag + '  ]:' + creat_time + filename + '[文件 大小]:{size:.2f} MB'.format(
            size=content_size / chunk_size / 1024))  # 开始下载，显示下载文件大小

        with open(m_url, 'wb') as file:  # 显示进度条
            for data in urlfileinfo.iter_content(chunk_size=chunk_size):
                file.write(data)
                size += len(data)
                print('\r' + '[下载进度]:%s%.2f%%' % (
                    '>' * int(size * 50 / content_size), float(size / content_size * 100)), end=' ')

            end = time.time()  # 下载结束时间
            self.down_count = self.down_count + 1;
            print('\n' + '[下载完成]:耗时: %.2f秒, 成功下载：%d\n' % (end - start, self.down_count))  # 输出下载用时时间

    def check_file_exists(self, title, fileext):
        filename = self.createfilename('', title, fileext)
        return filename in self.v_info

    def createfilename(self, creat_time, title, fileext = '.mp3'):
        m_url = ''
        if self.mode == 'post':
            m_url = m_url + creat_time
        else:
            m_url = m_url + str(self.like_counts) + '、'
        m_url = m_url + re.sub(r'[\\/:*?"<>|\r\n]+', "_", title) + fileext
        return m_url

    def downloadfile(self,url, retrycount):
        content = self.downloadresponse(url, retrycount);
        if content == None:
            return
        if content.status_code != 200:
            print('[  警告  ]:下载视频出错!')
            return None
        return content.content

    def downloadtext(self,url, retrycount):
        content = self.downloadresponse(url, retrycount);
        if content == None:
            return
        return content.text

    def downloadresponse(self,url, retrycount):
        while True:
            try:
                return requests.get(url=url, headers=self.headers)  # 视频内容
            except Exception as error:
                print('[  提示  ]:下载资源出错。\r')
                retrycount = retrycount -1
                if retrycount > 0:
                    continue
                return



# 主模块执行
if __name__ == "__main__":
    # 获取命令行函数
    def crawldata(args):
        args1 = read_args(args)
        print(
            '[  提示  ]:采集参数：mode：' + args1.mode + ',save-path:' + args1.savedir + ',music-arg:' + args1.musicarg
            + ',crawl-mode:' + args1.crawlmode + '....\r')

        for index in range(len(args1.uids)):
            selfuid = args1.uids[index]
            down_video(selfuid, args1.savedir, args1.musicarg, args1.count, args1.mode, args1.crawlmode, args1.picarg)

        input('[  完成  ]:已完成批量下载，输入任意键后退出:')
        sys.exit(0)


    def read_args(args):
        if args.user == None:
            if os.path.isfile(args.file) == False:
                gen_default_config_file()
                print('[  提示  ]:配置文件不存在.\r')
                sys.exit(0)
            # config read
            # 实例化读取配置文件
            cf = configparser.ConfigParser()

            # 用utf-8防止出错
            cf.read(args.file, encoding="utf-8")

            # 读取保存路径
            args.savedir = cf.get("save", "url")

            # 读取下载视频个数
            args.count = int(cf.get("count", "count"))

            # 读取下载是否下载音频
            args.musicarg = cf.get("music", "musicarg")
            args.picarg = cf.get("music", "picarg")

            # 读取用户主页地址
            args.uids = cf.get("url", "uid").split(',')
            # 读取下载模式
            args.mode = cf.get("mode", "mode")

            # 读取下载模式
            args.crawlmode = cf.get("crawlmode", "crawlmode")
            args.sleeptime = cf.get("crawlmode", "sleeptime")
        else:
            args.uids = [args.user]
        for i in range(len(args.uids)):
            if args.uids[i][0:5] == "https":
                continue
            args.uids[i] = "https://v.douyin.com/" + args.uids[i] + '/'

        return args


    def down_video(user, selfsave, music, count, mode, crawlmode, pic):
        try:
            print('[  提示  ]:开始采集：' + user + '....\r')
            # 新建TK实例
            TK = TikTok()
            # 命令行传参
            TK.setting(user, music, count, selfsave, mode, crawlmode, pic)
            print('[  提示  ]:完成采集：' + user + '.\r\r\n')
            time.sleep(1)
        except Exception as e:
            # print(e)
            print('[  警告  ]:', e, '可以复制此报错内容发issues\r\n')
        return user


    def gen_default_config_file():
        defaultfile = "defaultconf.ini"
        # 检测配置文件
        if os.path.isfile(defaultfile) == True:
            pass
        else:
            print('[  提示  ]:没有检测到配置文件，生成中!\r')
            try:
                cf = configparser.ConfigParser()
                # 往配置文件写入内容
                cf.add_section("url")
                cf.set("url", "uid", "https://v.douyin.com/JcjJ5Tq/")
                cf.add_section("music")
                cf.set("music", "musicarg", "yes")
                cf.set("music", "picarg", "yes")
                cf.add_section("count")
                cf.set("count", "count", "35")
                cf.add_section("save")
                cf.set("save", "url", "./Download/")
                cf.add_section("mode")
                cf.set("mode", "mode", "post")
                cf.add_section("crawlmode")
                cf.set("crawlmode", "crawlmode", "1")
                with open(defaultfile, "a+") as f:
                    cf.write(f)
                print('[  提示  ]:生成成功!\r')
            except:
                input('[  提示  ]:生成失败,正在为您下载配置文件!\r')
                r = requests.get('https://gitee.com/johnserfseed/TikTokDownload/raw/main/conf.ini')
                with open(defaultfile, "a+") as conf:
                    conf.write(r.content)


    def print_logo():
        print(r'''
  ████████╗██╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗
  ╚══██╔══╝██║██║ ██╔╝╚══██╔══╝██╔═══██╗██║ ██╔╝██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗
     ██║   ██║█████╔╝    ██║   ██║   ██║█████╔╝ ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║
     ██║   ██║██╔═██╗    ██║   ██║   ██║██╔═██╗ ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║
     ██║   ██║██║  ██╗   ██║   ╚██████╔╝██║  ██╗██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝
     ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝''')
        # 绘制布局
        print("#" * 120)
        print(
            """
                                                        TikTokDownload V1.2.5
                使用说明：
                        1、本程序目前支持命令行调用和配置文件操作，GUI预览版本已经发布
                        2、命令行操作方法：1）将本程序路径添加到环境变量
                                        2）控制台输入 TikTokMulti -u https://v.douyin.com/JtcjTwo/

                        3、配置文件操作方法：1）运行软件前先打开目录下 conf.ini 文件按照要求进行配置
                                        2）按照控制台输出信息操作

                        4、如有您有任何bug或者意见反馈请在 https://github.com/Johnserf-Seed/TikTokDownload/issues 发起
                        5、GUI预览版本现已发布，操作更简单 https://github.com/Johnserf-Seed/TikTokDownload/tags 下载

                注意：  目前已经支持app内分享短链和web端长链识别。
            """
        )
        print("#" * 120)
        print('\r')


    def parse_command_line():
        parser = argparse.ArgumentParser(description='TikTokMulti V1.2.5 使用帮助')
        parser.add_argument('--user', '-u', type=str, help='为用户主页链接，非必要参数', required=False)
        parser.add_argument('--savedir', '-d', type=str, help='视频保存目录，非必要参数， 默认./Download', default='./Download/')
        # parser.add_argument('--single', '-s', type=str, help='单条视频链接，非必要参数，与--user参数冲突')
        parser.add_argument('--music', '-m', type=str, help='视频音乐下载，非必要参数， 默认no可选yes', default='no')
        parser.add_argument('--pic', '-p', type=str, help='图像下载，非必要参数， 默认no可选yes', default='no')
        parser.add_argument('--count', '-c', type=int, help='单页下载的数量，默认参数 35 无须修改', default=35)
        parser.add_argument('--mode', '-M', type=str, help='下载模式选择，默认post:发布的视频 可选like:点赞视频(需要开放权限)', default='post')
        parser.add_argument('--file', '-F', type=str, help='下载配置文件，默认为conf.ini', default='conf.ini')
        parser.add_argument('--crawlmode', '-C', type=str, help='采集模式：1 采集第一页 2 采集所有页面', default='1')
        parser.add_argument('--sleeptime', '-S', type=float, help='每页下载等待时间，默认0.5秒', default='0.5')
        return parser.parse_args()


    try:
        print_logo()
        args = parse_command_line()
        # 获取命令行
        crawldata(args)
    except Exception as e:
        # print(e)
        print('[  警告  ]:', e, '可以复制此报错内容发issues')
        print('[  提示  ]:未输入命令或意外出错，自动退出!')
        sys.exit(0)
