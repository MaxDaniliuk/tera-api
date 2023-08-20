from bs4 import BeautifulSoup
import requests
import os
from rembg import remove
from PIL import Image, ImageFilter

image_url = "http://www.vilniausfutbolas.lt/uploads/_sfl.lt/teams/335_big.png"
response = requests.get(image_url)
if response.status_code != 200:
    print("Failed")

output_dir = "logo_images"
os.makedirs(output_dir, exist_ok=True)
    
def upload_image():    
    name = "whooo-Team_Logoxxx"
    image_name = f"{name}.png"  # Or use a different naming scheme
    image_path = os.path.join(output_dir, image_name)

    with open(image_path, "wb") as f:
            f.write(response.content)
    return name
uploaded_image_name = upload_image()
print(uploaded_image_name)

#input_path = os.path.join(output_dir, f"{uploaded_image_name}.jpg")
#output_path = os.path.join(output_dir, f"{uploaded_image_name}_output.jpg")

#input_image = Image.open(input_path)

#if input_image.mode in ("RGBA", "P"): 
#    im = input_image.convert("RGB")


# Process the image to remove the background
#output_image = remove(input_image)

# Save the processed image back to the same path, overwriting the original image
#output_image.save(output_path)



"""def remove_background(input_image_path, output_image_path):
    input_image = Image.open(input_image_path)
    
    #output_image_size = input_image.size 
    #print(output_image_size)
    #new_width = output_image_size[0] * 5
    #new_height = output_image_size[1] * 5

    # Resize the image using Lanczos resampling
    #resized_image = input_image.resize((new_width, new_height)) #(..... ,resample=Image.LANCZOS)

    # Process the image to remove the background
    output_image = remove(input_image)

    # Apply a Gaussian blur to smooth out artifacts
    #smoothed_image = output_image.filter(ImageFilter.GaussianBlur(radius=0.1))

    # Sharpen the image to enhance details
    #sharpened_image = smoothed_image.filter(ImageFilter.UnsharpMask(radius=0.5, percent=150))

    # Denoise the image to reduce noise and artifacts
    #denoised_image = sharpened_image.filter(ImageFilter.MedianFilter(size=3))

    # Save the processed image as a WebP image
    output_image.save(output_image_path, format="WebP", quality=80)

# Specify the paths for input and output images
input_image_path = os.path.join(output_dir, f"{uploaded_image_name}.png")
output_image_path = os.path.join(output_dir, f"{uploaded_image_name}_output.webp")

# Call the remove_background function to remove the background and save as WebP
remove_background(input_image_path, output_image_path)

print("Background removed and image saved as WebP.")"""
