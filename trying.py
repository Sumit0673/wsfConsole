import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from concurrent.futures import ProcessPoolExecutor

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

def scan_xss(js_script):
    """
    Given a `url`, it prints all XSS vulnerable forms and 
    returns True if any is vulnerable, False otherwise
    """
    # https://xss-game.appspot.com/level1/frame
    # get all the forms from the URL
    forms = get_all_forms('https://xss-game.appspot.com/level1/frame')
    print(f"[+] Detected {len(forms)} forms on {'https://xss-game.appspot.com/level1/frame'}.")
    # returning value
    is_vulnerable = False
    # iterate over all forms
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, 'https://xss-game.appspot.com/level1/frame', js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {'https://xss-game.appspot.com/level1/frame'}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
            # won't break because we want to print available vulnerable forms
    return is_vulnerable

if __name__ == "__main__":
    List = ['<script\x20type="text/javascript">console.log("test success...")</script>', 
    '<script\x3Etype="text/javascript">console.log("test success...")</script>',
    '<script\x0Dtype="text/javascript">console.log("test success...")</script>',
    '<script\x09type="text/javascript">console.log("test success...")</script>',
    '<script\x0Ctype="text/javascript">console.log("test success...")</script>',
    '<script\x2Ftype="text/javascript">console.log("test success...")</script>',
    '<script\x0Atype="text/javascript">console.log("test success...")</script>']

    test_str = ['<sumit']
    with ProcessPoolExecutor(max_workers = 3) as executor:
        Filter = executor.map(scan_xss, test_str)
    print([x for x in Filter])


    if Filter==True :
    # printing original list
            print("The original list is : " + str(List))
  
# Remove List elements containing String character
# Using loop
            res = []
            for sub in test_list:
                flag = 0
                for ele in sub:
                    if ele in test_str:
                        flag = 1
                if not flag:
                    res.append(sub)
  
# printing result 
                print("The list after removal : " + str(res))

    




    with ProcessPoolExecutor(max_workers = 3) as executor:
        result = executor.map(scan_xss, List)

    print([x for x in result])
