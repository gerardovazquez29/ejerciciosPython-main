
import requests
from bs4 import BeautifulSoup

url = "https://escueladirecta.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.prettify())

#for enlace in soup.find_all('a'):
    #print(enlace.get('href'))
    #print(enlace)