<div align="center">
<img width="450px" src="https://tva1.sinaimg.cn/large/006908GAly1gqg5fvxuutj30dw0dwt99.jpg"/>
</div>

<h1 align="center">TikTokDownload</h1>

<p align="center">✨  Jitterbug watermark video download  ✨</p>

<p align="center">
<a href="https://github.com/Johnserf-Seed/TikTokDownload/blob/main/LICENSE">
<img src="https://img.shields.io/github/license/johnserf-seed/tiktokdownload">
</a>
<a href="https://github.com/Johnserf-Seed/TikTokDownload">
<img src="https://img.shields.io/badge/python-v3.8.5-green">
</a>
<a href="https://github.com/Johnserf-Seed/TikTokDownload">
<img src="https://img.shields.io/github/stars/johnserf-seed/tiktokdownload?style=social">
</a>
<a href="https://github.com/Johnserf-Seed/TikTokDownload">
<img src="https://img.shields.io/github/forks/johnserf-seed/tiktokdownload?style=social">
</a>
<a target="_blank" href="http://mail.qq.com/cgi-bin/qm_share?t=qm_mailme&email=PFZTVFJPWU5aEU9ZWVh8WlNEUV1VUBJfU1E" style="text- decoration:none;">
<img src="http://rescdn.qqmail.com/zh_CN/htmledition/images/function/qm_open/ico_mailme_11.png"/>
</a>
</p>
[English](README-EN.md) [Simplified Chinese](README.md)

## Tutorial

1. Before running the software, open the conf.ini file in the directory and configure it as required

Batch download can directly modify the configuration file, single video download recommended <a href="https://github.com/Johnserf-Seed/TikTokWeb">TikTokWeb</a> project online parsing

​                                          **Older profiles**                                                                     *** New profiles***
​                                          **conf.ini                                                                                ** ***conf.conf***

<figure class="half" align="center">
<img src="https://tva2.sinaimg.cn/large/006908GAly1h5be5mhf5wj30am0bcabz.jpg" width="380">
<img src="https://tvax3.sinaimg.cn/large/006908GAly1h5be2em4ovj30ad0ba77s.jpg" width="380">
</figure>

2. This project created pip package, you can enter `` pip install TikTokDownload==1.2.3 `` to install ~~
(1.2.3 is not updated to 1.3.0 in time, please do not install)

<img src="https://tvax3.sinaimg.cn/large/006908GAly1gqg4j7ppuij30w60nnmxz.jpg" alt="image" width="800" data-width="808" data-height="224">

<img src="https://tvax3.sinaimg.cn/large/006908GAly1gqg4jfswmxj30ul08xmy8.jpg" alt="image" width="800" data-width="808" data-height="224">

**Package usage:**

   ```python
   #example.py
   import TikTokDownload as TK
   import TikTokMulti as MTK
   # Delete comments to use the corresponding file
   
   # user home page batch download
   # MTK.TikTok()
   
   # Single video download
   # TK.video_download(*TK.main())
   ```

   ***example.py needs to make sure that both TikTokMulti.py and TikTokDownload.py files are in the same directory***

