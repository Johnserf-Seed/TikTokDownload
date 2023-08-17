#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:Login.py
@Date       :2023/08/01 16:29:46
@Author     :JohnserfSeed
@version    :0.0.1
@License    :MIT License
@Github     :https://github.com/johnserf-seed
@Mail       :johnserf-seed@foxmail.com
-------------------------------------------------
Change Log  :
2023/08/01 16:29:46 - 添加登录日志消息映射
-------------------------------------------------
'''

import Util

XB = Util.XBogus()
URLS = Util.Urls()

class Login():

    def __init__(self) -> None:
        # 登录日志消息映射
        self.status_mapping = {
            '1': {"message": '[  登录  ]:等待二维码扫描！\r', "log": Util.log.info},
            '2': {"message": '[  登录  ]:扫描二维码成功！\r', "log": Util.log.info},
            '3': {"message": '[  登录  ]:确认二维码登录！\r', "log": Util.log.info},
            '4': {"message": '[  登录  ]:访问频繁，请检查参数！\r', "log": Util.log.warning},
            '5': {"message": '[  登录  ]:二维码过期，重新获取！\r', "log": Util.log.warning}
        }

        self.verifyFp = ''

        self.loginHeaders = {
            'Cookie': f'ttwid={Util.Cookies().generate_ttwid()}',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183',
            'Referer':'https://www.douyin.com/'
        }

        # 初始化默认调用登录二维码
        self.get_qrcode()


    def get_qrcode(self) -> str:
        """
        获取登录二维码

        Raises:
            RuntimeError: 网络异常: 获取二维码失败

        Returns:
            str: token
        """

        verifyFp = Util.Cookies().get_fp()
        self.verifyFp = verifyFp

        params = XB.getXBogus(f'service=https%3A%2F%2Fwww.douyin.com&need_logo=false&need_short_url=true&device_platform=web_app&aid=6383&account_sdk_source=sso&sdk_version=2.2.5&language=zh&verifyFp={self.verifyFp}&fp={self.verifyFp}')
        domain = URLS.SSO_LOGIN_GET_QR

        try:
            response = Util.requests.get(domain + params[0], headers=self.loginHeaders)
            response.raise_for_status()
            data = response.json()
            qrcode_url  = data.get('data', {}).get('qrcode_index_url', '')
            token = data.get('data', {}).get('token', '')
            self.show_qrcode(qrcode_url)
            self.check_qrconnect(token)
        except Util.requests.exceptions.RequestException as e:
            if response:
                error_message = f"网络异常: 获取二维码失败。 状态码: {response.status_code}, 响应体: {response.text}, 异常: {e}"
            else:
                error_message = f"网络异常: 获取二维码失败。 无法连接到服务器。 异常: {e}"
            Util.log.error(error_message)
            raise RuntimeError(error_message) from e


    def check_qrconnect(self, token) -> bool:
        """
        检查二维码状态

        Args:
            token (str): 登录二维码token

        Raises:
            RuntimeError: 网络异常: 检查二维码连接失败

        Return:
            bool: 是否登录成功
        """

        params = XB.getXBogus(f'token={token}&service=https%3A%2F%2Fwww.douyin.com&need_logo=false&need_short_url=true&device_platform=web_app&aid=6383&account_sdk_source=sso&sdk_version=2.2.5&language=zh&verifyFp={self.verifyFp}&fp={self.verifyFp}')
        domain = URLS.SSO_LOGIN_CHECK_QR

        try:
            while True:
                response = Util.requests.get(domain + params[0], headers=self.loginHeaders)
                response.raise_for_status()
                data = response.json().get('data', {})
                status = data.get('status', '')
                match status:
                    case '1':
                        self.log_and_print('1')
                    case '2':
                        self.log_and_print('2')
                    case '3':
                        self.log_and_print('3')
                        redirect_url = data.get('redirect_url', '')
                        login_cookies = Util.Cookies().split_cookies(response.headers.get('set-cookie', ''))
                        return self.login_redirect(redirect_url, login_cookies)
                    case '4':
                        self.log_and_print('4')
                    case '5':
                        self.log_and_print('5')
                        self.get_qrcode()
                        break

                Util.time.sleep(3)
        except Util.requests.exceptions.RequestException as e:
            if response:
                error_message = f"网络异常: 检查二维码扫码状态失败。 状态码: {response.status_code}, 响应体: {response.text}, 异常: {e}"
            else:
                error_message = f"网络异常: 获取二维码失败。 无法连接到服务器。 异常: {e}"
            Util.log.error(error_message)
            raise RuntimeError(error_message) from e


    def login_redirect(self, redirect_url, cookie) -> bool:
        """
        登录重定向

        Args:
            redirect_url (str): 重定向链接
            cookie (str): 登录时的Cookie值
        """

        self.loginHeaders['Cookie'] = cookie
        login_response = Util.requests.get(redirect_url, headers=self.loginHeaders)

        if login_response.history[0].status_code == 302:
            # 获取重定向链接中的Cookie并更新
            self.loginHeaders['Cookie'] = Util.Cookies().split_cookies(login_response.history[1].headers.get('set-cookie', ''))
            # 绑定XB算法的UA
            self.loginHeaders['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
            # 写入配置文件
            Util.Config().save(self.loginHeaders['Cookie'])
            Util.progress.console.print('[  登录  ]:重定向登录成功\r')
            Util.log.info('[  登录  ]:重定向登录成功')
            return True
        else:
            Util.progress.console.print('[  登录  ]:重定向登录失败\r')
            if login_response:
                error_message = f"网络异常: 重定向登录失败。 状态码: {login_response.status_code}, 响应体: {login_response.text}"
            else:
                error_message = f"网络异常: 重定向登录失败。 无法连接到服务器。"
            Util.log.warning(error_message)
            return False


    def show_qrcode(self, qrcode_url) -> None:
        """
        显示二维码

        Args:
            qrcode_url (str): 登录二维码链接
        """

        # # 创建QR码图像
        # qr_code_img = Util.qrcode.make(qrcode_url)

        # # 显示QR码图像
        # qr_code_img.show()

        qr = Util.qrcode.QRCode()

        # 添加数据
        qr.add_data(qrcode_url)

        # 生成二维码
        qr.make(fit=True)

        # 在控制台以 ASCII 形式打印二维码
        qr.print_ascii(invert=True)

        Util.progress.console.print("[  登录  ]:请扫描登录二维码。\r")
        Util.log.info("[  登录  ]:请扫描登录二维码。")


    def log_and_print(self, status):
        """
        输出日志和控制台消息

        Args:
            status (str): 根据status来查找错误信息
        """
        data = self.status_mapping.get(status, {})
        message = data.get("message", "")
        log_func = data.get("log", Util.log.info)
        Util.progress.console.print(message)
        log_func(message)
