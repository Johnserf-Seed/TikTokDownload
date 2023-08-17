#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:Download.py
@Date       :2022/08/11 22:02:49
@Author     :JohnserfSeed
@version    :1.0
@License    :MIT License
@Github     :https://github.com/johnserf-seed
@Mail       :johnserfseed@gmail.com
-------------------------------------------------
Change Log  :
2022/08/11 22:02:49 : Init
2022/08/30 00:30:09 : Add ImageDownload()
2023/08/04 00:48:30 : Add trim_filename(),download_file(),AwemeDownload() and Delete some unuseful function
-------------------------------------------------
'''

import Util

XB = Util.XBogus()
URLS = Util.Urls()

class Download:

    def __init__(self, config):
        # 配置文件
        self.config = config
        # 文件检查是否存在
        self.check = Util.Check()
        # 异步的任务数
        self.semaphore = Util.asyncio.Semaphore(int(self.config['max_tasks']))

    def trim_filename(self, filename: str, max_length: int = 50) -> str:
        """
        裁剪文件名以适应控制台显示。

        Args:
            filename (str): 完整的文件名。
            max_length (int): 显示的最大字符数。

        Returns:
            str: 裁剪后的文件名。
        """

        if len(filename) > max_length:
            prefix_suffix_len = max_length // 2 - 2  # 确保前缀和后缀长度相等，并且在中间留有四个字符用于省略号（"..."）
            return f"{filename[:prefix_suffix_len]}...{filename[-prefix_suffix_len:]}"
        else:
            return filename

    async def download_file(self, task_id: Util.TaskID, url: str, path: str) -> None:
        """
        下载指定 URL 的文件并将其保存在本地路径。

        Args:
            task_id (TaskID): 下载任务的唯一标识。
            url (str): 要下载的文件的 URL。
            path (str): 文件保存的本地路径.
        """
        try:
            async with self.semaphore:
                connector = Util.aiohttp.TCPConnector(limit=int(self.config['max_connections']))

                async with Util.aiohttp.ClientSession(connector=connector) as session:
                    async with session.get(url) as response:
                        if response.status != 200:
                            raise ValueError(f"HTTP连接意外: {response.status}")

                        Util.progress.update(task_id, total=int(response.headers["Content-length"]))
                        with open(path, "wb") as dest_file:
                            Util.progress.start_task(task_id)
                            chunk_size = 32768
                            while not Util.done_event.is_set():
                                chunk = await response.content.read(chunk_size)
                                if not chunk:
                                    break
                                dest_file.write(chunk)
                                Util.progress.update(task_id, advance=len(chunk))

        except Util.aiohttp.ClientError as e:
            Util.progress.console.print(f"[  失败  ]：网络连接出错。异常：{e}")
        except ValueError as e:
            Util.progress.print(f"[  失败  ]：该链接可能无法访问。 异常：{e}")
        except FileNotFoundError:
            Util.progress.print(f"[  失败  ]：文件路径 {path} 无效或无法访问。")
        except Exception as e:
            Util.progress.print(f"[  失败  ]：下载失败，未知错误。异常：{e}")

    async def AwemeDownload(self, aweme_data):
        """
        此函数用于从抖音作品数据列表（aweme_data）中异步下载音乐、视频和图集。
        它会根据aweme_type的类型来决定是下载视频还是图集，并且会根据配置文件来判断是否需要下载音乐。
        下载的文件会保存在用户目录下，并且会创建一个与抖音作品文案对应的子目录。
        如果文件已经存在，作品将不会重新下载。

        文件的命名规范：
        file_name: 文件名：ctime_f +  desc + 文件类型。 例如'2021-02-15 18.09.05测试.mp4'，用于控制台显示。
        file_path: 绝对路径的文件名：绝对路径 + ctime_f和作品同名目录 +  file_name。例如'H:\\TikTokDownload\\Download\\post\\小e同学\\2021-02-15 18.09.05测试\\2021-02-15 18.09.05测试.mp4'，用于文件保存。
        作品文件夹的命名规范: ctime_f和作品同名目录。例如 2021-02-15 18.09.05测试

        Args:
            aweme_data (list): 抖音数据列表，列表的每个元素都是一个字典，字典包含了抖音的各种信息，如aweme_type, path, desc等。
        """

        async def format_file_name(aweme: list, naming_template: str) -> str:
            """
            根据配置文件的全局格式化文件名。

            Args:
            - aweme (dict): 抖音数据的字典。
            - naming_template (str): 文件的命名模板，如 "{create}_{desc}"。

            Returns:
            - str: 格式化的文件名。
            """

            # 使用给定的命名模板格式化文件名
            return naming_template.format(create=aweme['create_time'], desc=aweme['desc'], id=aweme['aweme_id'])

        async def initiate_desc(file_type: str, desc_content: str, file_suffix: str, base_path: str, file_name: str) -> None:
            """
            初始化文案保存。如果文案文件已经存在，则跳过保存。否则，直接将文案内容写入文件。

            Args:
                file_type (str): 文件类型描述，通常是"文案"。
                desc_content (str): 要保存的文案内容。
                base_path (str): 文案文件保存的基础目录路径。
                file_name (str): 文案文件的主要名称，不包含后缀。

            Note:
                这个函数会检查文案文件是否已经在指定的路径存在。如果存在，跳过该任务。否则，将直接将文案内容写入文件。
            """

            file_path = f'{file_name}{file_suffix}'
            full_path = Util.os.path.join(base_path, file_path)
            if Util.os.path.exists(full_path):
                task_id = Util.progress.add_task(description=f"[  跳过  ]:",
                                                filename=self.trim_filename(file_path, 50),
                                                total=1, completed=1)
                Util.progress.update(task_id, completed=1)
            else:
                task_id = Util.progress.add_task(description=f"[  {file_type}  ]:",
                                                filename=self.trim_filename(file_path, 50),
                                                start=False)
                Util.progress.start_task(task_id)
                with open(full_path, 'w', encoding='utf-8') as desc_file:
                    desc_file.write(desc_content)
                # 更新进度条以显示任务完成
                Util.progress.update(task_id, completed=100)

        # 用于存储作者本页所有的下载任务, 最后会等待本页所有作品下载完成才结束本函数
        download_tasks = []

        # 遍历aweme_data中的每一个aweme字典
        for aweme in aweme_data:
            # 将UNIX时间戳转换为格式化的字符串
            ctime_f = Util.time.strftime('%Y-%m-%d %H.%M.%S', Util.time.localtime((aweme['create_time'])))
            # 如果设置了事件响应，则停止
            if Util.done_event.is_set():
                Util.progress.console.print("[  提示  ]: 中断该页下载")
                return

            # 获取文件的基础路径，这里的aweme['path']是到用户目录的绝对路径
            base_path = aweme['path']
            # 创建子目录名称
            subdir_name = f'{ctime_f}_{aweme["desc"]}'
            # 根据视频描述创建子目录
            desc_path = Util.os.path.join(base_path, subdir_name)
            # 确保子目录存在，如果不存在，os.makedirs会自动创建
            Util.os.makedirs(desc_path, exist_ok=True)

            # 如果配置文件设置为下载音乐
            if self.config['music'].lower() == 'yes':
                try:
                    # 尝试获取音乐的URL
                    music_url = aweme['music_play_url']['url_list'][0]
                    # 创建音乐文件名
                    music_file_name = f'{ctime_f}_{aweme["desc"]}_music'
                    # 创建相对路径的文件名
                    music_file_path = f'{music_file_name}.mp3'
                    # 创建绝对路径的文件名
                    music_full_path = Util.os.path.join(desc_path, music_file_path)
                    # 检查音乐文件是否已经存在
                    music_state = Util.os.path.exists(music_full_path)
                    # 如果音乐文件存在，则创建一个已完成的任务
                    if music_state:
                        task_id = self.progress.add_task(description="[  跳过  ]:",
                                                        filename=self.trim_filename(music_file_path, 50),
                                                        total=1, completed=1)
                        Util.log.info(f"repeat task created with ID: {task_id}")
                        self.progress.update(task_id, completed=1)
                    else:
                        # 如果音乐文件不存在，则创建一个新的下载任务
                        task_id = self.progress.add_task(description="[  音乐  ]:",
                                                        filename=self.trim_filename(music_file_path, 50),
                                                        start=False)
                        Util.log.info(f"New task created with ID: {task_id}")
                        download_task = Util.asyncio.create_task(self.download_file(task_id, music_url, music_full_path))
                        # 将任务添加到任务列表中
                        download_tasks.append(download_task) 
                except IndexError:
                    # 如果无法提取音乐URL，则跳过下载该音乐
                    pass

            # 根据aweme的类型下载视频或图集
            if aweme['aweme_type'] == 0:  # 如果aweme类型为0，下载视频
                    await initiate_download("音乐", music_url, ".mp3", desc_path, music_name)
                    Util.progress.console.print("[  失败  ]：该原声不可用，无法下载。")
                    Util.log.warning(f"[  失败  ]：该原声不可用，无法下载。{aweme} 异常：{Exception}")
                try:
                    # 获取视频的URL
                    video_url = aweme['video_url_list'][0]
                    # 创建视频文件名
                    video_file_name = f'{ctime_f}_{aweme["desc"]}_video'
                    # 创建相对路径的文件名
                    video_file_path = f'{video_file_name}.mp4'
                    # 创建绝对路径的文件名
                    video_full_path = Util.os.path.join(desc_path, video_file_path)
                    # 检查视频文件是否已经存在
                    video_state = Util.os.path.exists(video_full_path)
                    # 如果视频文件存在，则创建一个已完成的任务
                    if video_state:
                        task_id = self.progress.add_task(description="[  跳过  ]:",
                                                        filename=self.trim_filename(video_file_path, 50),
                                                        total=1, completed=1)
                        Util.log.info(f"repeat task created with ID: {task_id}")
                        self.progress.update(task_id, completed=1)
                    # 如果视频文件不存在，则创建一个新的下载任务
                    else:
                        task_id = self.progress.add_task(description="[  视频  ]:",
                                                        filename=self.trim_filename(video_file_path, 50),
                                                        start=False)
                        Util.log.info(f"New task created with ID: {task_id}")
                        download_task = Util.asyncio.create_task(self.download_file(task_id, video_url, video_full_path))
                        # 将任务添加到任务列表中
                        download_tasks.append(download_task) 
                except IndexError:
                    # 如果无法提取视频URL，则跳过下载该音乐
                    pass

            elif aweme['aweme_type'] == 68:  # 如果aweme类型为68，下载图集
                    await initiate_download("视频", video_url, ".mp4", desc_path, video_name)
                        await initiate_download("封面", cover_url, ".gif", desc_path, cover_name)
                        Util.progress.console.print(f"[  失败  ]:该视频封面不可用，无法下载。")
                        Util.log.warning(f"[  失败  ]:该视频封面不可用，无法下载。{aweme} 异常：{Exception}")
                try:
                    for i, image_dict in enumerate(aweme['images']):
                        # 提取每个图集的 url_list 的第一项
                        image_url = image_dict.get('url_list', [None])[0]
                        # 创建图片文件名
                        image_file_name = f'{ctime_f}_{aweme["desc"]}_image_{i + 1}'
                        # 创建相对路径的文件名
                        image_file_path = f'{image_file_name}.jpg'
                        # 创建绝对路径的文件名
                        image_full_path = Util.os.path.join(desc_path, image_file_path)
                        # 检查图片文件是否已经存在
                        image_state = Util.os.path.exists(image_full_path)
                        # 如果图片文件存在，则创建一个已完成的任务
                        if image_state:
                            task_id = self.progress.add_task(description="[  跳过  ]:",
                                                            filename=self.trim_filename(image_file_path, 50),
                                                            total=1, completed=1)
                            Util.log.info(f"repeat task created with ID: {task_id}")
                            self.progress.update(task_id, completed=1)
                        # 如果图片文件不存在，则创建一个新的下载任务
                        else:
                            task_id = self.progress.add_task(description="[  图集  ]:",
                                                            filename=self.trim_filename(image_file_path, 50),
                                                            start=False)
                            Util.log.info(f"New task created with ID: {task_id}")
                            download_task = Util.asyncio.create_task(self.download_file(task_id, image_url, image_full_path))
                            # 将任务添加到任务列表中
                            download_tasks.append(download_task) 
                except IndexError:
                    # 如果无法提取图集URL，则跳过下载该音乐
                    pass
                        await initiate_download("图集", image_url, ".jpg", desc_path, image_name)
            # 文案保存
            if self.config['desc'].lower() == 'yes':
                try:
                    desc_name = f"{await format_file_name(aweme, self.config['naming'])}_desc"
                    await initiate_desc("文案", aweme['desc'], ".txt", desc_path, desc_name)
                except Exception:
                    Util.progress.console.print(f"[  失败  ]:保存文案失败。异常：{Exception}")
                    Util.log.warning(f"[  失败  ]:保存文案失败。{aweme} 异常：{Exception}")

        # 等待本页所有的下载任务完成, 如果不等待的话就会还没等下完就去下载下一页了, 并发下载多了会被服务器断开连接
        await Util.asyncio.gather(*download_tasks)
