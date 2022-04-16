import requests
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.chrome.options import Options
chromedriver_autoinstaller.install()

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

spec_char=['<','>','.','"',"'",'$','*']


# url="https://xss-game.appspot.com"
 
# for i in spec_char:
def main(url):
    def filteration(spec_char):
        # spec_char='<'
        driver = webdriver.Chrome(service=Service(), chrome_options=options)
        # driver = webdriver.Chrome("C:\\Users\\Sumit\\OneDrive\\Desktop\\ProposalsCyberlabs\\chromedriver.exe")
        driver.get(url) 
        ele = driver.find_element_by_tag_name("input")
        ele.send_keys(spec_char)
        ele.send_keys(Keys.ENTER)
        time.sleep(5)
        elem = driver.find_element_by_tag_name("input").get_attribute("value")
        # elem= driver.find_element(by=By.TAG_NAME("input"), value=name)
        if elem == spec_char:
            chars=spec_char
            return chars

    with ThreadPoolExecutor() as executer:
        filtered = executer.map(filteration, spec_char)
        print([x for x in filtered])
# main(url)

