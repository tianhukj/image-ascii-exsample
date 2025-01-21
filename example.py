import os
from image_ascii.convert import convert_image_to_ascii

def main():
    # 在这里定义图片文件的路径
    image_path = "image.jpg"  # 替换为你的图片路径
    
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
