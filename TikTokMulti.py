#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:       
@Date       :2021/01/23 17:35:42
@Author     :JohnserfSeed
@version    :1.0
@License    :(C)Copyright 2017-2020, Liugroup-NLPR-CASIA
@Mail       :johnserfseed@gmail.com
'''
import requests,json,os,time,configparser,re,time
import sys

class TikTok():
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.66'
            }

    def fabu_time(self,t):
        '''
        将时间戳转换成时间格式
        :param t:
        :return:
        '''
        timeArray = time.localtime(t)
        fabu_time = time.strftime("%Y-%m-%d %H-%M-%S", timeArray)
        return '({})'.format(fabu_time)

    #单视频下载
    def single_down(self,url,save,fileType):
        key = re.findall('video/(\d+)/',url)[0]
        jx_url = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={key}'    #官方接口
        jss = json.loads(requests.get(url = jx_url,headers=self.headers).text)

        try:
            video_url = str(jss['item_list'][0]['video']['play_addr']['url_list'][0]).replace('playwm','play')   #去水印后链接
        except:
            print('视频链接获取失败\r')
            video_url = ''
            pass
        try:
            music_url = str(jss['item_list'][0]['music']['play_url']['url_list'][0])
        except:
            print('该音频目前不可用\r')
            music_url = ''
            pass

        try: 
            creat_time = self.fabu_time(jss['item_list'][0]['create_time'])
        except:
            creat_time = ''
            pass

        try:
            video_title = str(jss['item_list'][0]['desc'])
            music_title = str(jss['item_list'][0]['music']['title'])
            nickname = str(jss['item_list'][0]['author']['nickname'])
        except:
            print('标题获取失败')
            video_title = '视频走丢啦~'
            music_title = '音频走丢啦~'
            pass
        try:
            dynamic_cover = str(jss['item_list'][0]['video']['dynamic_cover']['url_list'][0])   #视频动态封面
        except:
            print('视频动态封面获取失败\r')
            dynamic_cover = ''
            pass

        if video_title == '':
            video_title = '此视频没有文案_%s' % music_title
        headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.66'
        }
       
        try:
            #创建并检测下载目录是否存在
            os.makedirs(save + nickname)
        except:
            pass

        if (fileType == 0 or fileType == 1):
             #单视频下载
            r=requests.get(url=video_url,headers=headers)
            print('视频 ',video_title,'   下载中\r')
            with open(save + nickname +  "/" + re.sub(r'[\\/:*?"<>|\r\n]+', "_", video_title) + creat_time +'.mp4','wb') as f:
                f.write(r.content)

        if (fileType == 0 or fileType == 2):
            #原声下载    
            r=requests.get(url=music_url,headers=headers)
            print('音频 ',music_title,'    下载中\r')
            with open(save + nickname +  "/" + re.sub(r'[\\/:*?"<>|\r\n]+', "_", music_title) + '.mp3','wb') as f:
                f.write(r.content)

        if (fileType == 0 or fileType == 3):
            #视频动态封面下载
            r=requests.get(url=dynamic_cover,headers=headers)
            print('视频动态封面 ',video_title,'   下载中\r')
            with open(save + nickname +  "/" + re.sub(r'[\\/:*?"<>|\r\n]+', "_", video_title) + creat_time +'.webp','wb') as f:
                f.write(r.content)

        input('....下载完成，按任意键退出....\r')
        sys.exit()
        return 

    #返回个人主页api数据 只能抓取30个
    def get_info_short(self,count,mode,uid,save,fileType):
        #获取解码后原地址
        r = requests.get(url = self.Find(uid)[0])
        #single_url = 'https://www.iesdouyin.com/share/video/'
        multi_url = 'https://www.iesdouyin.com/share/user/'
        if r.url[:37] == multi_url:
            print('....为您下载多个视频....\r')
            pass
        else:
            print('....为您下载单个视频....\r')
            self.single_down(r.url,save,fileType)

        #获取用户sec_uid
        key = re.findall('&sec_uid=(.*?)&',str(r.url))[0]
        #if key == '':
        #    key = re.findall('&sec_uid=(.*?)&',str(r.url))[0]
        api_post_url = 'https://www.iesdouyin.com/web/api/v2/aweme/%s/?sec_uid=%s&count=%s&max_cursor=0&aid=1128&_signature=RuMN1wAAJu7w0.6HdIeO2EbjDc&dytk=' % (mode,key,str(count))
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
            }
        index = 0
        result = []
        while result == []:
            index = index + 1
            print('---正在进行第 %d 次尝试---\r' % index)
            time.sleep(0.3)
            response = requests.get(url = api_post_url,headers=header)
            html = json.loads(response.content.decode())
            if html['aweme_list'] != []:
                result = html['aweme_list']
                print('---抓获数据成功---\r')
        return result

    #返回个人主页api数据 全部抓取
    def get_info(self,count,mode,uid,save,fileType):
        #获取解码后原地址
        r = requests.get(url = self.Find(uid)[0])
        #single_url = 'https://www.iesdouyin.com/share/video/'
        multi_url = 'https://www.iesdouyin.com/share/user/'
        if r.url[:37] == multi_url:
            print('....为您下载多个视频....\r')
            pass
        else:
            print('....为您下载单个视频....\r')
            self.single_down(r.url,save,fileType)

        #获取用户sec_uid
        print(str(r.url))
        key = re.findall('sec_uid=(.*?)&',str(r.url))[0]
        #if key == '':
        #    key = re.findall('&sec_uid=(.*?)&',str(r.url))[0]
        api_post_url = 'https://www.iesdouyin.com/web/api/v2/aweme/%s/?sec_uid=%s&count=%s&max_cursor=0&aid=1128&_signature=RuMN1wAAJu7w0.6HdIeO2EbjDc&dytk=' % (mode,key,str(count))
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
            }
        index = 0
        result = []
        while 1:
            index = index + 1
            print('---正在进行第 %d 次尝试---\r' % index)
            time.sleep(0.3)
            response = requests.get(url = api_post_url,headers=header)
            html = json.loads(response.content.decode())
            print(html['max_cursor'])
            api_post_url = 'https://www.iesdouyin.com/web/api/v2/aweme/%s/?sec_uid=%s&count=%s&max_cursor=%s&aid=1128&_signature=RuMN1wAAJu7w0.6HdIeO2EbjDc&dytk=' % (mode, key, str(count),html['max_cursor'])
            if html['aweme_list'] != []:
                for i in html['aweme_list']:
                    result.append(i)
                #result = list(set(result))
                print('---抓获数据成功---\r')
            if html['max_cursor'] ==0:
                break
        return result

    #获取用户主页信息
    def video_info(self,count,result):
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
        for i2 in range(count):
            try:
                author_list.append(str(result[i2]['desc']))
                video_list.append(str(result[i2]['video']['play_addr']['url_list'][0]))
                aweme_id.append(str(result[i2]['aweme_id']))
                nickname.append(str(result[i2]['author']['nickname']))
                dynamic_cover.append(str(result[i2]['video']['dynamic_cover']['url_list'][0]))
            except:
                print('抓取失败....')
                pass
        return author_list,video_list,aweme_id,nickname,dynamic_cover

    #匹配粘贴的url地址
    def Find(self,string): 
        # findall() 查找匹配正则表达式的字符串
        url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
        return url 

    #下载作品封面、原声、视频
    def download_all(self,count,author_list,video_list,aweme_id,nickname,dynamic_cover,mode,save,fileType):
        for i in range(count):
            try:
                #创建并检测下载目录是否存在
                os.makedirs(save + mode + "/" + nickname[i])
            except:
                pass
            jx_url  = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={aweme_id[i]}'    #官方接口
            js = json.loads(requests.get(url = jx_url,headers=self.headers).text)
            try: 
                creat_time = self.fabu_time(js['item_list'][0]['create_time'])
            except:
                creat_time = ''

            if (fileType == 0 or fileType == 2):
                try:
                    music_url = str(js['item_list'][0]['music']['play_url']['url_list'][0])
                    music_title = str(js['item_list'][0]['music']['author'])
                    r=requests.get(music_url)
                    print('音频 ',music_title,'    下载中\r')
                    with open(save + mode + "/" + nickname[i] + '/' + re.sub(r'[\\/:*?"<>|\r\n]+', "_", music_title) + '.mp3','wb') as f:
                        f.write(r.content)
                except:
                    if music_url == '':
                        print('该音频目前不可用\r')
                    else:
                        pass

            if (fileType == 0 or fileType == 1 or fileType == 3):
                try:
                    video = requests.get(video_list[i])
                    if (fileType == 0 or fileType == 1):
                        #保存视频
                        print('视频 ',author_list[i],'    下载中\r')
                        with open(save + mode + "/" + nickname[i] + '/' + re.sub(r'[\\/:*?"<>|\r\n]+', "_", author_list[i]) + creat_time + '.mp4','wb') as f:
                            f.write(video.content)
                    if (fileType == 0 or fileType == 3):
                        #保存视频动态封面
                        dynamic = requests.get(dynamic_cover[i])
                        with open(save + mode + '/'+ nickname[i] + '/' + re.sub(r'[\\/:*?"<>|\r\n]+', "_", author_list[i]) + creat_time + '.webp','wb') as f:
                            f.write(dynamic.content)
                except:    
                    pass
        sys.exit(input('....下载完成，按任意键退出....'))
        return

    #读取并生成配置
    def read_conf(self):
        if os.path.isfile("conf.ini") == True:
            pass
        else:
            print('....没有检测到配置文件，生成中....\r')
            try:
                cf = configparser.ConfigParser()
                # 往配置文件写入内容
                cf.add_section("url")
                cf.set("url", "uid", "https://v.douyin.com/JcjJ5Tq/")
                cf.add_section("music")
                cf.set("music", "musicarg", "yes")
                cf.add_section("count")
                cf.set("count", "count", "10")
                cf.add_section("save")
                cf.set("save", "url", "/Download/")
                cf.add_section("mode")
                cf.set("mode", "mode", "post")
                cf.add_section("fileType")
                cf.set("fileType", "fileType", "0")
                with open("conf.ini","a+") as f:
                    cf.write(f)
                print('....生成成功....')
            except:
                input('....生成失败,请前往GItHub下载配置文件....')
                sys.exit()

        #实例化读取配置文件
        cf = configparser.ConfigParser()
        #用utf-8防止出错
        cf.read("conf.ini", encoding="utf-8")
        #读取保存路径
        save = os.getcwd() + cf.get("save","url")
        #读取下载视频个数
        count = int(cf.get("count","count"))
        #读取用户主页地址
        uid = input('批量下载直接回车，单一视频直接粘贴：')
        if uid == '':
            uid = cf.get("url","uid")
        else:
            pass
        #读取下载模式
        mode = cf.get("mode","mode")
        #读取下载文件类型
        fileType = int(cf.get("fileType","fileType"))
        print('....读取配置完成....\r')
        return uid,count,save,mode,fileType

#主模块执行
if __name__ == "__main__":
    print("#" * 110)
    print( 
"""
                                            TikTokDownload V1.1
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
    
    #实例化TiTk
    TiTk = TikTok()
    #读取配置
    uid,count,save,mode,fileType = TiTk.read_conf()   
    #返回个人主页api数据
    result = TiTk.get_info(count,mode,uid,save,fileType)
    #处理视频api数据
    author_list,video_list,aweme_id,nickname,dynamic_cover = TiTk.video_info(count,result)
    #下载全部资源
    TiTk.download_all(count,author_list,video_list,aweme_id,nickname,dynamic_cover,mode,save,fileType)