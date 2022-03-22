import requests 
from bs4 import BeautifulSoup
url = input("enter the url:")
content = requests.get(url)
html_content = content.text
soup = BeautifulSoup(html_content,'html.parser')
print(soup.prettify())
