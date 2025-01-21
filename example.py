import os
from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def scale_image(image, new_width=100):
    """调整图像大小"""
    original_width, original_height = image.size
    aspect_ratio = original_height / float(original_width)
    new_height = int(aspect_ratio * new_width)
    new_image = image.resize((new_width, new_height))
    return new_image

def convert_to_grayscale(image):
    """将图像转为灰度"""
    return image.convert("L")

def map_pixels_to_ascii_chars(image, range_width=25):
    """将像素映射到ASCII字符"""
    pixels = list(image.getdata())
    ascii_str = ""
    for pixel in pixels:
        index = pixel // range_width
        # 确保索引在ASCII_CHARS范围内
        if index >= len(ASCII_CHARS):
            index = len(ASCII_CHARS) - 1
        ascii_str += ASCII_CHARS[index]
    return ascii_str

def convert_image_to_ascii(image_path, new_width=100):
    """将图像转换为ASCII艺术"""
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file {image_path}. {e}")
        return ""

    # 调整图像大小
    image = scale_image(image, new_width)
    
    # 转换为灰度
    image = convert_to_grayscale(image)
    
    # 将像素映射到ASCII字符
    ascii_str = map_pixels_to_ascii_chars(image)
    
    # 将ASCII字符分行
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join([ascii_str[index: index + img_width] for index in range(0, ascii_str_len, img_width)])
    
    return ascii_img

def main():
    # 在这里定义图片文件的路径
    image_path = "/image.jpg"  # 请替换为你的图片路径
    
    # 检查输入的路径是否有效
    if not os.path.isfile(image_path):
        print("Invalid image path. Please provide a valid file path.")
        return

    # 将图片转换为 ASCII 艺术
    ascii_art = convert_image_to_ascii(image_path, new_width=100)
    
    if ascii_art:
        # 获取图片文件所在的目录
        image_dir = os.path.dirname(image_path)
        # 创建输出文件路径
        output_path = os.path.join(image_dir, 'ascii_art.txt')
        
        # 将 ASCII 艺术保存到文件中
        with open(output_path, 'w') as f:
            f.write(ascii_art)
        
        # 打印保存路径
        print(f"ASCII art saved to {output_path}")

if __name__ == "__main__":
    main()
