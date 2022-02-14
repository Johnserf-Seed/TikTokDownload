# TikTokDownload V1.2.5
**抖音去水印视频下载，年前最后一次大大大更新**

**bug统一年后修复**
![mit](https://img.shields.io/badge/license-MIT-blue)![python: v3.8.5 (shields.io](https://img.shields.io/badge/python-v3.8.5-green)![pyqt](https://img.shields.io/badge/Qt5-v5.14.3-red)<a target="_blank" href="http://mail.qq.com/cgi-bin/qm_share?t=qm_mailme&email=PFZTVFJPWU5aEU9ZWVh8WlNEUV1VUBJfU1E" style="text-decoration:none;"><img src="http://rescdn.qqmail.com/zh_CN/htmledition/images/function/qm_open/ico_mailme_11.png"/></a>

[English](README-EN.md) [简体中文](README.md)

<a><div align=center>![Bannar](https://tva1.sinaimg.cn/large/006908GAly1gqg5fvxuutj30dw0dwt99.jpg)</div></a>

*GUI版即将发布*
![preview](https://tvax1.sinaimg.cn/large/006908GAly1gytdof69rrj30p00godhe.jpg)

**uTools插件同步开发中...**

![1.0.1版本](https://tva4.sinaimg.cn/large/006908GAgy1gtbtg4t2n3j30ma02y40d.jpg)

![1.0.1 error](https://tvax1.sinaimg.cn/large/006908GAgy1gtbtgut1njj30ma02ygmk.jpg)

![插件市场](https://tva1.sinaimg.cn/large/006908GAgy1gtbtie2kuzj30pk0gqtd3.jpg)

**V1.2.5控制台界面版本**
![V1.2.5控制台界面版本](https://tvax2.sinaimg.cn/large/006908GAly1gyuycwma5lj30ux0qstiz.jpg)


### 使用教程

1. 运行软件前先打开目录下 conf.ini 文件按照要求进行配置

  批量下载可直接修改配置文件，单一视频下载请直接打开主程序粘贴视频分享链接即可
  ![配置截图](https://tvax1.sinaimg.cn/large/006908GAly1gqg5b6fbvsj30ng09iwes.jpg)

2. 本项目制作了pip包，可以输入 ``` pip install TikTokDownload==1.2.3 ```安装

   ![pypi发布](https://tvax3.sinaimg.cn/large/006908GAly1gqg4j7ppuij30w60nnmxz.jpg)

   ![pip install TikTokDownload](https://tvax3.sinaimg.cn/large/006908GAly1gqg4jfswmxj30ul08xmy8.jpg)

   **包使用方法：**

   ```python
   #example.py
   #用户主页批量下载
   import TikTokMulti as MTK
   
   MTK.TikTok()
   
   #单视频下载
   import TikTokDownload as TK
   
   TK.video_download(*TK.main())
   ```

   ***example.py需确保TikTokMulti.py与TikTokDownload.py两个文件都在相同目录中***

3. 批量保存
   ![批量保存](https://tvax1.sinaimg.cn/large/006908GAly1gqg4d73rryg31bi0hdx6p.gif)
   
	跳过已下载
   ![跳过已下载](https://tva4.sinaimg.cn/large/006908GAly1gt63poph2jj30rt0huwl8.jpg)
   
	全部下载
   ![全部下载](https://tva3.sinaimg.cn/large/006908GAly1gqg4dk7fiyj31cw0mo4qp.jpg)  
   
	资源文件夹
   ![资源文件夹2](https://tva2.sinaimg.cn/large/006908GAly1gn1dim1oojj30q30ertaz.jpg)
   
	文件夹大小
   ![文件夹大小](https://tva3.sinaimg.cn/large/006908GAly1gqg4dny34uj30b10dt0st.jpg)

4. 如有您有任何bug或者意见反馈请在 https://github.com/Johnserf-Seed/TikTokDownload/issues 发起

   ![issues反馈](https://tva3.sinaimg.cn/large/006908GAly1gqg4f0b9kgj31hc0qwmz6.jpg)

5. 完全保留单一下载模式 Tik TokDownload，批量与单一TikTokMulti（重新构造了代码）

6. 编译py文件可以用第三方库，如Pyinstaller等

7. 后续可能会更新GUI界面，操作更简单


**注意（常见错误）：**

1. 单个视频链接与用户主页链接要分清，软件闪退可以通过终端运行查看报错信息（一般是链接弄错的问题）

   如：

   ![报错](https://tvax4.sinaimg.cn/large/006908GAly1gn1dofvcc7j309800k3y9.jpg)

   ![报错](https://tvax2.sinaimg.cn/large/006908GAly1gn1dpoiqhzj306d0193ya.jpg)

   ***链接一定要输入仔细哦~***

2. 配置文件一定要注意编码格式（推荐Notepad++）

   **正确：**

   ![utf-8正确](https://tva1.sinaimg.cn/large/006908GAly1gn1dl6jv3hj30ib09tq3k.jpg)

   **错误：**

   ![utf-8错误](https://tva1.sinaimg.cn/large/006908GAly1gn1dmakebqj30qh03lmx8.jpg)

   挺抽风的，另存为的UTF-8居然不可以会闪退，玄学
   
3. 如果出现长时间的api抓取可能是姿势不对（抖音api比较奇怪）

<center><img style="border-radius: 0.3125em;box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);"src="https://tvax4.sinaimg.cn/large/006908GAly1gn1dxspeqeg302s02sdgf.gif"><br><div style="color:orange; border-bottom: 1px solid #d9d9d9;display: inline-block;color: #999;padding: 2px;">欢迎Star</div></center>
