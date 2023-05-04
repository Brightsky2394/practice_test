#!/usr/bin/python3

import bs4
import requests

x = input("Enter text to be search: ")
link = "https://en.wikipedia.org/wiki/Simple:" + str(x)
response = requests.get(link)
wiki = bs4.BeautifulSoup(response.text, "html.parser")
file_name = input("Enter file name with .txt extension: ")
fd = open(file_name, 'w+', encoding='utf-8')
heading = wiki.find('h1').text
fd.write(heading + '\n')
for j in wiki.select("p"):
    fd.write(j.getText())
fd.close()
print("File saved as" + file_name) 
