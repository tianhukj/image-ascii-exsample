# ASCII Art Converter

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)
![GitHub followers](https://img.shields.io/github/followers/tianhukj.svg?style=social&label=Follow)
![GitHub stars](https://img.shields.io/github/stars/tianhukj/ASCII-Art-Converter.svg?style=social&label=Star)

## Project Introduction

ASCII Art Converter is a simple tool for converting images to ASCII art. It is written in Python and provides a convenient one-click Windows startup script that allows users to complete the conversion by simply entering the image path.

## Installation Guide

### Install dependencies using `pip`

First, make sure you have Python and `pip` installed. Then run the following command to install the required dependencies:

```bash
pip install image-ascii
```

### Example  Code
Here is an example code to convert an image to ASCII art:
```bash
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
