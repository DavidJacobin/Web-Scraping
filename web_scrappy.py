from bs4 import BeautifulSoup

with open("index.html", 'r') as file:

    doc = BeautifulSoup(file, "html.parser")

tag_title = doc.title
#print(tag_title)

tag_title.string = 'hello'
#print(tag_title)

tag_all_p = doc.findAll('p')
#print(tag_all_p)

tag_all_p = doc.findAll('p')[0]
#print(tag_all_p.findAll('b'))