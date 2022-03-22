from threading import Thread 
from URLSearchParams import URLSearchParams


def webscrap(url):
    import requests 
    from bs4 import BeautifulSoup
    url = input("enter the url:")
    content = requests.get(url)
    html_content = content.content
    soup = BeautifulSoup(html_content,'html.parser')
    print(soup)







