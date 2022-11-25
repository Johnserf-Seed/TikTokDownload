#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:维护之前下载的视频/图片
@Date       :2022/11/24
@Author     :JP Zhang
@version    :1.0.0
@License    :(C)Copyright 2019-2022, Liugroup-NLPR-CASIA
@Github     :https://github.com/zjplab
@Mail       :zjplab@gmail.com
'''
from tqdm import tqdm
import multiprocessing as mp
import subprocess

class MultiCmds:
    def __init__(self, urls, number_of_tasks=4):
        self.urls = urls
        self.cmd_prefix = ['python', './TiktokTool.py', '-u']
        self.cmds=[self.cmd_prefix+[url] for url in self.urls]
        self.NUMBER_OF_TASKS = number_of_tasks
        self.progress_bar = tqdm(total=self.NUMBER_OF_TASKS)

    def exec(self):
        # print(self.cmds)
        # print(self.NUMBER_OF_TASKS)
        pool = mp.Pool(self.NUMBER_OF_TASKS)
        for cmd in self.cmds:
            pool.apply_async(MultiCmds.work, (cmd,), callback=self.update_progress_bar)
        pool.close()
        pool.join()
    
    @staticmethod
    def work(cmd):
        # To do: 压制
        # subprocess.call(cmd, stdout=subprocess.DEVNULL)
        subprocess.call(cmd)

    def update_progress_bar(self, _):
        self.progress_bar.update()


class TikTokMaintain:
    def __init__(self):
        self.users_mapping = {}
        with open("maintainList.txt", "r", encoding="UTF-8") as f:
            file_lsts = f.readlines()
            file_lsts= [line for line in file_lsts if not line.startswith("#")]
            self.users_mapping= {split[0]:split[1]  for line in file_lsts if (split:=line.strip().split())[0].startswith("https")}
            self.users_mapping.update({split[1]:split[0]  for line in file_lsts if not (split:=line.strip().split())[0].startswith("http")})

    def maintain(self):
        cmds= MultiCmds(urls=self.users_mapping.keys(), number_of_tasks=4)
        cmds.exec()

if __name__ == '__main__':
    maintain = TikTokMaintain()
    maintain.maintain()