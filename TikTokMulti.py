#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:TikTokMulti.py
@Date       :2021/05/25 00:14:28
@Author     :JohnserfSeed
@version    :1.2
@License    :(C)Copyright 2019-2021, Liugroup-NLPR-CASIA
@Mail       :johnserfseed@gmail.com
'''

import requests,json,os,time,configparser,re,sys
import TikTokDownload

class TikTok():
    #初始化
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.66'
            }

        #绘制布局
        print("#" * 110)
        print( 
    """
                                                TikTokDownload V1.2
    使用说明：
            1、运行软件前先打开目录下 conf.ini 文件按照要求进行配置
            2、批量下载可直接修改配置文件，单一视频下载请直接打开粘贴视频链接即可
            3、如有您有任何bug或者意见反馈请在 https://github.com/Johnserf-Seed/TikTokDownload/issues 发起
            4、后续可能会更新GUI界面，操作更简单

    注意：  单个视频链接与用户主页链接要分清，软件闪退可以通过终端运行查看报错信息（一般是链接弄错的问题）
    """
        )
        print("#" * 110)
        print('\r')

        if os.path.isfile("conf.ini") == True:
            pass
        else:
            print('....没有检测到配置文件，生成中....\r')
            try:
                self.cf = configparser.ConfigParser()
                # 往配置文件写入内容
                self.cf.add_section("url")
                self.cf.set("url", "uid", "https://v.douyin.com/JcjJ5Tq/")
                self.cf.add_section("music")
                self.cf.set("music", "musicarg", "yes")
                self.cf.add_section("count")
                self.cf.set("count", "count", "35")
                self.cf.add_section("save")
                self.cf.set("save", "url", ".\\Download\\")
                self.cf.add_section("mode")
                self.cf.set("mode", "mode", "post")
                with open("conf.ini","a+") as f:
                    self.cf.write(f)
                print('....生成成功....')
            except:
                input('....生成失败,正在为您下载配置文件....')
                r =requests.get('https://gitee.com/johnserfseed/TikTokDownload/raw/main/conf.ini')
                with open("conf.ini", "a+") as conf:
                    conf.write(r.content)
                sys.exit()

        #实例化读取配置文件
        self.cf = configparser.ConfigParser()

        #用utf-8防止出错
        self.cf.read("conf.ini", encoding="utf-8")

        #读取保存路径
        self.save = self.cf.get("save","url")

        #读取下载视频个数
        self.count = int(self.cf.get("count","count"))

        self.musicarg = self.cf.get("music","musicarg")

        #读取用户主页地址
        self.uid = input('批量下载直接回车，单一视频下载直接粘贴视频链接：')
        if self.uid == '':
            self.uid = self.cf.get("url","uid")
        else:
            pass

        #读取下载模式
        self.mode = self.cf.get("mode","mode")
        print('....读取配置完成....\r')
        self.judge_link()

    #匹配粘贴的url地址
    def Find(self,string): 
        # findall() 查找匹配正则表达式的字符串
        url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
        return url

    #判断个人主页api链接
    def judge_link(self):
        #获取解码后原地址
        r = requests.get(url = self.Find(self.uid)[0])
        multi_url = 'https://www.iesdouyin.com/share/user/'

        #判断输入的是不是用户主页
        if r.url[:37] == multi_url:
            print('....为您下载多个视频....\r')
            #获取用户sec_uid
            key = re.findall('&sec_uid=(.*?)&',str(r.url))[0]
        else:
            print('....为您下载单个视频....\r')
            urlarg,musicarg = TikTokDownload.main()
            TikTokDownload.video_download(urlarg,musicarg)
            return

        #第一次访问页码
        max_cursor = 0

        #构造第一次访问链接
        api_post_url = 'https://www.iesdouyin.com/web/api/v2/aweme/%s/?sec_uid=%s&count=%s&max_cursor=%s&aid=1128&_signature=RuMN1wAAJu7w0.6HdIeO2EbjDc&dytk=' % (self.mode,key,str(self.count),max_cursor)
        self.get_data(api_post_url,max_cursor)
        return api_post_url,max_cursor,key

    #获取第一次api数据
    def get_data(self,api_post_url,max_cursor):
        #尝试次数
        index = 0

        #存储api数据
        result = []
        while result == []:
            index += 1
            print('---正在进行第 %d 次尝试---\r' % index)
            time.sleep(0.3)
            response = requests.get(url = api_post_url,headers=self.headers)
            html = json.loads(response.content.decode())

            if html['aweme_list'] != []:
                #下一页值
                max_cursor = html['max_cursor']
                result = html['aweme_list']
                print('---抓获数据成功---\r')

                #处理第一页视频信息
                self.video_info(result,max_cursor)
            else:
                print('---抓获数据失败---\r')

        return result,max_cursor

    #下一页
    def next_data(self,max_cursor):

        #获取解码后原地址
        r = requests.get(url = self.Find(self.uid)[0])

        #获取用户sec_uid
        key = re.findall('&sec_uid=(.*?)&',str(r.url))[0]

        #构造下一次访问链接
        api_naxt_post_url = 'https://www.iesdouyin.com/web/api/v2/aweme/%s/?sec_uid=%s&count=%s&max_cursor=%s&aid=1128&_signature=RuMN1wAAJu7w0.6HdIeO2EbjDc&dytk=' % (self.mode,key,str(self.count),max_cursor)
        
        index = 0
        result = []
        while result == []:
            index += 1
            print('---正在对',max_cursor,'页进行第 %d 次尝试---\r' % index)
            time.sleep(0.3)
            response = requests.get(url = api_naxt_post_url,headers=self.headers)
            html = json.loads(response.content.decode())

            if html['aweme_list'] != []:
                #下一页值
                max_cursor = html['max_cursor']
                result = html['aweme_list']
                print('---',max_cursor,'页抓获数据成功---\r')

                #处理下一页视频信息
                self.video_info(result,max_cursor)
            else:
                print('---',max_cursor,'页抓获数据失败---\r')
                sys.exit()

    #处理视频信息
    def video_info(self,result,max_cursor):

        #作者信息
        author_list = []

        #无水印视频链接
        video_list = []

        #作品id
        aweme_id = []

        #作者id
        nickname = []

        #封面大图
        dynamic_cover = []
        for i2 in range(self.count):
            try:
                author_list.append(str(result[i2]['desc']))
                video_list.append(str(result[i2]['video']['play_addr']['url_list'][0]))
                aweme_id.append(str(result[i2]['aweme_id']))
                nickname.append(str(result[i2]['author']['nickname']))
                dynamic_cover.append(str(result[i2]['video']['dynamic_cover']['url_list'][0]))
            except Exception as error:
                pass
                #print(error)
                #input('视频信息处理失败...')
                #sys.exit()
        self.videos_download(author_list,video_list,aweme_id,nickname,dynamic_cover,max_cursor)      
        return self,author_list,video_list,aweme_id,nickname,dynamic_cover,max_cursor

    def videos_download(self,author_list,video_list,aweme_id,nickname,dynamic_cover,max_cursor):
        for i in range(self.count):
            try:
                #创建并检测下载目录是否存在
                os.makedirs(self.save + self.mode + "\\" + nickname[i])
            except:
                #有目录不再创建
                pass
            try:
                jx_url  = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={aweme_id[i]}'    #官方接口
                js = json.loads(requests.get(url = jx_url,headers=self.headers).text)
                music_url = str(js['item_list'][0]['music']['play_url']['url_list'][0])
                music_title = str(js['item_list'][0]['music']['author'])
                if self.musicarg == "yes":
                    #保留音频
                    music=requests.get(music_url)
                    print('音频 ',music_title,'-',author_list[i],'    下载中\r')
                    m_url = self.save + self.mode + "\\" + nickname[i] + '\\' + re.sub(r'[\\/:*?"<>|\r\n]+', "_", music_title) + '_' + author_list[i] + '.mp3'
                    #print(m_url)
                    with open(m_url,'wb') as f:
                        f.write(music.content)
            except Exception as error:
                #print(error)
                if music_url == '':
                    print('该音频目前不可用\r')
                else:
                    pass
            try:
                video = requests.get(video_list[i])
                #保存视频
                print('视频 ',author_list[i],'    下载中\r')
                v_url = self.save + self.mode + "\\" + nickname[i] + '\\' + re.sub(r'[\\/:*?"<>|\r\n]+', "_", author_list[i]) + '.mp4'
                with open(v_url,'wb') as f:
                    f.write(video.content)

                #保存视频动态封面
                #dynamic = requests.get(dynamic_cover[i])
                #with open(self.save + self.mode + '\\'+ nickname[i] + '\\' + re.sub(r'[\\/:*?"<>|\r\n]+', "_", author_list[i]) + '.webp','wb') as f:
                #    f.write(dynamic.content)
            except Exception as error:
                pass
                #print(error)
                #input('缓存失败，请检查！')
                #sys.exit()
        self.next_data(max_cursor)

#主模块执行
if __name__ == "__main__":
    RTK = TikTok()
