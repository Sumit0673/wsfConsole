import xmltodict 
import requests 
url1 = input("enter the url :")
site_map = xmltodict.parse(requests.get(url1).text)
urls = [url["loc"] for url in site-map["urlset"]["url"]]
print("\n" .join(urls[0:3]))
