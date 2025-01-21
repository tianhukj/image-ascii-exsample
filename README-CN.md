# ASCII Art Converter

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
