@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

:: 显示ASCII艺术
echo    _    ____   ____ ___ ___ __  __     _ 
echo   / \  / ___| / ___|_ _|_ _|  \/  |   | |
echo  / _ \ \___ \| |    | | | || |\/| |_  | |
echo / ___ \ ___) | |___ | | | || |  | | |_| |
echo /_/   \_\____/ \____|___|___|_|  |_|\___/ 
echo.

:: 安装 asciimj 包
pip install asciimj

:: 提示用户输入图片路径
set /p imgPath="请输入图片的路径: "

:: 检查图片路径是否存在
if not exist "%imgPath%" (
    echo 图片路径不存在，请检查后重试。
    pause
    exit /b
)

:: 获取图片文件的目录和文件名（不包括扩展名）
for %%F in ("%imgPath%") do (
    set imgDir=%%~dpF
    set imgName=%%~nF
)

:: 生成输出的TXT文件路径
set outputFile=%imgDir%%imgName%.txt

:: 创建一个Python脚本来转换图片为ASCII并保存为TXT
echo import sys > convert.py
echo from asciimj import convert_image_to_ascii >> convert.py
echo img_path = sys.argv[1] >> convert.py
echo output_path = sys.argv[2] >> convert.py
echo with open(output_path, 'w') as f: >> convert.py
echo     ascii_art = convert_image_to_ascii(img_path) >> convert.py
echo     f.write(ascii_art) >> convert.py

:: 运行Python脚本
python convert.py "%imgPath%" "%outputFile%"

:: 删除临时的Python脚本
del convert.py

:: 打印输出目录
echo 转换完成，ASCII艺术已保存到: %outputFile%
pause
