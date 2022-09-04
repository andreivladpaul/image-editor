from email.mime import image
from PIL import Image, ImageEnhance, ImageFilter
import os

imgs_path = "./imgs"
edited_imgs_path = "./edited-imgs"

for filename in os.listdir(imgs_path):
    img = Image.open(f"{imgs_path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert("L")

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]
    edit.save(f"{edited_imgs_path}/{clean_name}_edited.jpg")
