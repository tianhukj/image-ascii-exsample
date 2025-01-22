# ASCII Art Convert--asciimj

[English](README.md) | [中文](README-CN.md)

![GitHub license](https://img.shields.io/badge/license-MIT-yello.svg)
![GitHub followers](https://img.shields.io/github/followers/tianhukj.svg?style=social&label=Follow)
![GitHub stars](https://img.shields.io/github/stars/tianhukj/image-ascii-exsample.svg?style=social&label=Star)
[![PyPI version](https://badge.fury.io/py/image-ascii-exsample.svg)](https://badge.fury.io/py/image-ascii)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/yourusername/image-ascii/issues)
![Commit Activity](https://img.shields.io/github/commit-activity/y/tianhukj/image-ascii-exsample)
![GitHub Watchers](https://img.shields.io/github/watchers/tianhukj/image-ascii-exsample?style=social)
[![Buy Me a Coffee](https://img.shields.io/badge/Donate-Buy%20Me%20A%20Coffee-FF813F.svg?logo=buy-me-a-coffee)](https://www.buymeacoffee.com/tianhukj)


## Project Introduction

asciimj is a simple tool for converting images to ASCII art. It is written in Python and provides a convenient one-click Windows startup script that allows users to complete the conversion by simply entering the image path.

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
    image = Image.open(image_path)
    
    ascii_art = asciimj.convert_image_to_ascii(image, output_width)
    
    return ascii_art

def save_ascii_to_file(ascii_art, output_path):
    with open(output_path, 'w') as file:
        file.write(ascii_art)

if __name__ == "__main__":
    image_path = "image.jpg"  
    
    if not os.path.isfile(image_path):
        print("file not found")
    else:
        output_path = os.path.splitext(image_path)[0] + ".txt"
        
        ascii_art = image_to_ascii(image_path)
        
        save_ascii_to_file(ascii_art, output_path)
        
        print(f"ASCIIART had saved by{output_path}")
```
For details, see [exsample.py](exsample.py)

### One-Click Windows Startup Code
To simplify the user experience, you can use the following one-line bat command to install the required Python package and prompt the user to enter the image path, then automatically perform the conversion and save the result to ascii_art.txt in the same path:

For details, see [run_image_ascii.bat](run_image_ascii.bat)

## MIT License
This project is licensed under the MIT [LICENSE](LICENSE). For more details, please refer to the LICENSE file.
