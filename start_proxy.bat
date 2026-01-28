@echo off

echo 正在安装依赖...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo 依赖安装失败，请检查是否已安装Python
    pause
    exit /b %errorlevel%
)

echo 依赖安装成功，正在启动代理服务器...
python proxy_server.py

if %errorlevel% neq 0 (
    echo 代理服务器启动失败
    pause
    exit /b %errorlevel%
)