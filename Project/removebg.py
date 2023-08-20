from PIL import Image
import os
import cv2
import numpy as np
from scipy import ndimage
from rembg import remove

output_dir = "logo_images"
os.makedirs(output_dir, exist_ok=True)

def remove_white_background():
    input_path = os.path.join(output_dir, "fk-medžiai.png")
    output_path = os.path.join(output_dir, "fk-medžiai_outputx.webp")
    image = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)

    # Define the threshold for white pixels
    white_threshold = 220

    if image.shape[2] == 3:  # RGB image
        # Convert the image to RGBA format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)

    # Create a mask for white pixels
    white_mask = np.all(image[:, :, :3] > white_threshold, axis=-1)

    # Set alpha channel to 0 for white pixels
    image[white_mask, 3] = 0

    # Save the image with transparent background
    cv2.imwrite(output_path, image)  

# Specify your input and output file paths


# Call the function to remove the white background
remove_white_background()

def remove_background():
    input_path = os.path.join(output_dir, "fk-medžiai.png")
    output_path = os.path.join(output_dir, "fk-medžiai_outputy.webp")
    input_image = Image.open(input_path)
    
    output_image = remove(input_image)
    output_image.save(output_path, format="WebP", quality=95)

#remove_background()