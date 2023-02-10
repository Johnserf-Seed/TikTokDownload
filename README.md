<div align="center">
<img width="450px" src="https://tva1.sinaimg.cn/large/006908GAly1gqg5fvxuutj30dw0dwt99.jpg"/>
</div>

<h1 align="center">TikTokDownload</h1>

<p align="center">✨ 抖音去水印视频下载 ✨</p>

<p align="center">
<a href="https://github.com/Johnserf-Seed/TikTokDownload/blob/main/LICENSE">
<img src="https://img.shields.io/github/license/johnserf-seed/tiktokdownload">
</a>
<a href="https://github.com/Johnserf-Seed/TikTokDownload">
<img src="https://img.shields.io/badge/python-v3.11.1-orange">
</a>
<a href="https://github.com/Johnserf-Seed/TikTokDownload">
<img src="https://img.shields.io/github/stars/johnserf-seed/tiktokdownload?style=social">
</a>
<a href="https://github.com/Johnserf-Seed/TikTokDownload">
<img src="https://img.shields.io/github/forks/johnserf-seed/tiktokdownload?style=social">
</a>
<a target="_blank" href="http://mail.qq.com/cgi-bin/qm_share?t=qm_mailme&email=PFZTVFJPWU5aEU9ZWVh8WlNEUV1VUBJfU1E" style="text-decoration:none;">
<img src="http://rescdn.qqmail.com/zh_CN/htmledition/images/function/qm_open/ico_mailme_11.png"/>
</a>
<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FJohnserf-Seed%2FTikTokDownload&count_bg=%235FFFFF&title_bg=%23FB1953&icon=tiktok.svg&icon_color=%23250C1F&title=view&edge_flat=false"/>
</a>
</p>

[English](README-EN.md)   [简体中文](README.md)

## 使用教程

1. 运行软件前先打开目录下``conf.ini`` 文件按照要求进行配置

  批量下载使用<a href="https://github.com/Johnserf-Seed/TikTokDownload/releases/tag/v1.3.0-beta">TikTokTool</a>，直接修改配置文件；单一视频下载推荐<a href="https://github.com/Johnserf-Seed/TikTokWeb">TikTokWeb</a>项目在线解析；**TikTokMulti不再维护**。

<table>
    <tr>
    <td><center>TikTokTool</td>
    <td><center>TikTokMulti</td>
    </tr>
    <tr>
        <td><center><img src="https://tvax2.sinaimg.cn/large/006908GAly1h5be5mhf5wj30am0bcabz.jpg"></center></td>
        <td><center><img src="https://tvax2.sinaimg.cn/large/006908GAly1h5be2em4ovj30ad0ba77s.jpg"></center></td>
    </tr>
    <tr>
    	<td><center>新版配置文件conf.ini</td>
    	<td><center>旧版配置文件conf.conf</td>
    </tr>
</table>

   **包使用方法：**

   ```python
   # example.py
   import TikTokDownload as TK
   import Util
   
   # 单视频下载
   # TK.video_download(*TK.main())
   
   # 批量下载
   if __name__ == '__main__':
       # 获取命令行参数
       cmd = Util.Command()
       # 获取用户主页数据
       profile = Util.Profile()
       # 使用参数，没有则使用默认参数并下载
       profile.getProfile(cmd.setting())
   	# 如果需要定时下载则注释这个input
       input('[  完成  ]:已完成批量下载，输入任意键后退出:')
   
   ```

   ***``example.py``需确保``Util``目录与``TikTokDownload.py``文件都在相同目录中***
   ***``example.py``需确保``Util``目录与``TikTokDownload.py``文件都在相同目录中***
   ***``example.py``需确保``Util``目录与``TikTokDownload.py``文件都在相同目录中***

**重要的话说三遍**

2. 如何编译

   运行根目录下```build.bat```文件按控制台提示即可，生成的```exe```在```./dist```目录中

