@echo off
echo Install Require
pip install -r requirements.txt
echo Build EXE version, Ctrl + C to Exit
pause
echo Bulid TikTokDMulti
pyinstaller -F -i logo.ico --version-file API\TikTokMultiVersion.txt TikTokMulti.py
echo Bulid TikTokDownload
pyinstaller -F -i logo.ico --version-file API\TikTokDownloadVersion.txt TikTokDownload.py
pause