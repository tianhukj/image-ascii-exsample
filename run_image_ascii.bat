@echo off
cls

:: 设置蓝色文本颜色
echo [34m
echo _                                                 _ _ 
echo (_)_ __ ___   __ _  __ _  ___        __ _ ___  ___(_|_)
echo | | '_ ` _ \ / _` |/ _` |/ _ \_____ / _` / __|/ __| | |
echo | | | | | | | (_| | (_| |  __/_____| (_| \__ \ (__| | |
echo |_|_| |_| |_|\__,_|\__, |\___|      \__,_|___/\___|_|_|
echo                   |___/
echo [0m

echo.

:input
set /p image_path="Please enter the path to the image file: "

if "%image_path%"=="" (
    echo You must provide a valid image path.
    goto input
)

:: Get the directory of the image file
for %%f in ("%image_path%") do set image_dir=%%~dpf

echo Installing image-ascii package...
pip install image-ascii==0.1.0

echo Converting image to ASCII art and saving to file...
python -c "from image_ascii.convert import convert_image_to_ascii; import os; image_path = r'%image_path%'; output_path = os.path.join(r'%image_dir%', 'ascii_art.txt'); ascii_art = convert_image_to_ascii(image_path, new_width=100); with open(output_path, 'w') as f: f.write(ascii_art); print(f'ASCII art saved to {output_path}')"

echo.
pause
