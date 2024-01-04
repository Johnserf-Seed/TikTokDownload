@echo off
echo Install Pip Require
pip install -r requirements.txt
echo Build EXE version, Press Ctrl + C to Exit
echo Build Server
pyinstaller -F -i ..\f2-logo.ico --distpath . --version-file Server.txt --hidden-import=charset_normalizer.md__mypyc Server.py
echo Install Npm Require
npm i
pause