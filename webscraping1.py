import requests
# using get function to fetch data in diffrent formats
url = 'https://www.tutorialsfreak.com/'
web = requests.get(url)
print(web)
print(web.content)
print(web.url)
print(web.status_code)
