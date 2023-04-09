# import os
import time
import execjs
# import sqlite3
import requests

from flask import Flask
from flask import request
from flask import jsonify
# from flask import make_response
# from flask import render_template

from urllib.parse import urlencode
from urllib.parse import unquote
from urllib.parse import parse_qsl

class Server:
    def __init__(self) -> None:
        # 工厂模式
        self.app = Flask(__name__)

        self.app.config.from_mapping(
            SECRET_KEY='douyin-xbogus'
        )

        self.app.config['JSON_AS_ASCII'] = False

        with open("x-bogus.js", "r", encoding="utf-8") as fp:
            self.xbogust_func = execjs.compile(fp.read())

        with open("x-tt-params.js", "r", encoding="utf-8") as fp:
            self.xttm_func = execjs.compile(fp.read())

        self.ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"

    # 获取xg参数
    def getXG(self, url_path, params):
        xbogus = self.xbogust_func.call("getXB", url_path)
        # 字典中添加xg
        params["X-Bogus"] = xbogus
        tips = {
            "status_code": "200",
            "time": {
                "strftime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                "timestamp": int(round(time.time() * 1000))
            },
            "result": [{
                "params": params,
                "paramsencode": urlencode(params, safe="="),
                "user-agent": self.ua,
                "X-Bogus": {
                    0: xbogus,
                    1: "X-Bogus=%s" % xbogus
                }
            }]
        }
        print(tips)
        return jsonify(tips)

    # 生成x-tt-params
    def getxttparams(self, url_path):
        xttp = self.xttm_func.call("getXTTP", url_path)
        tips = {
            "status_code": "200",
            "time": {
                "strftime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                "timestamp": int(round(time.time() * 1000))
            },
            "result": [{
                "headers": {
                    "user-agent": self.ua,
                    "x-tt-params": xttp
                }
            }]
        }
        print(tips)
        return jsonify(tips)


if __name__ == "__main__":
    server = Server()
    # 首页
    @server.app.route('/', methods=['GET', 'POST'])
    def index():
        tips = {
            "status_code": "-1",
            "time": {
                "strftime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                "timestamp": int(round(time.time() * 1000))
            },
            "path": {
                0: "/xg/path/?url=",
                2: "/x-tt-params/path"
            }
        }
        print(tips)
        return jsonify(tips)

    # xg参数
    @server.app.route('/xg/path/', methods=['GET', 'POST'])
    def xgpath():
        path = request.args.get('url', '')
        # 如果str路径为空
        if not path:
            tips = {
                "status_code": "-3",
                "time": {
                    "strftime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                    "timestamp": int(round(time.time() * 1000))
                },
                "message": {
                    0: "The key url cannot be empty and the need for url encoding, The '&' sign needs to be escaped to '%26', Use urllib.parse.quote(url) to escape. Example:/xg/path/?url=aid=6383%26sec_user_id=xxx%26max_cursor=0%26count=10",
                    1: "url参数不能为空，且需要注意传入值中的“&”需要转义成“%26”，使用urllib.parse.quote(url)转义. 例如:/xg/path/?url=aid=6383%26sec_user_id=xxx%26max_cursor=0%26count=10"
                }
            }
            print(tips)
            return jsonify(tips)
        else:
            # url转字典
            params = dict(parse_qsl(path))
            # 字典转url
            url_path = urlencode(params, safe="=")
            return server.getXG(url_path, params)

    # x-tt-params参数
    @server.app.route('/x-tt-params/path', methods=['GET', 'POST'])
    def xttppath():
        try:
            path = request.json
        except:
            pass
        if not path:
            tips = {
                "status_code": "-5",
                "time": {
                    "strftime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                    "timestamp": int(round(time.time() * 1000))
                },
                "message": {
                    0: "Body uses raw JSON format to pass dictionary parameters, such as %s" % '{"aid": 1988,"app_name": "tiktok_web","channel": "tiktok_web".........}',
                    1: "body中使用raw json格式传递字典参数，如%s" % '{"aid": 1988,"app_name": "tiktok_web","channel": "tiktok_web".........}'
                }
            }
            print(tips)
            return jsonify(tips)
        else:
            return server.getxttparams(path)

    # ttwid
    @server.app.route('/xg/ttwid', methods=['GET', 'POST'])
    def gen_ttwid(self) -> str:
        """生成请求必带的ttwid
        param :None
        return:ttwid
        """
        url = 'https://ttwid.bytedance.com/ttwid/union/register/'
        data = '{"region":"cn","aid":1768,"needFid":false,"service":"www.ixigua.com","migrate_info":{"ticket":"","source":"node"},"cbUrlProtocol":"https","union":true}'
        response = requests.request("POST", url, data=data)
        # j = ttwid  k = 1%7CfPx9ZM.....
        for j, k in response.cookies.items():
            tips = {
                "status_code": "200",
                "time": {
                    "strftime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                    "timestamp": int(round(time.time() * 1000))
                },
                "result": [{
                    "headers": {
                        "user-agent": self.ua,
                        "cookie": "ttwid=%s;" % k
                    }
                }]
            }
        print(tips)
        return jsonify(tips)

    server.app.run(host='0.0.0.0',port='8889')
