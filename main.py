import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://www.docstring.fr/api/books_to_scrape/index.html"
response = requests.get(url)
print(response.status_code)

soup  = BeautifulSoup(response.text, 'html.parser')

#fonction pour parcourir récursivement l'arbre DOM
#def traverse_dom(element, level=0):
#    #Afficher l'élement actuel
#    if element.name:
#        print(f'{' '* level}<{element.name}>')
#    
#    #Si l'élément à des enfants, les parcourir également
#    if hasattr(element, 'children'):
#        for child in element.children:
#            traverse_dom(child, level +1)
#
##Commencer le parcours depuis la racine de l'arbre Dom
#traverse_dom(soup)


#Lister tous le body
#body= soup.find_all("body")
#print(body)

#Lister toutes les images
#images = soup.find_all('img')
#pprint(images) 

# Ou avec plus de précision
images = soup.find_all('article', class_="product_pod")
pprint(images)  