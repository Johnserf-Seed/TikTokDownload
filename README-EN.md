<div align="center">
<img width="450px"src="https://tva1.sinaimg.cn/large/006908GAly1gqg5fvxuutj30dw0dwt99.jpg"/>
</div>
<h1 align="center">TikTokDownload</h1>
<p align="center"> ✨ Tiktok to watermark video download ✨</ p>
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
<img src="https://img.shields.io/github/forks/johnserf-seed/tiktokdownload?style=social"></a>
<a target="_blank"href="http://mail.qq.com/cgi-bin/qm_share?t=qm_mailme&email=PFZTVFJPWU5aEU9ZWVh8WlNEUV1VUBJfU1E"Style="text decoration:none;">
<img src="http://rescdn.qqmail.com/zh_CN/htmledition/images/function/qm_open/ico_mailme_11.png"/>
</a>
</p>


[English](readme-en.md) [Simplified Chinese](readme.md)


## Tutorial use

1. Before running the software, open the conf.ini file in the directory and configure it as required


Batch download can directly modify the configuration file. For single video download, please directly open the main program and paste the video sharing link

![configuration screenshot](https://tvax1.sinaimg.cn/large/006908GAly1gqg5b6fbvsj30ng09iwes.jpg)


2. PIP package is made for this project. You can enter ``` PIP install tiktokdownload = = 1.2.3 ``` to install


![pypi release](https://tvax3.sinaimg.cn/large/006908GAly1gqg4j7ppuij30w60nnmxz.jpg)


![pip install TikTokDownload](https://tvax3.sinaimg.cn/large/006908GAly1gqg4jfswmxj30ul08xmy8.jpg)


**Package usage:**


```python

#example. py
#User homepage batch download
import TikTokMulti as MTK
MTK. TikTok()

#Single video download
import TikTokDownload as TK
TK. video_ download(*TK.main())

```

***example.py need to ensure tiktokmulti.py and tiktokdownload.py both files are in the same directory***


3. How to compile


Run ```build.bat``` In the root directory ,can be prompted by the console, and the generated ```exe```is in ```./dist```directory

4. Batch saving

![batch save](https://tvax1.sinaimg.cn/large/006908GAly1gqg4d73rryg31bi0hdx6p.gif)(old demo)

- Skip downloaded

![skip downloaded](https://tva4.sinaimg.cn/large/006908GAly1gt63poph2jj30rt0huwl8.jpg)

- Download all

![Download all](https://tva3.sinaimg.cn/large/006908GAly1gqg4dk7fiyj31cw0mo4qp.jpg)

- Resource folder

![resource folder 2](https://tva2.sinaimg.cn/large/006908GAly1gn1dim1oojj30q30ertaz.jpg)

- Folder Size

![folder size](https://tva3.sinaimg.cn/large/006908GAly1gqg4dny34uj30b10dt0st.jpg)


5. Issues feedback

If you have any bugs or feedback, please https://github.com/Johnserf-Seed/TikTokDownload/issues launch


![issues feedback](https://tva3.sinaimg.cn/large/006908GAly1gqg4f0b9kgj31hc0qwmz6.jpg)


6. Keep the single download mode tiktokdownload and batch download mode tiktokmulti


**Note (common errors):**


1. A single video link should be distinguished from the user's home page link. The software flash back can view the error information through the terminal operation (generally the problem of wrong link)


For example:


- ![error reporting](https://tvax4.sinaimg.cn/large/006908GAly1gn1dofvcc7j309800k3y9.jpg)


- ![error reporting](https://tvax2.sinaimg.cn/large/006908GAly1gn1dpoiqhzj306d0193ya.jpg)


***Links must be entered carefully~***


2. Pay attention to the coding format of the configuration file (Notepad + + is recommended)


**Correct:**


![UTF-8 correct](https://tva1.sinaimg.cn/large/006908GAly1gn1dl6jv3hj30ib09tq3k.jpg)


**Error:**


![UTF-8 error](https://tva1.sinaimg.cn/large/006908GAly1gn1dmakebqj30qh03lmx8.jpg)


It's very windy. The UTF-8 saved as can't flash back. Metaphysics

3. if long time tiktok is taken, it may be wrong to pose (API is rather strange). API


## New

**The new version after 4 / 23 supports the analysis of 1080p resolution video (*Note: Although 1080p is downloaded, the original resolution is still the original resolution even if the original video does not meet 1080p***)


**720p vs 1080p**

![image](https://tva4.sinaimg.cn/large/006908GAly1h1iwtyrqyij30id073q52.jpg)


**GUI version will be released soon**

![preview](https://tvax1.sinaimg.cn/large/006908GAly1gytdof69rrj30p00godhe.jpg)


**Utools plug-in synchronous development**

![version 1.0.1](https://tva4.sinaimg.cn/large/006908GAgy1gtbtg4t2n3j30ma02y40d.jpg)


![1.0.1 error](https://tvax1.sinaimg.cn/large/006908GAgy1gtbtgut1njj30ma02ygmk.jpg)


![plug in market](https://tva1.sinaimg.cn/large/006908GAgy1gtbtie2kuzj30pk0gqtd3.jpg)


**V1. 2.5 console interface version**


![v1.2.5 console interface version](https://tvax2.sinaimg.cn/large/006908GAly1gyuycwma5lj30ux0qstiz.jpg)


## ToDo

- [ ] no watermark Atlas download function

- [ ] record work details to local database

- [ ] local service detects the jitter, and focuses on updating user's work * (tiktok) *

- [ ] optional function for batch downloading of all videos that have followed the user's home page

- [ ] video analysis function of other platforms


## Web version project


[Johnserf-Seed/TikTokWeb](https://github.com/Johnserf-Seed/TikTokWeb)

<img src="https://tvax3.sinaimg.cn/large/006908GAly1h1e6e0mjmbj30m217a168.jpg">


<img src="https://tvax4.sinaimg.cn/large/006908GAly1gn1dxspeqeg302s02sdgf.gif">