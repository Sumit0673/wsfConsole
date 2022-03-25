import time
from concurrent.futures import ProcessPoolExecutor

m= time.perf_counter()
def scrap(q):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    # from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    # d = DesiredCapabilities.CHROME
    # d['loggingPrefs'] = { 'browser':'ALL' }

    # driver = webdriver.Chrome(desired_capabilities=d)
    # chrome_options = Options()

    # #chrome_options.add_argument("--disable-extensions")

    # #chrome_options.add_argument("--disable-gpu")

    # chrome_options.add_argument("--headless")
    driver= webdriver.Chrome("C:\\Users\\Sumit\\OneDrive\\Desktop\\chromedriver.exe", )
    
    driver.get("https://www.google.com")

    for entry in driver.get_log('browser'):
    
        print(entry)
    

    
    21
    # search.click()
    # driver.switch_to_alert.dismiss()
    # search.click()
    # driver.switch_to_alert.accept()
    # driver.switchTo().alert().getText()
    for s in search:
        s.send_keys(q)


List = ['<script\x20type="text/javascript">console.log("test success...")</script>', 
'<script\x3Etype="text/javascript">console.log("test success...")</script>',
'<script\x0Dtype="text/javascript">console.log("test success...")</script>',
'<script\x09type="text/javascript">console.log("test success...")</script>',
'<script\x0Ctype="text/javascript">console.log("test success...")</script>',
'<script\x2Ftype="text/javascript">console.log("test success...")</script>',
'<script\x0Atype="text/javascript">console.log("test success...")</script>']

def main():
    
    with ProcessPoolExecutor(max_workers = 3) as executor:
        executor.map(scrap, List)

if __name__ == "__main__":
    main()
    
    n=time.perf_counter()
    time_required=n-m
    print(f"Time required during the process: {time_required}")

