import os
from rembg import remove
from PIL import Image
import requests
from dataextractor import DataExtractor
from bs4 import BeautifulSoup
import io
from pathlib import Path


class ImagesData:
    output_dir = "logo_images"
    os.makedirs(output_dir, exist_ok=True)
    
    def __init__(self, web_url):
        self.web_url = web_url
        self.standings_table = DataExtractor(self.web_url).get_table()
        self.images_urls_dict = self.get_team_images_urls()
        
    
    def get_teams_urls(self):
        teams_urls = {} 
        for tr_block in self.standings_table.find_all('tr'):
            a_tag = tr_block.find('a')
            if a_tag and 'href' in a_tag.attrs:
                team_url = a_tag['href']
                team_name = a_tag.get_text(strip=True)
                try:
                    response = requests.head(a_tag['href'])
                    if response.status_code == 200:
                        teams_urls[team_name] = team_url
                except requests.RequestException:
                        print(f"URL check for '{team_name}': Failed to reach URL")
                        pass  
        return teams_urls

    def get_team_images_urls(self):
        images_urls_dict = {}
        for team_name, team_url in self.get_teams_urls().items():
            response_html = requests.get(team_url)
            if response_html.status_code != 200:
                return f"Link to {team_name} website is not reachable, status code: {response_html.status_code}"

            soup = BeautifulSoup(response_html.content, 'html.parser')
            specific_div_tag = soup.find('div', class_='span5')
            if specific_div_tag:
                img_tag = specific_div_tag.find('img', alt='{}'.format(team_name))
                if img_tag and 'src' in img_tag.attrs:
                    team_image_url = img_tag['src']
                    images_urls_dict[team_name] = team_image_url
                else:
                    print(f"No image URL found on {team_name} website") 
        return images_urls_dict   
            
    def save_image(self):
        for team_name, team_logo_url in self.images_urls_dict.items():
            
            image_content = requests.get(team_logo_url).content
            image_file = io.BytesIO(image_content)
            image = Image.open(image_file)

            if image.mode == "RGBA":
                white_background = Image.new("RGB", image.size, (255, 255, 255))
                white_background.paste(image, mask=image.split()[3])
            else: 
                white_background = image

            file_path = Path(self.output_dir, team_name.strip().lower().replace(' ', '-') + ".png")
            white_background.save(file_path, "PNG", quality=80)

            input_path = file_path  # Use the path of the saved white-background image
            output_path = file_path.with_suffix(".webp")  # Change the extension to .webp
            input_image = Image.open(input_path)
            
            #if input_image.mode == "RGB":
            output_image = remove(input_image)
                
            #if input_image.mode == "RGB":
                
            output_image.save(output_path, format="PNG", quality=95)
                    
    def empty_image_folder(self):
        #files_names = list(self.images_urls_dict.values())
        folder_path = os.path.join(self.output_dir)
        file_list = os.listdir(folder_path)
        for file_name in file_list:
            if file_name.endswith(".png") or file_name.endswith(".webp"):
                file_path = os.path.join(folder_path, file_name)
            try:
                os.remove(file_path)
                print(f"Deleted: {file_name}")
            except Exception as e:
                print(f"Error deleting {file_name}: {e}")

my_obj = ImagesData("http://www.vilniausfutbolas.lt/lyga/III-Lyga/20")

my_obj.save_image()
#my_obj.empty_image_folder()

###############################







