import requests
import pandas as pd
import io
from PIL import Image, ImageFilter
from pathlib import Path
import hashlib
import os
from rembg import remove
import cv2
import numpy as np



output_dir = "logo_images"
os.makedirs(output_dir, exist_ok=True)

other_img = []

image_url = [
            'http://www.vilniausfutbolas.lt/uploads/_sfl.lt/teams/165_big.png?2022-08-30',
            'http://www.vilniausfutbolas.lt/uploads/_sfl.lt/teams/285_big.png?2022-08-30'
             ]

def save_urls_to_csv():
    df = pd.DataFrame({"links": image_url})
    df.to_csv("links.csv", index=False, encoding="utf-8")

for url_img in image_url:

    image_content = requests.get(url_img).content
    image_file = io.BytesIO(image_content)
    image = Image.open(image_file)
    #if image.mode != "RGBA":
    #    image = image.convert("RGBA")
    if image.mode == "RGBA":
        white_background = Image.new("RGB", image.size, (255, 255, 255))
        white_background.paste(image, mask=image.split()[3])
    else: 
        white_background = image

    file_path = Path(output_dir, hashlib.sha1(image_content).hexdigest()[:10] + ".png")
    white_background.save(file_path, "PNG", quality=80)

    input_path = file_path  # Use the path of the saved white-background image
    output_path = file_path.with_suffix(".webp")  # Change the extension to .webp
    input_image = Image.open(input_path)
    
    if input_image.mode == "RGB":
        output_image = remove(input_image)
        
    if input_image.mode == "RGB":
        pass
    output_image.save(output_path, format="PNG", quality=95)





