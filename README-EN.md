# TikTokDownload V1.2.5

**tiktok to watermark video download, the last big update a year ago**

**Bug fixed after one year**

![mit](https://img.shields.io/badge/license-MIT-blue)![python: v3.8.5 (shields.io](https://img.shields.io/badge/python-v3.8.5-green)![pyqt](https://img.shields.io/badge/Qt5-v5.14.3-red)<a target="_blank" href="http://mail.qq.com/cgi-bin/qm_share?t=qm_mailme&email=PFZTVFJPWU5aEU9ZWVh8WlNEUV1VUBJfU1E " style="text-decoration:none;"><img src="http://rescdn.qqmail.com/zh_CN/htmledition/images/function/qm_open/ico_mailme_11.png "/></a>

[English](readme-en.MD)[simplified Chinese](readme.MD)

<a><div align=center>![Bannar](https://tva1.sinaimg.cn/large/006908GAly1gqg5fvxuutj30dw0dwt99.jpg)</div></a>

*GUI version will be released soon*
![preview](https://tvax1.sinaimg.cn/large/006908GAly1gytdof69rrj30p00godhe.jpg)

**Utools plug-in synchronous development**

![version 1.0.1](https://tva4.sinaimg.cn/large/006908GAgy1gtbtg4t2n3j30ma02y40d.jpg)

![1.0.1 error](https://tvax1.sinaimg.cn/large/006908GAgy1gtbtgut1njj30ma02ygmk.jpg)

![plug in market](https://tva1.sinaimg.cn/large/006908GAgy1gtbtie2kuzj30pk0gqtd3.jpg)

**V1. 2.5 console interface version**

![v1.2.5 console interface version](https://tvax2.sinaimg.cn/large/006908GAly1gyuycwma5lj30ux0qstiz.jpg)

###Using tutorials

1. Before running the software, open the conf.ini file in the directory and configure it as required

Batch download can directly modify the configuration file. For single video download, please directly open the main program and paste the video sharing link

![configuration screenshot](https://tvax1.sinaimg.cn/large/006908GAly1gqg5b6fbvsj30ng09iwes.jpg)

2. PIP package is made for this project. You can enter ``` pip install TikTokDownload == 1.2.3 ``` to install

![pypi release](https://tvax3.sinaimg.cn/large/006908GAly1gqg4j7ppuij30w60nnmxz.jpg)


![pip install TikTokDownload](https://tvax3.sinaimg.cn/large/006908GAly1gqg4jfswmxj30ul08xmy8.jpg)


**Package usage:**

```python
#example.py
#User homepage batch download
import TikTokMulti as MTK
MTK.TikTok()

#Single video download
import TikTokDownload as TK
TK.video_download(*TK.main())
```

***example.py need to ensure TikTokMulti.py and TikTokDownload.py both files are in the same directory***

3. Batch saving

![batch save](https://tvax1.sinaimg.cn/large/006908GAly1gqg4d73rryg31bi0hdx6p.gif)

Skip downloaded

![skip downloaded](https://tva4.sinaimg.cn/large/006908GAly1gt63poph2jj30rt0huwl8.jpg)

Download all

![Download all](https://tva3.sinaimg.cn/large/006908GAly1gqg4dk7fiyj31cw0mo4qp.jpg)

Resource folder

![resource folder 2](https://tva2.sinaimg.cn/large/006908GAly1gn1dim1oojj30q30ertaz.jpg)

Folder Size

![folder size](https://tva3.sinaimg.cn/large/006908GAly1gqg4dny34uj30b10dt0st.jpg)

4. If you have any bugs or feedback, please https://github.com/Johnserf-Seed/TikTokDownload/issues launch

![issues feedback](https://tva3.sinaimg.cn/large/006908GAly1gqg4f0b9kgj31hc0qwmz6.jpg)

5. Completely retain the single download mode Tik tokdownload, batch and single tiktokmulti (reconstructed code)

6. Compile py files with third-party libraries, such as pyinstaller

7. The GUI interface may be updated later to make the operation easier

**Note (common errors):**

1. A single video link should be distinguished from the user's home page link. The software flash back can view the error information through the terminal operation (generally the problem of wrong link)

For example:

![error reporting](https://tvax4.sinaimg.cn/large/006908GAly1gn1dofvcc7j309800k3y9.jpg)

![error reporting](https://tvax2.sinaimg.cn/large/006908GAly1gn1dpoiqhzj306d0193ya.jpg)

***Links must be entered carefully~***

2. Pay attention to the coding format of the configuration file (Notepad + + is recommended)

**Correct:**

![UTF-8 correct](https://tva1.sinaimg.cn/large/006908GAly1gn1dl6jv3hj30ib09tq3k.jpg)

**Error:**

![UTF-8 error](https://tva1.sinaimg.cn/large/006908GAly1gn1dmakebqj30qh03lmx8.jpg)

It's very windy. The UTF-8 saved as can't flash back. Metaphysics

3. if long time tiktok is taken, it may be wrong to pose (API is rather strange). API

<div align=center>
<img style="border-radius: 0.3125em;box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="https://tvax4.sinaimg.cn/large/006908GAly1gn1dxspeqeg302s02sdgf.gif"><br><div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">welcome to star</div></div>