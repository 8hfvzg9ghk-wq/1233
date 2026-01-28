@echo off

echo ====================================
echo   哈基米番茄钟应用启动脚本  
echo ====================================
echo.
echo 请选择启动方式:
echo 1. 使用Docker容器（推荐）
echo 2. 使用Python内置服务器
echo 3. 使用Node.js http-server
echo 4. 直接打开HTML文件
echo.

set /p choice=请输入选项编号: 

echo.

if "%choice%"=="1" goto docker
if "%choice%"=="2" goto python
if "%choice%"=="3" goto node
if "%choice%"=="4" goto direct

:invalid
echo 错误: 无效的选项
goto end

:docker
echo === 使用Docker容器启动 ===
echo 检查Docker是否可用...
docker --version >nul 2>&1
if %errorlevel%==0 (
    echo Docker已安装，正在启动容器...
    docker-compose up -d --build
    echo.
    echo 容器启动成功！
    echo 应用访问地址: http://localhost:8080
) else (
    echo 错误: Docker未安装或不可用
    echo 请安装Docker Desktop并启动后重试
)
goto end

:python
echo === 使用Python内置服务器启动 ===
echo 检查Python是否可用...
python --version >nul 2>&1
if %errorlevel%==0 (
    echo Python已安装，正在启动服务器...
    python server.py
) else (
    echo 错误: Python未安装
    echo 请安装Python 3.x后重试
)
goto end

:node
echo === 使用Node.js http-server启动 ===
echo 检查Node.js是否可用...
node --version >nul 2>&1
if %errorlevel%==0 (
    echo Node.js已安装，检查http-server...
npm list -g http-server >nul 2>&1
if %errorlevel%==0 (
    echo http-server已安装，正在启动...
    http-server -p 8000
) else (
    echo http-server未安装，正在安装...
    npm install -g http-server
    if %errorlevel%==0 (
        echo http-server安装成功，正在启动...
        http-server -p 8000
    ) else (
        echo 错误: http-server安装失败
    )
)
) else (
    echo 错误: Node.js未安装
    echo 请安装Node.js后重试
)
goto end

:direct
echo === 直接打开HTML文件 ===
echo 请在浏览器中打开以下文件:
echo - index.html (主页面)
echo - pomodoro.html (番茄钟)
echo - alarm.html (闹钟)
echo - countdown.html (倒计时)
goto end

:end
echo.
echo ====================================
echo 启动脚本执行完成
echo ====================================