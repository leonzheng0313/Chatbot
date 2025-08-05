@echo off
chcp 65001 >nul
echo.
echo ========================================
echo    ChatPersona AI人格社交平台
echo ========================================
echo.

:: 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误: 未找到Python，请先安装Python 3.7+
    echo 下载地址: https://www.python.org/downloads/
    pause
    exit /b 1
)

:: 检查是否在正确目录
if not exist "app.py" (
    echo ❌ 错误: 请在ChatPersona项目根目录下运行此脚本
    pause
    exit /b 1
)

:: 检查依赖是否安装
echo 🔍 检查依赖包...
python -c "import flask" >nul 2>&1
if errorlevel 1 (
    echo 📦 正在安装依赖包...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ❌ 依赖安装失败，请手动运行: pip install -r requirements.txt
        pause
        exit /b 1
    )
    echo ✅ 依赖安装完成
)

echo.
echo 🚀 启动ChatPersona...
echo.

:: 启动应用
python run.py

echo.
echo 👋 ChatPersona已停止运行
pause