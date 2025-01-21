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
