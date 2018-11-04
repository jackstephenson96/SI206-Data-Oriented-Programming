from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
count = int(input("Enter count: "))
position = int(input("Enter position: "))
print(url)
names = []

for x in range(count):
	newHtml = urlopen(url)
	soup = BeautifulSoup(newHtml, 'html.parser')
	tags = soup('a')
	for tag in tags:
		names.append(tag.get('href', None))
	url = names[position - 1]
	print(url)
	names = []















# print(names[position - 1])
# 	newUrl = names[position - 1]
# 	html = urlopen(newUrl)
# 	soup = BeautifulSoup(html, 'html.parser')