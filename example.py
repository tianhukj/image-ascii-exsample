from image_ascii.convert import convert_image_to_ascii

def main():
    image_path = "/image.jpg"  # 替换为你的图片路径
    ascii_art = convert_image_to_ascii(image_path, new_width=100)
    if ascii_art:
        print(ascii_art)

if __name__ == "__main__":
    main()
