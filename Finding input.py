from selenium import webdriver
q=input("enter the url:")
driver= webdriver.Chrome("C:\\Users\\Sumit\\OneDrive\\Desktop\\chromedriver.exe")
driver.get(q)
search = driver.find_elements_by_tag_name("input")
for s in search:
    s.send_keys("xss")
