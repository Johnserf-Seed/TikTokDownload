#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description:TikTokTool.py
@Date       :2022/07/29 23:19:14
@Author     :JohnserfSeed
@version    :1.6
@License    :MIT License
@Github     :https://github.com/johnserf-seed
@Mail       :johnserf-seed@foxmail.com
-------------------------------------------------
Change Log  :
2022/07/29 23:19:14 : Init
2023/03/10 16:22:19 : gen dyheaders
2023/08/04 02:09:31 : async download
2023/12/26 18:01:56 : Switch to f2
2024/04/05 00:56:22 : Update to 1.6 with f2 0.0.1.5
-------------------------------------------------
"""

import f2
import sys
import time
from f2.cli.cli_console import RichConsoleManager as RCManager


if __name__ == "__main__":
    RCManager = RCManager()

    if len(sys.argv) <= 1:
        RCManager.rich_console.print(
            "[bold red]请通过命令行启动并提供必要的参数, 输入[bold green] TikTokTool -h [/bold green]查看不同平台帮助。[/bold red]"
        )

        RCManager.rich_console.print(
            f"[bold white]F2 Version:{f2.__version__}[/bold white]"
        )
        time.sleep(3)
        sys.exit(1)

    from f2.apps.douyin.cli import douyin
    from f2.apps.tiktok.cli import tiktok

    clis = [douyin, tiktok]

    selected = RCManager.rich_prompt.ask(
        "[bold yellow]1.Douyin 2.TikTok:[/bold yellow]",
        choices=[str(i) for i in range(1, len(clis) + 1)],
    )

    # 调用相应的 CLI 函数
    clis[int(selected) - 1]()
