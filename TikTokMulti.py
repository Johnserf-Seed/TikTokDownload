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
import requests,json,os,time,configparser,re
import sys
sys.path.append('../')
#返回个人主页api数据
def get_info(count,mode,uid):
    #获取解码后原地址
    r = requests.get(url = Find(uid)[0])
    #获取用户sec_uid
    key = re.findall('&sec_uid=(.*?)&u_code=',str(r.url))[0]
    if key == '':
        key = re.findall('&sec_uid=(.*?)&',str(r.url))[0]
        
    api_post_url = 'https://www.iesdouyin.com/web/api/v2/aweme/%s/?sec_uid=%s&count=%s&max_cursor=0&aid=1128&_signature=RuMN1wAAJu7w0.6HdIeO2EbjDc&dytk=' % (mode,key,str(count))
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    i = 0
    result = []
    while result == []:
        i = i + 1
        print('---正在进行第 %d 次尝试...\r' % i)
        time.sleep(0.3)
        response = requests.get(url = api_post_url,headers=headers)
        html = json.loads(response.content.decode())
        if html['aweme_list'] != []:
            result = html['aweme_list']
            print('---抓获数据成功---\r')
    return result

#获取用户主页信息
def video_info(count,result):
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
    for i in range(count):
        try:
            author_list.append(str(result[i]['desc']))
            video_list.append(str(result[i]['video']['play_addr']['url_list'][0]))
            aweme_id.append(str(result[i]['aweme_id']))
            nickname.append(str(result[i]['author']['nickname']))
            dynamic_cover.append(str(result[i]['video']['dynamic_cover']['url_list'][0]))
        except:
            #print('抓取失败....')
            pass
    return author_list,video_list,aweme_id,nickname,dynamic_cover

def Find(string): 
    # findall() 查找匹配正则表达式的字符串
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
    return url 

#下载作品封面、原声、视频
def download_all(count,author_list,video_list,aweme_id,nickname,dynamic_cover,mode,save):    
    for i in range(count):
        try:
            video = requests.get(video_list[i])
            try:
                #创建并检测下载目录是否存在
                os.makedirs(save + mode + "\\" + nickname[i])
            except:
                pass
            #保存视频
            with open(save + mode + "\\" + nickname[i] + '\\' + author_list[i] + '.mp4','wb') as f:
                f.write(video.content)
            #保存视频动态封面
            dynamic = requests.get(dynamic_cover[i])
            with open(save + mode + '\\'+ nickname[i] + '\\' + author_list[i] + '.webp','wb') as f:
                f.write(dynamic.content)
        except:    
            pass
    return

def read_conf():
    #实例化读取配置文件
    cf = configparser.ConfigParser()
    #用utf-8防止出错
    cf.read("conf.ini", encoding="utf-8")
    #读取保存路径
    save = cf.get("save","url")
    #读取下载视频个数
    count = int(cf.get("count","count"))
    #读取用户主页地址
    uid = cf.get("url","uid")
    #读取下载模式
    mode = cf.get("mode","mode")
    print('读取配置完成....\r')
    return uid,count,save,mode

#主模块执行
if __name__ == "__main__":

#    print('''
#抓取用户作品输入1
#抓取用户喜欢作品输入2
#    ''')
    #下载模式选择
    #mode = int(input('请输入：'))
    #if mode == 1:
    #    mode = 'post'
    #else:
    #    mode = 'like'

    #读取配置
    uid,count,save,mode = read_conf()   
    #返回个人主页api数据
    result = get_info(count,mode,uid)
    #处理视频api数据
    author_list,video_list,aweme_id,nickname,dynamic_cover = video_info(count,result)
    #下载全部资源
    download_all(count,author_list,video_list,aweme_id,nickname,dynamic_cover,mode,save)