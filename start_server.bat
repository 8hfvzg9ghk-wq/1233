@echo off
setlocal enabledelayedexpansion
echo 正在启动HTTP服务器...
python -m http.server 8080
echo 服务器启动完成。如果遇到错误，请按任意键关闭窗口。
pause