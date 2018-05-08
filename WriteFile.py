from bs4 import BeautifulSoup
import requests


base_url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(base_url)

soup = BeautifulSoup(r.text, "html.parser")

story = soup.select('section.content-section > p')
article = ""
for elem in story:
    article += str(elem)

with open('Article.txt', 'w') as open_file:
    open_file.write(article)