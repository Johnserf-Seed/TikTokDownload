@echo off
echo Install Require
pip install -r requirements.txt
echo Build EXE version, Press Ctrl + C to Exit
pause
echo Build Server
pyinstaller -F -i f2-logo.ico --version-file API\Server.txt --hidden-import=charset_normalizer.md__mypyc Server\Server.py
echo Bulid TikTokTool
pyinstaller -F -i f2-logo.ico --version-file API\TikTokTool.txt --hidden-import=charset_normalizer.md__mypyc TikTokTool.py
pause