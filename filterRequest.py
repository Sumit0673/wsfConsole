import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:\\Users\\Sumit\\OneDrive\\Desktop\\ProposalsCyberlabs\\chromedriver.exe")
driver.get(input("Enter the url : "))
ele = driver.find_element_by_tag_name("input")
payload = input("Enter character : ")
ele.send_keys(payload)
ele.send_keys(Keys.ENTER)
time.sleep(5)
elem = driver.find_element_by_tag_name("input").get_attribute("value")

if elem == payload:
    print("Not filtered...")

# """ charachters:<Cyberlabs
#                 >Cyberlabs
#                 /Cyberlabs
#                 "Cyberlabs"
#                 'Cyberlabs'
#                 `Cyberlabs`
#                 \Cyberlabs
#                 (Cyberlabs)
#                 *Cyberlabs
#                 %Cyberlabs"""
