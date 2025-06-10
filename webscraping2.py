import requests
from bs4 import BeautifulSoup
url = "https://www.tutorialsfreak.com/"
web = requests.get(url)
print(web.status_code)
print(web.content)
print(web.url)
print ("*"*500)
soup = BeautifulSoup(web.content,"html.parser")
print(soup.prettify())

title = soup.title
print(title)
print(soup.title.name)
print(soup.p)
print(soup.a)
print(soup.h1)


