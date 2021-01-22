#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:       
@Date       :2020/12/28 13:14:29
@Author     :JohnserfSeed
@version    :1.0
@License    :(C)Copyright 2017-2020, Liugroup-NLPR-CASIA
@Mail       :johnserfseed@gmail.com
'''
import requests,re,json,sys,getopt

def printUsage():
	print ('''
        使用方法: 1、添加为环境变量 2、输入命令
        -u<url 抖音复制的链接:https://v.douyin.com/JtcjTwo/>
        -m<music 是否下载音频,默认为yes可选no>
        
        例如：TikTokDownload.exe -u https://v.douyin.com/JtcjTwo/ -m yes
        
    ''')
    #TikTokDownLoad.exe --url=<抖音复制的链接> --music=<是否下载音频,默认为yes可选no>
    
def Find(string): 
    # findall() 查找匹配正则表达式的字符串
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
    return url 

def main():
    urlarg=""
    musicarg="yes"
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hu:m:",["url=","music="])
    except getopt.GetoptError:
        printUsage()
        sys.exit(-1)
    try:    
        if opts == []:
            urlarg = str(input("请输入抖音链接:"))
            return urlarg,musicarg
    except:
        pass
    for opt,arg in opts:
        if opt == '-h':
            printUsage()
            sys.exit(-1)
        elif opt in ("-u", "--url"):
            urlarg=arg
        elif opt in ("-m","--music"):
            musicarg=arg
    return urlarg,musicarg
    
def download(video_url,music_url,video_title,music_title,headers,musicarg):
    #视频下载
    r=requests.get(url=video_url,headers=headers)
    if video_title == '':
        video_title = '此视频没有文案_%s' % music_title
    with open(f'{video_title}.mp4','wb') as f:
        f.write(r.content)
    
    #原声下载
    if musicarg != 'yes':
        input('下载完成，按任意键退出。。。')
        return
    else:
        r=requests.get(url=music_url,headers=headers)
        with open(f'{music_title}.mp3','wb') as f:
            f.write(r.content)
        input('下载完成，按任意键退出。。。')
        return

def get_info():
    #返回个人主页api数据
    api_post_url = 'https://www.iesdouyin.com/web/api/v2/aweme/like/?sec_uid=MS4wLjABAAAA5sofqwkCjeZqwtTMs00E5HAg8udRR-warVgfPykwwgk&count=%d' % int(input('输入抓取视频个数，不输入默认抓取全部:'))
    i = 0
    result = []
    while result == []:
        i = i + 1
        print('---正在第 %d 次尝试...\r' % i)
        response = requests.get(api_post_url)
        html = json.loads(response.content.decode())
        if html['aweme_list'] != []:
            result = html['aweme_list']
            print('---抓获数据成功...\r')
    return result

if __name__=="__main__":
    urlarg,musicarg=main()
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.66'
    }
    r = requests.get(url = Find(urlarg)[0])
    key = re.findall('video/(\d+)/',str(r.url))[0]
    jx_url  = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={key}'    #官方接口
    js = json.loads(requests.get(url = jx_url,headers=headers).text)
    video_url = str(js['item_list'][0]['video']['play_addr']['url_list'][0]).replace('playwm','play')   #去水印后链接
    music_url = str(js['item_list'][0]['music']['play_url']['url_list'][0])
    video_title = str(js['item_list'][0]['desc'])
    music_title = str(js['item_list'][0]['music']['author'])

    download(video_url,music_url,video_title,music_title,headers,musicarg)
	
