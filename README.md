# ASCII Art Converter

[English](README.md) | [中文](README-CN.md)

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)
![GitHub followers](https://img.shields.io/github/followers/tianhukj.svg?style=social&label=Follow)
![GitHub stars](https://img.shields.io/github/stars/tianhukj/image-ascii-exsample.svg?style=social&label=Star)

## Project Introduction

ASCII Art Converter is a simple tool for converting images to ASCII art. It is written in Python and provides a convenient one-click Windows startup script that allows users to complete the conversion by simply entering the image path.

## Installation Guide

### Install dependencies using `pip`

First, make sure you have Python and `pip` installed. Then run the following command to install the required dependencies:

```bash
pip install asciimj
```

### Example  Code
Here is an example code to convert an image to ASCII art:
```bash
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
For details, see [exsample.py](exsample.py)

### One-Click Windows Startup Code
To simplify the user experience, you can use the following one-line bat command to install the required Python package and prompt the user to enter the image path, then automatically perform the conversion and save the result to ascii_art.txt in the same path:

For details, see [run_image_ascii.bat](run_image_ascii.bat)

## MIT License
This project is licensed under the MIT [LICENSE](LICENSE). For more details, please refer to the LICENSE file.
