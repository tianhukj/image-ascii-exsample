# ASCII Art Converter

[English](README.md) | [中文](README-CN.md)

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)
![GitHub followers](https://img.shields.io/github/followers/tianhukj.svg?style=social&label=Follow)
![GitHub stars](https://img.shields.io/github/stars/tianhukj/image-ascii-exsample.svg?style=social&label=Star)

## 项目介绍

ASCII Art Converter 是一个简单的工具，用于将图像转换为 ASCII 艺术。它基于 Python 编写，并提供了一个方便的 Windows 一键启动脚本，用户只需输入图像路径即可完成转换。

## 安装教程

### 使用 `pip` 安装依赖包

首先，确保你已经安装了 Python 和 `pip`。然后运行以下命令来安装所需的依赖包：

```bash
pip install image-ascii
```

### 示例代码
以下是一个示例代码，用于将图像转换为 ASCII 艺术：

```python
import os
from image_ascii import convert_image_to_ascii

def main():
    image_path = "image.JPG"  # 根目录下的图片路径
    ascii_art = convert_image_to_ascii(image_path, new_width=100)
    if ascii_art:
        output_path = os.path.join(os.path.dirname(image_path), 'ascii_art.txt')
        with open(output_path, 'w') as f:
            f.write(ascii_art)
        print(f"ASCII art saved to {output_path}")

if __name__ == "__main__":
    main()
```

### Windows 一键启动代码
为了简化用户体验，你可以使用以下一行 bat 命令来安装所需的 Python 包，并提示用户输入图片路径，然后自动进行转换并将结果保存到同一路径下的 ascii_art.txt 文件中：

```bash
@echo off && pip install image-ascii && set /p img_path="Enter image path: " && python -c "import os; from image_ascii import convert_image_to_ascii; img_path='%img_path%'; ascii_art = convert_image_to_ascii(img_path, new_width=100); output_path = os.path.join(os.path.dirname(img_path), 'ascii_art.txt'); open(output_path, 'w').write(ascii_art); print(f'ASCII art saved to {output_path}')"
```

## 使用 MIT 许可证
该项目使用 MIT 许可证。详细信息请参阅 ![LICENSE](./LICENSE) 文件。