3. 批量保存

	- 下载录制
	<img src="https://tva1.sinaimg.cn/large/006908GAly1h5bgh6pvgog318h0ey4qp.gif" alt="image" width="800" data-width="808" data-height="224">
	
	- 直播推流
	<img src="https://tva2.sinaimg.cn/large/006908GAly1h7aqbjrw9hj30uw06nq4g.jpg" alt="image" width="800" data-width="800" data-height="239">
   
	- 跳过已下载
	<img src="https://tva3.sinaimg.cn/large/006908GAly1h5beq5uq0qg313m0ktdl5.gif" alt="image" width="800" data-width="808" data-height="224">
	
	- 图文下载
	<img src="https://tva4.sinaimg.cn/large/006908GAly1h5bevy693qg313m0kt41g.gif" alt="image" width="800" data-width="808" data-height="224">
   
	- 全部下载
	<img src="https://tva3.sinaimg.cn/large/006908GAly1gqg4dk7fiyj31cw0mo4qp.jpg" alt="image" width="800" data-width="808" data-height="224">

	- 资源文件夹
	<img src="https://tva2.sinaimg.cn/large/006908GAly1gn1dim1oojj30q30ertaz.jpg" alt="image" width="800" data-width="808" data-height="224">
   
4. issues反馈
    如有您有任何bug或者意见反馈请在 https://github.com/Johnserf-Seed/TikTokDownload/issues 发起

<img src="https://tva3.sinaimg.cn/large/006908GAly1gqg4f0b9kgj31hc0qwmz6.jpg" alt="image" width="800" data-width="808" data-height="224">

5. 单一下载模式 ``TikTokDownload``;批量下载模式``TikTokMulti``;图文下载 ``TikTokPic``;测试版图形界面 ``TikTokMultiGUI``

**注意（常见错误）：**

