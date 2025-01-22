# 显示ASCII艺术
Write-Host "    _      ____     ____   ___   ___   __  __       _ "
Write-Host "   / \    / ___|   / ___| |_ _| |_ _| |  \/  |     | |"
Write-Host "  / _ \   \___ \  | |      | |   | |  | |\/| |  _  | |"
Write-Host " / ___ \   ___) | | |___   | |   | |  | |  | | | |_| |"
Write-Host "/_/   \_\ |____/   \____| |___| |___| |_|  |_|  \___/ "
Write-Host ""

# 安装 asciimj 包
pip install asciimj

# 提示用户输入图片路径
$imagePath = Read-Host "请输入图片的路径"

# 检查图片路径是否存在
if (-Not (Test-Path -Path $imagePath)) {
    Write-Host "图片路径不存在，请检查后重试。"
    Pause
    Exit
}

# 获取图片文件的目录和文件名（不包括扩展名）
$imageDirectory = Split-Path -Path $imagePath -Parent
$imageName = [System.IO.Path]::GetFileNameWithoutExtension($imagePath)

# 生成输出的TXT文件路径
$outputFile = "$imageDirectory\$imageName.txt"

# 创建一个Python脚本来转换图片为ASCII并保存为TXT
$pythonScript = @"
import sys
from asciimj import convert_image_to_ascii

img_path = sys.argv[1]
output_path = sys.argv[2]

with open(output_path, 'w') as f:
    ascii_art = convert_image_to_ascii(img_path)
    f.write(ascii_art)
"@

# 将Python脚本保存到临时文件
$scriptPath = "$env:TEMP\convert.py"
$pythonScript | Out-File -FilePath $scriptPath -Encoding UTF8

# 运行Python脚本
python $scriptPath $imagePath $outputFile

# 删除临时的Python脚本
Remove-Item -Path $scriptPath

# 打印输出目录
Write-Host "转换完成，ASCII艺术已保存到: $outputFile"
Pause
