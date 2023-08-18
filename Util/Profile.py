#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:Profile.py
@Date       :2022/08/11 23:13:22
@Author     :JohnserfSeed
@version    :1.0
@License    :MIT License
@Github     :https://github.com/johnserf-seed
@Mail       :johnserfseed@gmail.com
-------------------------------------------------
Change Log  :
2022/08/11 23:13:22 : Init
2023/08/17 17:46:08 : Fixes where downloads would be skipped when has_more was 0.
2023/08/17 17:46:08 : Added a signal that can interrupt the download.
-------------------------------------------------
'''

import Util



XB = Util.XBogus()
URLS = Util.Urls()


class Profile:

    def __init__(self, config, dyheaders):
        # 抓获所有视频
        self.Isend = False
        # 第一次访问页码
        self.max_cursor = 0
        # 全局IOS头部
        self.headers = dyheaders
        # 配置文件
        self.config = config
        # 记录配置文件
        Util.log.info(f"配置文件：{config}")
        # 昵称映射表
        self.nick_mapper = Util.NickMapper('nickname_mapping.db')
        # 连接数据库
        self.nick_mapper.connect()
        # 创建下载实例
        self.download = Util.Download(self.config)

    def create_user_folder(self, config: dict, nickname: Util.Union[str, int]) -> None:
        """
        根据提供的配置文件和昵称，创建对应的保存目录。
        如果未在配置文件中指定路径，则默认为 "Download"。
        仅支持相对路径。

        Args:
            config (dict): 配置文件，字典格式。
            nickname (Union[str, int]): 用户的昵称，允许字符串或整数。
        Raises:
            TypeError: 如果 config 不是字典格式，将引发 TypeError。
        """

        # 确定函数参数是否正确
        if not isinstance(config, dict):
            raise TypeError("config 参数必须是字典。")

        # 获取相对路径
        path = Util.os.path.join(".", config.get('path', 'Download'), config['mode'], nickname)

        # 获取绝对路径
        path = Util.os.path.abspath(path)
        if not Util.os.path.exists(path):
            # 创建用户文件夹
            Util.os.makedirs(path)

        return path

    async def re_match(self, session: Util.aiohttp.ClientSession, inputs: str) -> Util.Optional[Util.re.Match]:
        """
        根据传入的url，正则匹配sec_user_id

        Args:
            session (aiohttp.ClientSession): HTTP session
            inputs (str): 单条url
        Return:
            match (re.Match): 匹配到的结果
        """

        match = None

        async with session.get(url=Util.reFind(inputs),
                                timeout=10,
                                allow_redirects=True) as response:
            # 检查响应状态码，如果不是200和444，会抛出异常
            if response.status in {200, 444}:
                if 'v.douyin.com' in inputs:
                    pattern = r"sec_uid=([^&]*)"
                    match = Util.re.search(pattern, response.url.path_qs)
                else:
                    pattern = r"user/([^/?]*)"
                    match = Util.re.search(pattern, response.url.path_qs)

        return match

    async def get_request_data(self, method: str, url: str, headers: dict, data: dict = None):
        """
        发送异步HTTP请求并获取返回的接口数据

        Args:
            method (str): HTTP请求的方法，如'GET', 'POST'等
            url (str): 需要发送请求的URL
            headers (dict): HTTP请求的头部
            data (dict, optional): 如果请求方法为'GET'，需要发送的数据。默认为None。

        Returns:
            Tuple[List[dict], int, bool]: 返回一个元组，包含三个元素：
                                        1. 一个字典列表，每个字典代表一页作品信息
                                        2. 一个整数，表示下次请求的页码
                                        3. 一个布尔值，表示是否有更多作品
        """

        async with Util.aiohttp.ClientSession() as session:
            async with session.request(method, url, headers=headers, data=data, timeout=10) as response:
                if response.status == 200:
                    if response.text != '':
                        api_data = await response.json()
                        info_status_code = api_data.get("status_code", None)
                        # 确保接口返回数据正常
                        if info_status_code == 0:
                            # 接口相关(逆天，收藏接口完全不一样)
                            if method == "POST":
                                max_cursor = api_data.get("cursor", 0)
                            else:
                                max_cursor = api_data.get("max_cursor", 0)
                            has_more = api_data.get("has_more")
                            aweme_list = api_data.get("aweme_list", [])
                            return aweme_list, max_cursor, has_more
                        else:
                            raise RuntimeError(f"接口返回异常: status_code={info_status_code}")
                    else:
                        raise RuntimeError('获取接口数据失败，请从删除配置文件中的cookie，重新扫码登录并检查是否触发人机验证\r')
                else:
                    raise Util.aiohttp.ClientError(f'本地网络错误 status_code={response.status}')

    async def get_all_sec_user_id(self, inputs: Util.Union[str, list]) -> Util.Union[str, list]:
        """
        获取用户SECUID，传入单条url或者列表url都可以解析出sec_user_id。

        Args:
            inputs (Union[str, list]): 单条url或者列表url
        Return:
            sec_user_id (Union[str, list]): 用户的唯一标识，返回字符串或列表
        """

        # 进行参数检查
        if not isinstance(inputs, (str, list)):
            raise TypeError("输入参数必须是字符串或列表。")

        # 从字符串提取
        if isinstance(inputs, str):
            try:
                async with Util.aiohttp.ClientSession() as session:
                    match = await self.re_match(session, inputs)
                    if match:
                        return match.group(1)
                    else:
                        raise ValueError("链接错误,无法提取用户ID.")
            except Util.aiohttp.ClientError as e:
                raise RuntimeError(f"网络连接异常，异常：{e}")

        # 从列表提取
        elif isinstance(inputs, list):
            try:
                # 处理列表
                sec_user_id_list = []
                async with Util.aiohttp.ClientSession() as session:
                    tasks = []
                    for url in inputs:
                        task = Util.asyncio.ensure_future(self.re_match(session, url))
                        tasks.append(task)
                    responses = await Util.asyncio.gather(*tasks)
                    for match in responses:
                        if match:
                            sec_user_id_list.append(match.group(1))
                        else:
                            raise ValueError("链接错误,无法提取用户ID.")
            except ValueError:
                raise ValueError("列表url非字符串。")
            except Util.aiohttp.ClientError as e:
                raise RuntimeError(f"网络连接异常，异常：{e}")

        return sec_user_id_list

    async def get_diff_type_url(self, config: dict, sec_user_id: Util.Union[str, None], count = 20, cursor = 0) -> str:
        """
        根据传入配置文件中的mode和用户sec_user_id,生成不同作品类型的接口链接。

        Args:
            config (dict): 字典配置文件
            sec_user_id (str): 用户唯一标识
            count (int): 作品数
            cursor (long): 作品页码
        Return:
            domain + params[0] (str): 拼接接口链接
        """

        # 确定函数参数是否正确
        if not isinstance(config, dict):
            raise TypeError("config 参数必须是字典.")
        if not isinstance(sec_user_id, str):
            raise TypeError("sec_user_id 参数必须是字符串.")

        # 生成接口链接,收藏夹的接口麻烦点的
        mode = config.get('mode', 'post').lower()
        if mode == "post" and sec_user_id is not None:
            params = XB.getXBogus(f'aid=6383&sec_user_id={sec_user_id}&count={count}&max_cursor={cursor}&cookie_enabled=true&platform=PC&downlink=10')
            domain = URLS.USER_POST
            self.type_data = None
        elif mode == "like" and sec_user_id is not None:
            params = XB.getXBogus(f'aid=6383&sec_user_id={sec_user_id}&count={count}&max_cursor={cursor}&cookie_enabled=true&platform=PC&downlink=10')
            domain = URLS.USER_FAVORITE_A
            self.type_data = None
        elif mode == "listcollection":
            params = XB.getXBogus(f'aid=6383&cookie_enabled=true&platform=PC&downlink=1.5')
            domain = URLS.USER_COLLECTION
            self.type_data = f'count={count}&cursor={cursor}'

        return domain + params[0]

    async def get_user_base_info(self, headers: dict, sec_user_id: Util.Union[str, list]) -> dict:
        """
        根据 sec_user_id 来获取用户im基本数据

        Args:
            headers (dict): 包含 Cookie、User-Agent、Referer 等请求头信息
            sec_user_id (Union[str, list]): 用户的唯一标识，可以是字符串或列表
        Return:
            data (dict): 返回该用户的基本信息
        """

        # 确定函数参数是否正确
        if not isinstance(headers, dict):
            raise TypeError("headers 参数必须是字典.")
        if not isinstance(sec_user_id, (str, list)):
            raise TypeError("sec_user_id 参数必须是字符串或列表.")

        params = XB.getXBogus("aid=6383&platform=PC&downlink=1.25")
        domain = URLS.USER_SHORT_INFO

        # 该接口的参数是列表
        if isinstance(sec_user_id, str):
            sec_user_id_json = Util.json.dumps([sec_user_id])
        else:
            sec_user_id_json = Util.json.dumps(sec_user_id)

        request_data = 'sec_user_ids=%s' % Util.parse.quote(str(sec_user_id_json))
        data = {}

        try:
            async with Util.aiohttp.ClientSession() as session:
                async with session.get(url=domain + params[0],
                                        headers=headers,
                                        data=request_data,
                                        proxy=None, timeout=10) as response:
                    if response.status == 200:
                        data = await response.json()
                        info_status_code = data.get("status_code", None)
                        # 确保接口返回数据正常
                        """
                        info_status_code == 0 说明接口返回正常
                        info_status_code == 5 说明接口参数异常
                        info_status_code == 8 说明用户未登录
                        """
                        if info_status_code == 0:
                            data = data.get("data", {})
                        else:
                            raise RuntimeError(f"接口返回异常: {info_status_code}")
        except Util.aiohttp.ClientError as e:
            raise RuntimeError(f"请求异常: {str(e)}")

        return data

    async def get_user_profile_info(self, headers: dict, sec_user_id: str) -> dict:
        """
        根据 sec_user_id 来获取用户完整信息

        Args:
            headers (dict): 包含 Cookie、User-Agent、Referer 等请求头信息
            sec_user_id (str): 用户的唯一标识，可以是字符串或列表
        Return:
            data (dict): 返回该用户的完整信息
        """

        # 确定函数参数是否正确
        if not isinstance(headers, dict):
            raise TypeError("headers 参数必须是字典.")
        if not isinstance(sec_user_id, str):
            raise TypeError("sec_user_id 参数必须是字符串.")

        params = XB.getXBogus(f"device_platform=webapp&aid=6383&sec_user_id={sec_user_id}&cookie_enabled=true&platform=PC&downlink=10")
        domain = URLS.USER_DETAIL

        data = {}

        try:
            async with Util.aiohttp.ClientSession() as session:
                async with session.get(url=domain + params[0],
                                        headers=headers,
                                        proxy=None, timeout=10) as response:
                    if response.status == 200:
                        if response.text != '':
                            data = await response.json()
                            info_status_code = data.get("status_code", None)
                            # 确保接口返回数据正常
                            if info_status_code == 0:
                                data = data.get("user", {})
                            else:
                                raise RuntimeError(f"接口内容返回异常: status_code={info_status_code}")
                        else:
                            raise RuntimeError("接口返回空，检查cookie是否过期以及是否出现人机验证，解决不了请重新扫码登录\r")
                    else:
                        raise RuntimeError(f"请检查网络状况。 状态码: {response.status}, 响应体: {response.text}")
        except Util.aiohttp.ClientError as e:
            raise RuntimeError(f"本地网络请求异常。 异常: {e}\r") from e

        return data

    async def get_user_post_info(self, headers: dict, url: str) -> dict:
        """
        获取指定用户的作品信息

        Args:
            headers (dict): HTTP请求的头部
            url (str): 需要发送请求的URL

        Returns:
            List[dict]: 返回一个字典列表，每个字典包含一个作品的所有信息，如作品类型，作品ID，作品描述，作者信息，音乐信息等
        """

        aweme_data = []

        try:
            if self.config['mode'] != 'listcollection':
                aweme_list, max_cursor, has_more = await self.get_request_data('GET', url, headers)
            else:
                headers['Content-Type'] = 'application/x-www-form-urlencoded'
                aweme_list, max_cursor, has_more = await self.get_request_data('POST', url, headers, self.type_data)
        except Util.aiohttp.ClientError as e:
            raise RuntimeError(f"本地请求异常, 异常: {e}") from e
        except Exception as e:
            raise RuntimeError(f"运行异常, 异常: {e}") from e

        if aweme_list == []:
            data = {}
            # 作品相关
            data['max_cursor'] = max_cursor
            data['has_more'] = has_more
            aweme_data.append(data)
        else:
            for item in aweme_list:
                data = {}
                # 类别相关
                author = item.get("author", {})
                music = item.get("music", {})
                video = item.get("video", {})
                aweme_type = item.get("aweme_type", None)

                if aweme_type == 0:
                    # 视频相关
                    bit_rate = video.get("bit_rate", [])
                    # 封面相关
                    cover = video.get("cover", {})
                    dynamic_cover = video.get("dynamic_cover", {})
                    try:
                        data['video_uri'] = bit_rate[0].get("play_addr", {}).get("uri", None)
                        data['video_url_list'] = bit_rate[0].get("play_addr", {}).get("url_list", [])
                        data['cover'] = cover.get("url_list",[])
                        data['dynamic_cover'] = dynamic_cover.get("url_list",[])
                    except IndexError:
                        # raise RuntimeError("该视频已被下架，无法下载。")
                        continue

                elif aweme_type == 68:
                    # 图集相关
                    data['images'] = item.get("images", [])
                    data['cover'] = ''
                    data['dynamic_cover'] = ''

                # 作品相关
                data['max_cursor'] = max_cursor
                data['has_more'] = has_more
                data['aweme_type'] = aweme_type
                data['aweme_id'] = item.get("aweme_id", None)
                data['desc'] = Util.replaceT(item.get("desc", None))
                # 将UNIX时间戳转换为格式化的字符串
                data['create_time'] = Util.time.strftime('%Y-%m-%d %H.%M.%S', Util.time.localtime(item.get("create_time", None)))

                # 作者相关
                data['uid'] = author.get("uid", None)
                # 判断昵称映射表中是否已经存在该用户
                if self.nick_mapper.get_nickname(author['sec_uid']) is None:
                    # 如果不存在，添加昵称映射
                    self.nick_mapper.add_mapping(author['sec_uid'], author['nickname'])
                    # 关闭索引
                    # self.nick_mapper.close()
                # 获取昵称映射
                data['nickname'] = self.nick_mapper.get_nickname(author['sec_uid'])
                data['aweme_count'] = author.get("aweme_count", None)

                # 原声相关
                data['music_title'] = music.get("title", None)
                data['music_play_url'] = music.get("play_url", None)

                # 保存路径相关
                data['path'] = self.path

                aweme_data.append(data)

        return aweme_data

    async def process_aweme_data(self, aweme_data):
        """
        处理 aweme_data，执行下载等操作。

        Args:
            aweme_data
        """
        if 'aweme_id' not in aweme_data[0]:
            # 如果数据为空，直接返回
            Util.progress.console.print(f'[  提示  ]:抓获{self.max_cursor}页数据为空，已跳过。\r')
            Util.log.info(f'[  提示  ]:抓获{self.max_cursor}页数据为空，已跳过。')
            return
        # 下载作品
        with Util.progress:
            await self.download.AwemeDownload(aweme_data)
        Util.progress.console.print(f'[  提示  ]:抓获{self.max_cursor}页数据成功! 该页共{len(aweme_data)}个作品。\r')
        Util.log.info(f'[  提示  ]:抓获{self.max_cursor}页数据成功! 该页共{len(aweme_data)}个作品。')

    async def get_Profile(self, count: int = 20) -> None:
        """
        获取用户的Profile并设置相应的实例变量。

        首先获取用户的唯一标识和昵称，然后根据 mode 和其他配置来生成 profile_URL，并创建用户的文件夹。
        如果 mode 是 'listcollection'，则 params 将不包含 sec_user_id，否则包含 sec_user_id。
        生成的 profile_URL 将用于后续的数据获取，最后保存用户的主页链接。

        Raises:
            Exception: 如果在获取用户信息过程中出现错误，则会抛出异常。
        """

        try:
            # 获取sec_user_id
            self.sec_user_id = await self.get_all_sec_user_id(inputs=self.config['uid'])

            # 用户详细信息
            user_profile_info = await self.get_user_profile_info(self.headers, self.sec_user_id)

            # 用户昵称,需要替换非法字符防止因为昵称字符问题导致报错,api参考API目录
            self.nickname = Util.replaceT(user_profile_info.get("nickname"))
            # 判断昵称映射表中是否已经存在该用户
            if self.nick_mapper.get_nickname(self.sec_user_id) is None:
                # 如果不存在，添加昵称映射
                self.nick_mapper.add_mapping(self.sec_user_id, self.nickname)
            # 根据映射表中的唯一标识获取用户的昵称，即使用户修改昵称也不会影响文件目录
            self.nickname = self.nick_mapper.get_nickname(self.sec_user_id)
            Util.progress.console.print(f'[  用户  ]:用户的昵称：{self.nickname}，用户唯一标识：{self.sec_user_id}')
            Util.log.info(f'[  用户  ]:用户的昵称：{self.nickname}，用户唯一标识：{self.sec_user_id}')

            # 用户初始接口URL生成
            self.profile_URL = await self.get_diff_type_url(self.config, self.sec_user_id, count, 0)

            # 创建用户文件夹
            self.path = self.create_user_folder(self.config, self.nickname)

            # 保存用户主页链接
            with open(Util.os.path.join(self.path,
                                        self.nickname + '.txt'),
                                        'w') as f:
                f.write(f"https://www.douyin.com/user/{self.sec_user_id}")

            Util.progress.console.print('[  提示  ]:批量获取所有视频中!\r')
            Util.log.info('[  提示  ]:批量获取所有视频中!')

            aweme_data = await self.get_user_post_info(self.headers, self.profile_URL)
            self.has_more = aweme_data[0].get("has_more")
            self.max_cursor = aweme_data[0].get("max_cursor")
            Util.progress.console.print(f'[  提示  ]:抓获首页数据成功! 该页共{len(aweme_data)}个作品。\r')
            Util.log.info(f'[  提示  ]:抓获首页数据成功! 该页共{len(aweme_data)}个作品。')

            while True:
                if Util.done_event.is_set():
                    Util.progress.console.print("[  提示  ]: 中断本次下载")
                    return

                # 首先处理当前的 aweme_data
                await self.process_aweme_data(aweme_data)

                # 检查是否有更多作品需要请求
                if self.has_more == 0:
                    break

                # 如果有更多作品，则更新URL并请求新的数据
                self.profile_URL = await self.get_diff_type_url(self.config,
                                                                self.sec_user_id,
                                                                count,
                                                                self.max_cursor)
                aweme_data = await self.get_user_post_info(self.headers, self.profile_URL)
                self.has_more = aweme_data[0].get("has_more")
                self.max_cursor = aweme_data[0].get("max_cursor")
        except Exception as e:
            Util.progress.console.print(f'[  提示  ]:异常，{e}')
            Util.log.error(f'[  提示  ]:异常，{e}，{Util.traceback.format_exc()}')
            input('[  提示  ]：按任意键退出程序!\r')
            exit(0)
