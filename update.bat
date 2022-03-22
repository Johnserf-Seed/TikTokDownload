@echo off & title TikTokDownload update By JohnserfSeed

set Url=https://github.com/Johnserf-Seed/TikTokDownload/releases/download/v1.2.5/TikTokMulti.exe
set Url2=https://github.com/Johnserf-Seed/TikTokDownload/releases/download/v1.2.5/TikTokDownload.exe

set Save=.\dist
if exist %Save% (echo Update Location：%Save%) else (mkdir %Save% & echo Created：%Save%)
if not exist ".\dist\TikTokMulti.exe" (
del ".\dist\TikTokMulti.exe"
del ".\dist\TikTokDownload.exe"
echo old version deleted
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
echo TikTokMulti Update Complete
DownloadFile.vbs "%Url2%" ".\dist\TikTokDownload.exe"
echo TikTokDownload Update Complete

del DownloadFile.vbs
pause