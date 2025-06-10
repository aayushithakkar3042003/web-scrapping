import requests
from bs4 import BeautifulSoup
url = 'https://www.tutorialsfreak.com/'
web = requests.get(url)
print(web.content)
print("*"*100)
print(web.text)
print("*"*100)
print(web.url)
print("*"*100)
print(web.raw)
soup = BeautifulSoup(web.content,"html.parser")
print(soup.h1)
print(soup.prettify)
print(soup.title)
#tag
tag = soup.html
print(tag)
print(soup.p)
print("Navigable string")
print(soup.p.string)
print(soup.a.string)
print(soup.h1.string)
#Beautifulsoup
print(soup.name)
print(soup.title.string)
print(soup.head.string)
print(soup.findall("src="))