from typing import Text
import requests
from bs4 import BeautifulSoup

 def open_html(path):
     with open(path, 'rb') as f:
         return f.read()  
        
page = html = open_html('quotes.html') 
soup = BeautifulSoup(page, features="html.parser")

#page = requests.get("http://quotes.toscrape.com/")
#soup = BeautifulSoup(page.content, features="html.parser")

i=0
list_tags = []
# fa l'scraping de totes les quotes de la web passant cada pàgina
while True:

    divs = soup.find_all(attrs={'class':'quote'})
    for div in divs:
        text = div.find(attrs={'class':'text'})
        author = div.find(attrs={'class':'author'})
        print(str(i) + text.string)
        print(author.string)
        tags = div.find_all(attrs={'class':'tag'})
        for tag in tags:
            list_tags.append (tag.string)
        print (*list_tags, sep=", ") 
        list_tags.clear()
        i=i+1
        print()
    if not (paginacio := soup.find(attrs={'class':'next'})):
        break
    a = paginacio.find('a') 
    page = requests.get("http://quotes.toscrape.com"+a['href'])
    soup = BeautifulSoup(page.content, features="html.parser")


  