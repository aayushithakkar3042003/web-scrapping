import requests 
from bs4 import BeautifulSoup
url = "https://www.tutorialsfreak.com/"
web = requests.get(url)
print("Status code= ",web.status_code)
soup = BeautifulSoup(web.content,"html.parser")
links = soup.find_all('p')
for link in links:
    print(link.get_text())
# hrefsi = soup.find_all('a')
# for hrefi in hrefsi:
#     href = hrefi.get('href')
#     text = hrefi.get_text()
#     print("link text = ",text,"\n url = ",hrefi)
#     print(text)