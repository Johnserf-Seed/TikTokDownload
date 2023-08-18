
![项目图](https://tvax2.sinaimg.cn/large/006908GAly1hgn9zod1yuj30zk0hstmf.jpg)

<h1 align="center">✨ 抖音去水印作品下载 ✨</h1>
<div align="center">

[English](README-EN.md) | 简体中文

[![License: MIT](https://img.shields.io/github/license/johnserf-seed/tiktokdownload?style=for-the-badge)](https://github.com/Johnserf-Seed/TikTokDownload/blob/main/LICENSE)
![Release Download](https://img.shields.io/github/downloads/Johnserf-Seed/TikTokDownload/total?style=for-the-badge)
![GitHub Repo size](https://img.shields.io/github/repo-size/Johnserf-Seed/TikTokDownload?style=for-the-badge&color=3cb371)
[![GitHub Repo Languages](https://img.shields.io/github/languages/top/Johnserf-Seed/TikTokDownload?style=for-the-badge)](https://github.com/BeyondDimension/SteamTools/search?l=c%23)
[![Python v3.11.1](https://img.shields.io/badge/python-v3.11.1-orange?style=for-the-badge)](https://github.com/Johnserf-Seed/TikTokDownload)
![Terminal: wt](https://img.shields.io/badge/Terminal-wt-blue?style=for-the-badge)

[![GitHub Stars](https://img.shields.io/github/stars/johnserf-seed/tiktokdownload?style=social)](https://github.com/Johnserf-Seed/TikTokDownload)
[![GitHub Forks](https://img.shields.io/github/forks/johnserf-seed/tiktokdownload?style=social)](https://github.com/Johnserf-Seed/TikTokDownload)
[![GitHub Issues](https://img.shields.io/github/issues/johnserf-seed/tiktokdownload?style=social)](https://github.com/Johnserf-Seed/TikTokDownload)
[![GitHub Closed Issues](https://img.shields.io/github/issues-closed/johnserf-seed/tiktokdownload?style=social)](https://github.com/Johnserf-Seed/TikTokDownload)

[![jsDelivr monthly hits](https://data.jsdelivr.com/v1/package/gh/Johnserf-Seed/TikTokDownload/badge)](https://www.jsdelivr.com/package/gh/Johnserf-Seed/TikTokDownload)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FJohnserf-Seed%2FTikTokDownload&count_bg=%235FFFFF&title_bg=%23FB1953&icon=tiktok.svg&icon_color=%23250C1F&title=view&edge_flat=false)](https://hits.seeyoufarm.com)
[![Discord](https://img.shields.io/discord/1070512513889878067?color=5865F2&logo=discord&logoColor=white?style=for-the-badge)](https://discord.gg/q3hA8qQZbG)
[![Patreon](https://img.shields.io/badge/Patreon-TikTokDownload-red.svg?style=flat&logo=patreon)](https://www.patreon.com/TikTokDownload713)

</div>


## 🚀 环境准备/Environment

> [![Microsoft 应用商店](https://tvax1.sinaimg.cn/large/006908GAly1hgn87jhad8j305001qa9y.jpg)](https://aka.ms/terminal)
> 
> 旧的控制台无法很好适配，推荐使用Windows Terminal。
> 
> [![Python v3.11.1](https://www.python.org/static/img/python-logo.png)](https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe)
> 
> Python3.11.1 低于该版本可能会有意外的错误
> 
> [![GitHub 发行版](https://tvax2.sinaimg.cn/large/006908GAly1hh16psn51aj30a5020gly.jpg)](https://github.com/Johnserf-Seed/TikTokDownload/releases)
> 
> 发行版下载 每次Commits之后会重新打包

<details><summary> ⚙ Windows Terminal 设置（必看） </summary>

![wt配置](https://github.com/Johnserf-Seed/TikTokDownload/assets/40727745/997b6fc2-586e-4268-bee8-43bb8d68622c)

</details>


## 🧰 功能/Features

- DouYin 接口信息
	- ✅ 详细用户信息。
	- ✅ 下载发布作品。
	- ✅ 下载收藏作品。
	- ✅ 下载喜欢作品。
	- ✅ 下载图集作品。
	- ✅ 下载作品封面。
	- ✅ 下载作品文案。
	- ✅ 下载作品原声。
	- ✅ 提取直播链接。
	- ⌛  下载关注作品。
	- ⌛  下载好友作品。
	- ⌛  下载推荐作品。
	- ❌ 下载合集作品。
	- ❌ 提取评论。

- 异步下载
	- ✅ 同时下载和处理多个作品，提高效率。
	- ✅ 调节异步线程，减轻系统压力减少接口出错。
	- ✅ 调节网络并发数，减少被服务器校验

- Cookie 管理
	- ✅ 生成web所需 cookie 值，便于访问需要登录的接口。
	- ✅ 处理 SetCookie。

- 配置文件操作
    - ✅ 长短链解析。
	- ✅ 自定义保存目录。
	- ✅ 是否下载原声。
	- ✅ 是否自动更新。
	- ✅ 指定下载时间区间。
	- ❌ 设定下载作品点赞阈值。
	- ❌ 设定下载作品播放阈值。

- 版本更新
	- ✅ 提供自动检查和下载新版本的功能。

- 文件检查
	- ✅ 下载文件前检查文件是否已经存在，避免重复下载。

- 命令行交互
	- ✅ 提供命令行选项和全局 headers，便于用户操作。
	- ⌛  提供webui模式

- 扫码登录
	- ✅ 提供扫码登录的功能，无需手动填写 cookie。

- 自动重命名
	- ✅ 使用昵称映射表确保不重复下载改名作者的作品。
	- ⌛  使用作品文案映射表确保不重复下载改文案的作品。

- 本地加密参数调用
	- ✅ XBogus
	- ✅ verifyFp
	- ✅ s_v_web_id
	- ✅ ttwid
	- ✅ x-tt-params
	- 🔘 msToken


## 💡 待办/ToDo

- 适配TikTok
- 创建自动化任务
- 多用户解析
- [更多请查看项目板](https://github.com/users/Johnserf-Seed/projects/1/views/1)


## 🖥 支持的操作系统/Supported Operating Systems

<details>
<summary> 1.4.2.2 支持的操作系统列表 </summary>

- Windows 11
- Windows 10 版本 1809（OS 内部版本 17763）或更高版本
- macOS Monterey（12.0）或更高版本
- macOS Big Sur（11.0）或更高版本
- macOS Catalina（10.15）或更高版本
- Ubuntu 20.04 LTS 或更高版本
- Debian 10 或更高版本
- CentOS 7 或更高版本
- Fedora 34 或更高版本
- Deepin (UOS) 20 或更高版本

</details>


## 📸 运行过程/Running Process

<details>
  <summary> 🎬 无配置文件扫码登录 </summary>

https://user-images.githubusercontent.com/40727745/fc1e6c46-d0c3-4f2a-a4a5-ca3d781e7d11

 </details>

<details>
  <summary> 🎬 主页作品下载 </summary>

https://user-images.githubusercontent.com/40727745/12c21d55-b629-485a-b904-54d86341c371

 </details>


## 📥 安装与运行/Installation and Running

1. **📦 安装/Installation**


```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

2. **▶️ 运行/Running**


```python
import Util

if __name__ == '__main__':
    # 获取命令行和配置文件
    cmd = Util.Command()
    config = cmd.config_dict
    dyheaders = cmd.dyheaders

    # 异步下载作品
    Util.asyncio.run(Util.Profile(config, dyheaders).get_Profile())
    input("[  提示  ]:下载完成，输入任意键退出。")
```

3. **🔬 测试/Test**

```bash
python example.py
```


## 🗂️ 项目结构/Folder

<details>
<summary>📁 目录</summary>

```bash
├─ .github
│   └─ ISSUE_TEMPLATE
│       ├── --------.md
│       └── -------.md
│
├─ API
│   ├── API.js
│   ├── API参考.md
│   ├── Server.txt
│   ├── TikTokAPI.py
│   ├── TikTokDownloadVersion.txt
│   ├── TikTokGUIVersion.txt
│   ├── TikTokLive.txt
│   ├── TikTokMultiVersion.txt
│   ├── TikTokPicVersion.txt
│   ├── TikTokTool.txt
│   ├── TikTokUpdata.txt
│   ├── user_base_info.json
│   ├── user_post_delete.json
│   ├── user_post_detail.json
│   ├── user_post_info_image.json
│   ├── user_post_info_video.json
│   └── user_profile_info.json
│
├─ Collection
│   ├── CopyWritingHomePage_1.json
│   ├── GirlHomePage_1.json
│   └── MusicHomePage_1.json
│
├─ DB
│   └── create.sql
│
├─ GUI
│   ├── Main.ui
│   ├── preview.png
│   ├── README-EN.md
│   ├── README.md
│   ├── requirements.txt
│   ├── resource.py
│   └── Resource.qrc
│
└─ Util
    ├── Check.py
    ├── Command.py
    ├── Config.py
    ├── Cookies.py
    ├── Download.py
    ├── Lives.py
    ├── Log.py
    ├── Login.py
    ├── NickMapper.py
    ├── Profile.py
    ├── Resource.py
    ├── Urls.py
    ├── XB.py
    ├── __init__.py
    ├── __version__.py
    └─ algorithm
        ├── package.json
        ├── Server.py
        ├── s_v_web_id.js
        ├── s_v_web_id.py
        ├── x-bogus.js
        └── x-tt-params.js
│
├─ .gitignore
├─ Banner.png
├─ build-win.bat
├─ conf.conf
├─ conf.ini
├─ Dockerfile
├─ example.py
├─ info.db
├─ LICENSE
├─ Logo.ico
├─ README-EN.md
├─ README.md
├─ requirements.txt
├─ server.bat
├─ server.sh
├─ TikTokLive.py
├─ TikTokMultiGUI.py
├─ TikTokTool.py
├─ TikTokUpdata.py
├─ version
└─ _config.yml

```

</details>


## 💖 赞赏/Sponsor

![赞赏](https://user-images.githubusercontent.com/40727745/217866800-23980dc1-f3ce-4bc7-b192-518651fef8da.png)

感谢对本项目的支持！如果您觉得这个项目有帮助，欢迎赞助。您可以直接访问我们的 [![Patreon](https://img.shields.io/badge/Patreon-TikTokDownload-red.svg?style=flat&logo=patreon)](https://www.patreon.com/TikTokDownload713)


## 📧 联系/Contact

如果有任何问题或者建议，可以通过邮箱联系我：

- 邮箱：[johnserf-seed@foxmail.com](mailto:johnserf-seed@foxmail.com)


## 🙏 鸣谢/Acknowledgments

- [Windows Terminal](https://aka.ms/terminal)
- [aiohttp](https://github.com/aio-libs/aiohttp)
- [requests](https://github.com/psf/requests)
- [Pillow (PIL Fork)](https://github.com/python-pillow/Pillow)
- [lxml](https://github.com/lxml/lxml)
- [rich](https://github.com/willmcgugan/rich)
- [qrcode](https://github.com/lincolnloop/python-qrcode)
- [ConfigObj](https://github.com/DiffSK/configobj)

对于他们的贡献和努力，我们表示由衷的感谢。


## ⚖️ 免责声明/Disclaimer

此项目不出售、共享、加密、上传、研究任何个人信息。此项目及其相关代码仅供学习与研究使用，不构成任何明示或暗示的保证。使用者因使用此项目及其代码可能造成的任何形式的损失，作者不承担任何责任。


## 📜 版权声明/LICENSE

MIT License

Copyright (c) 2021 JohnserfSeed

此项目的源代码在 MIT 许可证下授权，有关详细信息，请参阅 [LICENSE](LICENSE) 文件。


## 📝 贡献者守则/CoC

此项目欢迎所有的贡献者。我们希望能够创建一个友好的环境，让每个人都能在尊重和理解的氛围中共同工作。在参与贡献之前，请参阅我们的 [贡献者守则](CODE_OF_CONDUCT.md)。


## 👨‍💻贡献者/Contributors

我们欢迎任何形式的贡献，无论是提交错误报告，提出改进意见，或者是提供代码和文档。我们都欣赏你的帮助。

![Contributors](https://contributors-img.web.app/image?repo=Johnserf-Seed/TikTokDownload)

