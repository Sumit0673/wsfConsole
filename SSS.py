import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import colorama
# init the colorama module
class webCrawler:
    # global total_urls_visited
    def __init__(self, url,total_urls_visited):
        self.total_urls_visited = total_urls_visited 
        self.url=url
        colorama.init()
        self.GREEN = colorama.Fore.GREEN
        self.GRAY = colorama.Fore.LIGHTBLACK_EX
        self.RESET = colorama.Fore.RESET
        self.YELLOW = colorama.Fore.YELLOW
        # initialize the set of links (unique links)
        self.internal_urls = set()
        self.external_urls = set()
    def is_valid(self, url):
   
   
        parsed = urlparse(self.url)
        return bool(parsed.netloc) and bool(parsed.scheme)
    def get_all_website_links(self, url):
    
        # all URLs of `url`
        urls = set()
        # domain name of the URL without the protocol
        domain_name = urlparse(self.url).netloc
        soup = BeautifulSoup(requests.get(self.url).content, "html.parser")


        for a_tag in soup.findAll("a"):
            href = a_tag.attrs.get("href")
            if href == "" or href is None:
          
                continue
          
            href = urljoin(self.url, href)
            parsed_href = urlparse(href)
        
            href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
            if not self.is_valid(href):
                # not a valid URL
                continue
            if href in self.internal_urls:
            # already in the set
                continue
            if domain_name not in href:
            # external link
                if href not in self.external_urls:
                    print(f"{self.GRAY}[!] External link: {href}{self.RESET}")
                    self.external_urls.add(href)
                continue
            print(f"{self.GREEN}[*] Internal link: {href}{self.RESET}")
            urls.add(href)
            self.internal_urls.add(href)
        return urls
    # number of urls visited so far will be stored here
    # total_urls_visited = 0

    def crawl(self, url, max_urls, all):
    
        # global total_urls_visited
        self.total_urls_visited +=1
        print(f"{self.YELLOW}[*] Crawling: {url}{self.RESET}")
        links = self.get_all_website_links(url)
        for link in links:
            all.append(link)
            if self.total_urls_visited > max_urls:
                break
            self.crawl(link, max_urls, all)

# url=input("ENTER THE url: ")
# g=webCrawler(url, 0)
# if __name__ == "__main__":
#     a = []
#     g.crawl(url, 30, a)
#     print("[+] Total Internal links:", len(g.internal_urls))
#     print("[+] Total External links:", len(g.external_urls))
#     print("[+] Total URLs:", len(g.external_urls) + len(g.internal_urls))

#     print(a)
