import Util
import random
import requests


class Cookies:
    def __init__(self, conf) -> None:
        self.dyCookie(conf)

    def generate_random_str(self, randomlength=16):
        """
        根据传入长度产生随机字符串
        param :randomlength
        return:random_str
        """
        random_str = ''
        base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789='
        length = len(base_str) - 1
        for _ in range(randomlength):
            random_str += base_str[random.randint(0, length)]
        return random_str

    def generate_ttwid(self) -> str:
        """
        生成请求必带的ttwid
        param :None
        return:ttwid
        """
        url = 'https://ttwid.bytedance.com/ttwid/union/register/'
        data = '{"region":"cn","aid":1768,"needFid":false,"service":"www.ixigua.com","migrate_info":{"ticket":"","source":"node"},"cbUrlProtocol":"https","union":true}'
        response = requests.request("POST", url, data=data)
        # j = ttwid  k = 1%7CfPx9ZM.....
        for j, k in response.cookies.items():
            return k

    def dyCookie(self, conf):
        self.conf = conf
        # self.conf[3] cookie
        if self.conf[3] == '' or 'odin_tt' not in self.conf[3]:
            self.odin_tt = '324fb4ea4a89c0c05827e18a1ed9cf9bf8a17f7705fcc793fec935b637867e2a5a9b8168c885554d029919117a18ba69'
            self.passport_csrf_token = '2f142a9bb5db1f81f249d6fc997fe4a1'
            self.dyheaders = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
                'referer': 'https://www.douyin.com/',
                # 获取用户数据失败就自行替换odin_tt和passport_csrf_token
                'Cookie': f'msToken={self.generate_random_str(107)};ttwid={self.generate_ttwid()};odin_tt={self.odin_tt};passport_csrf_token={self.passport_csrf_token}'
            }
            return self.dyheaders
        else:
            self.dyheaders = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
                'referer': 'https://www.douyin.com/',
                'Cookie': self.conf[3]
            }
            return self.dyheaders


if __name__ == '__main__':
    Cookies()
