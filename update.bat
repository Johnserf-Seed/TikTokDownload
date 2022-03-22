@echo off & title TikTokDownload update By JohnserfSeed
 
::设置要下载的文件链接，仅支持http协议。必写项。
set Url=https://github.com/Johnserf-Seed/TikTokDownload/releases/download/v1.2.5/TikTokMulti.exe
set Url2=https://github.com/Johnserf-Seed/TikTokDownload/releases/download/v1.2.5/TikTokDownload.exe

::设置文件保存目录，若下载至当前目录，请留空
set Save=.\dist
if exist %Save% (echo 更新位置：%Save%) else (mkdir %Save% & echo 已创建：%Save%)
if not exist ".\dist\TikTokMulti.exe" (
del ".\dist\TikTokMulti.exe"
del ".\dist\TikTokDownload.exe"
echo 已删除旧版本
)

for %%a in ("%Url%") do set "FileName=%%~nxa"
if not defined Save set "Save=%cd%"
(echo Download Wscript.Arguments^(0^),Wscript.Arguments^(1^)
echo Sub Download^(url,target^)
echo   Const adTypeBinary = 1
echo   Const adSaveCreateOverWrite = 2
echo   Dim http,ado
echo   Set http = CreateObject^("Msxml2.ServerXMLHTTP"^)
echo   http.open "GET",url,False
echo   http.send
echo   Set ado = createobject^("Adodb.Stream"^)
echo   ado.Type = adTypeBinary
echo   ado.Open
echo   ado.Write http.responseBody
echo   ado.SaveToFile target, 2
echo   ado.Close
echo End Sub)>DownloadFile.vbs

DownloadFile.vbs "%Url%" ".\dist\TikTokMulti.exe"
echo TikTokMulti更新完成
DownloadFile.vbs "%Url2%" ".\dist\TikTokDownload.exe"
echo TikTokDownload更新完成
::下载完删除生成的vbs文件
del DownloadFile.vbs
pause