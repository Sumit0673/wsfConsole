from threading import Thread 
from URLSearchParams import URLSearchParams
from lxml import etree


def webscrap(url):
    import requests 
    from bs4 import BeautifulSoup
    content = requests.get(url)
    html_content = content.content
    soup = BeautifulSoup(html_content,'html.parser')
    print(soup.prettify())
    dom = etree.HTML(str(soup))
    print(dom.xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')[0].text)


webscrap("https://www.google.com")





