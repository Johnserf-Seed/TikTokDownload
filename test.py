import requests,json,os,time,configparser,re

#返回个人主页api数据
def get_info(count,choose,uid):
    #获取解码后原地址
    r = requests.get(url = Find(uid)[0])
    #获取用户sec_uid
    key = re.findall('&sec_uid=(.*?)&u_code=',str(r.url))[0]

    api_post_url = 'https://www.iesdouyin.com/web/api/v2/aweme/%s/?sec_uid=%s&count=%d' % (choose,key,count)
    i = 0
    result = []
    while result == []:
        i = i + 1
        print('---正在进行第 %d 次尝试...\r' % i)
        time.sleep(0.3)
        response = requests.get(api_post_url)
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
            print('抓取失败....')
            pass
    return author_list,video_list,aweme_id,nickname,dynamic_cover

def Find(string): 
    # findall() 查找匹配正则表达式的字符串
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
    return url 

#下载作品封面、原声、视频
def download_all(count,author_list,video_list,aweme_id,nickname,dynamic_cover,choose):
    for i in range(count):
        try:
            video = requests.get(video_list[i])
            try:
                os.makedirs(".\\Download\\" + choose + "\\" + nickname[i])
            except:
                pass
            with open(".\\Download\\" + choose + "\\" + nickname[i] + '\\' + author_list[i] + '.mp4','wb') as f:
                f.write(video.content)
            dynamic = requests.get(dynamic_cover[i])
            with open('.\Download\\" + choose + "\\'+ nickname[i] + '\\' + author_list[i] + '.webp','wb') as f:
                f.write(dynamic.content)
        except:
            pass
    return

if __name__ == "__main__":
    #读取用户配置
    cf = configparser.ConfigParser()
    cf.read("conf.ini")

    #读取下载视频个数
    count = int(cf.get("count","count"))

    print('''
抓取用户作品输入1
抓取用户喜欢作品输入2
    ''')

    choose = int(input('请输入：'))
    if choose == 1:
        choose = 'post'
    else:
        choose = 'like'

    #uid = cf.get("url","url")

    result = get_info(count,choose,cf.get("url","uid"))

    author_list,video_list,aweme_id,nickname,dynamic_cover = video_info(count,result)

    download_all(count,author_list,video_list,aweme_id,nickname,dynamic_cover,choose)