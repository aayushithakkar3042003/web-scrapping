import os
import requests
from bs4 import BeautifulSoup

# Replace 'your_website_url' with the actual URL of the website you want to scrape
url = "https://www.tutorialsfreak.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Create an 'images' directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Find all image tags
img_tags = soup.find_all('img')

# Download each image
for img in img_tags:
    img_url = img.get('src')
    if not img_url.startswith('http'):
        img_url = url + img_url  # Handle relative URLs
    img_data = requests.get(img_url).content

    # Generate a valid file name
    img_name = os.path.basename(img_url.split('?')[0])  # Remove query parameters

    img_path = os.path.join('images', img_name)
    with open(img_path, 'wb') as handler:
        handler.write(img_data)

print("Images have been downloaded successfully!")
