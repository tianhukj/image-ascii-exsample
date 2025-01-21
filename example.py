import os
from asciimj import AsciiMJ
from PIL import Image

def image_to_ascii(image_path, output_width=100):
    # 打开图像
    image = Image.open(image_path)
    
    # 创建AsciiMJ对象
    ascii_mj = AsciiMJ(image, output_width)
    
    # 获取ASCII艺术字符串
    ascii_art = ascii_mj.to_ascii()
    
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
        
        # 转换图像为ASCII艺术
        ascii_art = image_to_ascii(image_path)
        
        # 将ASCII艺术保存到文件
        save_ascii_to_file(ascii_art, output_path)
        
        print(f"ASCII艺术已保存到 {output_path}")