3. How to compile

   Run the ``build.bat`` file in the root directory and follow the console prompts, the resulting ``exe`` will be in the ``. /dist``` directory

4. Batch save

	- Download the recording
	<img src="https://tva3.sinaimg.cn/large/006908GAly1h5bel0gf8ng319r0g3qvc.gif" alt="image" width="800" data-width="808" data-height="224 ">
   
	- Skip Downloaded
	<img src="https://tva3.sinaimg.cn/large/006908GAly1h5beq5uq0qg313m0ktdl5.gif" alt="image" width="800" data-width="808" data-height="224 ">
	
	- Graphic Download
	<img src="https://tva4.sinaimg.cn/large/006908GAly1h5bevy693qg313m0kt41g.gif" alt="image" width="800" data-width="808" data-height="224 ">
   
	- Download All
	<img src="https://tva3.sinaimg.cn/large/006908GAly1gqg4dk7fiyj31cw0mo4qp.jpg" alt="image" width="800" data-width="808" data-height="224 ">

	- Resource Folder
	<img src="https://tva2.sinaimg.cn/large/006908GAly1gn1dim1oojj30q30ertaz.jpg" alt="image" width="800" data-width="808" data-height="224 ">
   
5. issues feedback
    If you have any bugs or feedback, please post them at https://github.com/Johnserf-Seed/TikTokDownload/issues

<img src="https://tva3.sinaimg.cn/large/006908GAly1gqg4f0b9kgj31hc0qwmz6.jpg" alt="image" width="800" data-width="808" data-height="224 ">

6. single download mode TikTokDownload batch download mode TikTokMulti
	Graphic Download TikTokPic Beta GUI TikTokMultiGUI

**Note (common errors):**

1. a single video link and the user home page link to distinguish, the software flashback can be run through the terminal to view the error message (usually the problem of the wrong link)

   Such as.

    - <img src="https://tvax4.sinaimg.cn/large/006908GAly1gn1dofvcc7j309800k3y9.jpg" alt="image" width="800" data-width="808" data-height=" 224">

    - <img src="https://tvax2.sinaimg.cn/large/006908GAly1gn1dpoiqhzj306d0193ya.jpg" alt="image" width="800" data-width="808" data-height=" 224">

   *** link must be entered carefully Oh ~***

2. configuration file must pay attention to the encoding format (Notepad++ is recommended)

   **Correct:**

<img src="https://tva1.sinaimg.cn/large/006908GAly1gn1dl6jv3hj30ib09tq3k.jpg" alt="image" width="700" data-width="808" data-height="224 ">

   **Error:**

<img src="https://tva1.sinaimg.cn/large/006908GAly1gn1dmakebqj30qh03lmx8.jpg" alt="image" width="700" data-width="808" data-height="224 ">

   quite jerky, save as UTF-8 actually can not be flashback, metaphysics

3. if there is a long time api crawl may be the wrong posture (shake api more strange)
4. now the new log function, you can find all the log files in the logs, when reporting issues can be attached

<img src="https://tva2.sinaimg.cn/large/006908GAly1h5beyv1f13j30gk07pgqg.jpg" width="700">
<img src="https://tvax4.sinaimg.cn/large/006908GAly1h5bf16rylfj310q0ijb29.jpg">


## New

**05/01 Updated with watermark-free gallery download ->TikTokPic.py**

<img src="https://tvax2.sinaimg.cn/large/006908GAly1h1s8uky10aj30us0gh0ym.jpg" alt="image" width="800" data-width="1108" data-height="593">

<img src="https://tva4.sinaimg.cn/large/006908GAly1h1s8pryq7rj30mg068tdn.jpg" alt="image" width="800" data-width="808" data-height="224">

**04/23 after the new version supports the resolution of 1080p video** (***Note, although the download is 1080p, but the original video does not meet the case of 1080p, even if downloaded to the local is still the original resolution***)

**720p compared to 1080p**

**GUI version to be released soon**

<img src="https://tva4.sinaimg.cn/large/006908GAly1h1iwtyrqyij30id073q52.jpg" alt="image" width="800" data-width="808" data-height="224">

***You can compile ui by yourself in the GUI folder -> pyuic5 -o Main.py Main.ui***

**V1.3.0 console interface version**

<img src="https://tvax1.sinaimg.cn/large/006908GAly1h5bf5oylooj30ui0m20zn.jpg" alt="image" width="800" data-width="808" data-height="224">

**Utools plug-in synchronous development**

<img src="https://tva4.sinaimg.cn/large/006908GAgy1gtbtg4t2n3j30ma02y40d.jpg" alt="image" width="800" data-width="808" data-height="224">

<img src="https://tvax1.sinaimg.cn/large/006908GAgy1gtbtgut1njj30ma02ygmk.jpg" alt="image" width="800" data-width="808" data-height="224">

<img src="https://tva2.sinaimg.cn/large/006908GAly1h5bf4dvde0j30m00gnwij.jpg" alt="image" width="800" data-width="808" data-height="224">

## ToDo

- [x] Watermark-free gallery download function
- [x] Visualization interface
- [ ] Support multi-platform video parsing
- [ ] Record work details to local database
- [ ] Local service detects updates of ShakeYin followed users' works***(and push)***
- [ ] Optional function for batch download of videos from all followed users' homepages
- [ ] Live streaming push stream saving
- [ ] Make local interface parsing service


## Web version project


[Johnserf-Seed/TikTokWeb](https://github.com/Johnserf-Seed/TikTokWeb)

<img src="https://tvax3.sinaimg.cn/large/006908GAly1h1e6e0mjmbj30m217a168.jpg">


<img src="https://tvax4.sinaimg.cn/large/006908GAly1gn1dxspeqeg302s02sdgf.gif">