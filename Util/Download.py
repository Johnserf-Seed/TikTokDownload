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

        async def initiate_download(file_type: str, file_url: str, file_suffix: str, base_path: str, file_name: str) -> None:
            """
            初始化下载任务。如果文件已经存在，则跳过下载。否则，创建一个新的异步下载任务。

            Args:
                file_type (str): 文件类型描述，如“音乐”、“视频”或“封面”。
                file_url (str): 要下载的文件的URL。
                file_suffix (str): 文件的后缀名，如“.mp3”或“.mp4”。
                base_path (str): 文件保存的基础目录路径。
                file_name (str): 文件的主要名称，不包含后缀。

            Note:
                这个函数会检查文件是否已经在指定的路径存在。如果存在，跳过该任务。否则，将创建一个新的下载任务。
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
                download_task = Util.asyncio.create_task(self.download_file(task_id, file_url, full_path))
                download_tasks.append(download_task)
                # 这将使事件循环继续进行，允许任务立即开始
                await Util.asyncio.sleep(0)

        # 用于存储作者本页所有的下载任务, 最后会等待本页所有作品下载完成才结束本函数
        download_tasks = []

        # 作品发布时间区间
        should_check_interval = False
        start_date, end_date = (None, None)
        if self.config['interval'] != 'all':
            should_check_interval = True
            start_str, end_str = self.config['interval'].split('|')
            start_date = Util.time.strptime(start_str + " 00.00.00", '%Y-%m-%d %H.%M.%S')
            end_date = Util.time.strptime(end_str + " 23.59.59", '%Y-%m-%d %H.%M.%S')

        # 遍历aweme_data中的每一个aweme字典
        for aweme in aweme_data:
            aweme_time = Util.time.strptime(aweme['create_time'], '%Y-%m-%d %H.%M.%S')
            # 如果设置了日期区间并且作品的发布日期不在指定的日期范围内，则跳过
            if should_check_interval:
                # 如果 aweme_time 比不符合时间区间，跳过当前的作品
                if aweme_time < start_date or aweme_time > end_date:
                    continue

            # 如果设置了事件响应，则停止
            if Util.done_event.is_set():
                Util.progress.console.print("[  提示  ]: 中断该页下载")
                return

            # 获取文件的基础路径，这里的aweme['path']是到用户目录的绝对路径
            base_path = aweme['path']
            # 创建子目录名称
            subdir_name = await format_file_name(aweme, self.config['naming'])
            # 如果folderize配置设置为'yes'，则将作品单独保存为一个文件夹。
            if self.config['folderize'].lower() == 'yes':
                desc_path = Util.os.path.join(base_path, subdir_name)
            else:
                desc_path = base_path  # 直接使用基础路径，不创建子目录
            # 确保子目录存在，如果不存在，os.makedirs会自动创建
            Util.os.makedirs(desc_path, exist_ok=True)

            # 原声下载
            if self.config['music'].lower() == 'yes':
                try:
                    music_url = aweme['music_play_url']['url_list'][0]
                    music_name = f"{await format_file_name(aweme, self.config['naming'])}_music"
                    await initiate_download("音乐", music_url, ".mp3", desc_path, music_name)
                except Exception:
                    Util.progress.console.print("[  失败  ]：该原声不可用，无法下载。")
                    Util.log.warning(f"[  失败  ]：该原声不可用，无法下载。{aweme} 异常：{Exception}")

            # 视频下载
            if aweme['aweme_type'] == 0:
                try:
                    video_url = aweme['video_url_list'][0]
                    video_name = f"{await format_file_name(aweme, self.config['naming'])}_video"
                    await initiate_download("视频", video_url, ".mp4", desc_path, video_name)
                except Exception:
                    Util.progress.console.print("[  失败  ]:该视频不可用，无法下载。")
                    Util.log.warning(f"[  失败  ]:该视频不可用，无法下载。{aweme} 异常：{Exception}")

                # 封面下载
                if self.config['cover'].lower() == 'yes':
                    try:
                        cover_url = aweme['dynamic_cover'][0]
                        cover_name = f"{await format_file_name(aweme, self.config['naming'])}_cover"
                        await initiate_download("封面", cover_url, ".gif", desc_path, cover_name)
                    except Exception:
                        Util.progress.console.print(f"[  失败  ]:该视频封面不可用，无法下载。")
                        Util.log.warning(f"[  失败  ]:该视频封面不可用，无法下载。{aweme} 异常：{Exception}")

            # 图集下载
            elif aweme['aweme_type'] == 68:
                try:
                    for i, image_dict in enumerate(aweme['images']):
                        image_url = image_dict.get('url_list', [None])[0]
                        image_name = f"{await format_file_name(aweme, self.config['naming'])}_image_{i + 1}"
                        await initiate_download("图集", image_url, ".jpg", desc_path, image_name)
                except Exception:
                    Util.progress.console.print("[  失败  ]：该图片不可用，无法下载。")
                    Util.log.warning(f"[  失败  ]：该图片不可用，无法下载。{aweme} 异常：{Exception}")

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
