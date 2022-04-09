
with open('C:/Users/Sumit/OneDrive/Documents/DOC/Sumit/subdomain_names.txt','r') as file:
    
    # reading the file
    name = file.read()
      
    # using spilitlines() function storing the list
    # of spitted strings
    sub_dom = name.splitlines()
      
    # printing number of subdomain names present in
    # the list
    print(f"Number of subdomain names present in the file are: {len(sub_dom)}\n")
      
    # printing list of subdomain names present in the 
    # text file
    print("List of subdomain names present in the file\n")
    print(sub_dom)
# importing library
import requests
import threading
from concurrent.futures import ThreadPoolExecutor

  
# function for scanning subdomains
sub_domain=[]
def domain_scanner(domain_name,sub_domnames):
    print('-----------Scanner Started-----------')
    print('----URL after scanning subdomains----')
      
    # loop for getting URL's
    for subdomain in sub_domnames:
        
        # making url by putting subdomain one by one
        url = f"https://{subdomain}.{domain_name}"
          
        # using try catch block to avoid crash of
        # the program
        try:
            
            # sending get request to the url
            requests.get(url)
              
            # if after putting subdomain one by one url 
            # is valid then printing the url
            print(f'[+] {url}')
            sub_domain.append(url)
              
        # if url is invalid then pass it
        except requests.ConnectionError:
            pass
    print('\n')
    print('----Scanning Finished----')
    print('-----Scanner Stopped-----')
def exists(i):
    try:
        r=requests.get(i)
        print(i + "\tStatus=" + str(r.status_code))
    except Exception as e:
        print(i +"\tNA CONNECTION Failed\t" + str(e))
            
  
# main function
if __name__ == '__main__':
    
    # inputting the domain name
        dom_name = input("Enter the Domain Name:")
        print('\n')
    
        # opening the subdomain text file
        with open('C:/Users/Sumit/OneDrive/Documents/DOC/Sumit/subdomain_names.txt','r') as file:
            
            # reading the file
            name = file.read()
            
            # using spilitlines() function storing the 
            # list of splitted strings
            sub_dom = name.splitlines()
            
        # calling the function for scanning the subdomains
        # and getting the url
        domain_scanner(dom_name,sub_dom)
        print(sub_domain)
        with ThreadPoolExecutor() as executer:
            executer.map(exists,sub_domain)