1. 单个视频链接与用户主页链接要分清，软件闪退可以通过终端运行查看报错信息（一般是链接弄错的问题）

   如：

    - <img src="https://tvax4.sinaimg.cn/large/006908GAly1gn1dofvcc7j309800k3y9.jpg" alt="image" width="700" data-width="808" data-height="224">

    - <img src="https://tvax2.sinaimg.cn/large/006908GAly1gn1dpoiqhzj306d0193ya.jpg" alt="image" width="700" data-width="808" data-height="224">

   链接一定要输入仔细,配置文件只支持***用户主页***
   
   - <img src="https://tvax3.sinaimg.cn/large/006908GAly1h7aq83zn1wj30mc04dwi5.jpg" alt="image" width="700" data-width="804" data-height="157">
   
   ***出现报用户昵称错误的情况需要在主页发布一条视频，原因见 [获取用户昵称失败————主页若空作品则无法下载喜欢页](https://github.com/Johnserf-Seed/TikTokDownload/issues/236)***

2. 配置文件一定要注意编码格式（推荐Notepad++）

   **正确：**

<img src="https://tva1.sinaimg.cn/large/006908GAly1gn1dl6jv3hj30ib09tq3k.jpg" alt="image" width="700" data-width="808" data-height="224">

   **错误：**

<img src="https://tva1.sinaimg.cn/large/006908GAly1gn1dmakebqj30qh03lmx8.jpg" alt="image" width="700" data-width="808" data-height="224">

   挺抽风的，另存为的UTF-8居然不可以会闪退，玄学

3. 如果出现长时间的api抓取可能是姿势不对（抖音api服务器会抽）
4. 现在新增了日志功能，可以在logs中找到所有的日志文件，汇报issue的时候可以附上

<img src="https://tva2.sinaimg.cn/large/006908GAly1h5beyv1f13j30gk07pgqg.jpg" width="700">

<img src="https://tvax4.sinaimg.cn/large/006908GAly1h5bf16rylfj310q0ijb29.jpg" width="700">

## New

**09/15 支持获取抖音直播推流解析**

<img src="https://tva2.sinaimg.cn/large/006908GAly1h7aqbjrw9hj30uw06nq4g.jpg" alt="image" width="800" data-width="800" data-height="239">

<img src="https://tvax4.sinaimg.cn/large/006908GAly1h7aqf4v8exj30eu0sh7df.jpg" alt="image" width="500">


**08/30 现支持批量下载时自动下载主页所有图集内容**

<img src="https://tvax1.sinaimg.cn/large/006908GAly1h5olxy83pcj30n304mac3.jpg" alt="image" width="800" data-width="831" data-height="166">

<img src="https://tvax4.sinaimg.cn/large/006908GAly1h5olz436xrj30lr06g43z.jpg" alt="image" width="800" data-width="783" data-height="232">

<img src="https://tvax4.sinaimg.cn/large/006908GAly1h5om3r87lzj30uw0kzjyh.jpg" alt="image" width="800" data-width="1112" data-height="755">



**05/01 更新了无水印图集下载功能 ->TikTokPic.py**

<img src="https://tvax2.sinaimg.cn/large/006908GAly1h1s8uky10aj30us0gh0ym.jpg" alt="image" width="800" data-width="1108" data-height="593">

<img src="https://tva4.sinaimg.cn/large/006908GAly1h1s8pryq7rj30mg068tdn.jpg" alt="image" width="800" data-width="808" data-height="224">

**04/23 后的新版支持解析1080p分辨率视频（*注，虽然下载的是1080p，但是原视频不满足1080p的情况下，即使下载到本地也还是原本的分辨率***）

**720p对比1080p**

<img src="https://tva4.sinaimg.cn/large/006908GAly1h1iwtyrqyij30id073q52.jpg" alt="image" width="800" data-width="808" data-height="224">

**GUI版即将发布**

<img src="https://tva3.sinaimg.cn/large/006908GAly1h5bf3snbfij30sm0gzwhc.jpg" alt="image" width="800" data-width="808" data-height="224">

***可自行在GUI文件夹内编译ui -> pyuic5 -o Main.py Main.ui***

**V1.3.0控制台界面版本**

<img src="https://tvax1.sinaimg.cn/large/006908GAly1h5bf5oylooj30ui0m20zn.jpg" alt="image" width="800" data-width="808" data-height="224">

**uTools插件同步开发中...**

<img src="https://tva4.sinaimg.cn/large/006908GAgy1gtbtg4t2n3j30ma02y40d.jpg" alt="image" width="800" data-width="808" data-height="224">

<img src="https://tvax1.sinaimg.cn/large/006908GAgy1gtbtgut1njj30ma02ygmk.jpg" alt="image" width="800" data-width="808" data-height="224">

<img src="https://tva2.sinaimg.cn/large/006908GAly1h5bf4dvde0j30m00gnwij.jpg" alt="image" width="800" data-width="808" data-height="224">

## ToDo
- [x] 无水印图集下载功能
- [x] 可视化界面
- [x] 直播推流保存
- [ ] 支持多平台视频解析
- [ ] 记录作品详细信息到本地数据库
- [ ] 本地服务检测抖音关注用户作品的更新情况 ***(并推送)***
- [ ] 所有已关注用户主页的视频批量下载的可选功能
- [ ] 收藏作品与搜索作品下载
- [ ] 制作本地接口解析服务


## Web版项目

[Johnserf-Seed/TikTokWeb](https://github.com/Johnserf-Seed/TikTokWeb)

<img src="https://tvax3.sinaimg.cn/large/006908GAly1h1e6e0mjmbj30m217a168.jpg" alt="image" width="800" data-width="808" data-height="224">



## 赞赏

<img src="https://user-images.githubusercontent.com/40727745/217866800-23980dc1-f3ce-4bc7-b192-518651fef8da.png" alt="赞赏" width="1000" data-width="808" data-height="224">
https://www.patreon.com/TikTokDownload713


# 声明
<h1>本项目只做个人学习研究之用，不得用于商业用途！</h1>
