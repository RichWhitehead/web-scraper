import requests 
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Mediterranean_Sea'

def get_soup(URL):
    response = requests.get(URL)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    
    return soup 

response = requests.get(URL)

content = response.content

soup = BeautifulSoup(content, 'html.parser')

result = soup.find_all('a', title= 'Wikipedia:Citation needed')

print (len(result))

for citation in result:
    print (citation.parent.parent.parent.text)