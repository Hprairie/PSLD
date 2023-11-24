import os
from PIL import Image

def convert_png_to_jpg_inplace(png_path):
    img = Image.open(png_path)
    gray_img = img.convert('L')
    jpg_path = png_path.replace('.png', '.jpg')
    gray_img.save(jpg_path)

    # Delete the original PNG file
    os.remove(png_path)

# Usage
dir_path = 'training/images'
images = os.listdir(dir_path)

for image in images:
    image_path = os.path.join(dir_path, image)
    convert_png_to_jpg_inplace(image_path)
