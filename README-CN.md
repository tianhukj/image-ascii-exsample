# ASCII Art Convert--asciimj

[English](README.md) | [中文](README-CN.md)

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)
![GitHub followers](https://img.shields.io/github/followers/tianhukj.svg?style=social&label=Follow)
![GitHub stars](https://img.shields.io/github/stars/tianhukj/image-ascii-exsample.svg?style=social&label=Star)

## 项目介绍

asciimj 是一个简单的工具，用于将图像转换为 ASCII 艺术。它基于 Python 编写，并提供了一个方便的 Windows 一键启动脚本，用户只需输入图像路径即可完成转换。

## 安装教程

### 使用 `pip` 安装依赖包

首先，确保你已经安装了 Python 和 `pip`。然后运行以下命令来安装所需的依赖包：

```bash
pip install asciimj
```

### 示例代码
以下是一个示例代码，用于将图像转换为 ASCII 艺术：

```python
import os
import asciimj
from PIL import Image

def image_to_ascii(image_path, output_width=100):
    # 打开图像
    image = Image.open(image_path)
    
    # 使用 asciimj 包直接转换图像为 ASCII 艺术
    ascii_art = asciimj.convert_image_to_ascii(image, output_width)
    
    return ascii_art

def save_ascii_to_file(ascii_art, output_path):
    with open(output_path, 'w') as file:
        file.write(ascii_art)

if __name__ == "__main__":
    # 直接在代码中输入图像路径
    image_path = "image.jpg"  # 替换为你的图像路径
    
    # 检查文件是否存在
    if not os.path.isfile(image_path):
        print("文件不存在，请检查路径并重试。")
    else:
        # 生成输出文件路径
        output_path = os.path.splitext(image_path)[0] + ".txt"
        
        # 转换图像为 ASCII 艺术
        ascii_art = image_to_ascii(image_path)
        
        # 将 ASCII 艺术保存到文件
        save_ascii_to_file(ascii_art, output_path)
        
        print(f"ASCII 艺术已保存到 {output_path}")
```

For details, see [exsample.py](example.py)

### Windows 一键启动代码
为了简化用户体验，你可以使用以下一行 bat 命令来安装所需的 Python 包，并提示用户输入图片路径，然后自动进行转换并将结果保存到同一路径下的 ascii_art.txt 文件中：

For details, see [run_image_ascii.bat](run_image_ascii.bat)

## 使用 MIT 许可证
该项目使用 MIT 许可证。详细信息请参阅 [LICENSE](LICENSE) 文件。
