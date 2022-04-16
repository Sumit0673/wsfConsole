import requests
import threading
from concurrent.futures import ThreadPoolExecutor
import dns.resolver
import sys


# def cname_founder(subd_list):
#     record_types =['CNAME']
#     subdomain=subd_list
#     for records in record_types:
#         try:
#             answer=dns.resolver.resolve(subdomain, records)
#             print(f'{records} Records')
#             print('-'*30)
#             for server in answer:
#                 print(server.to_text() + '\n')
#         except dns.resolver.NoAnswer:
#             print('no record found.')
#             pass
#         except dns.resolver.NXDOMAIN:
#             print(f"""{subdomain} 
#                 CNAME does not exist\n""")
            

#         except Exception as e:
#             print(f'{subd_list}  {e}')
            


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
                        # print("List of subdomain names present in the file\n")
                        # print(sub_dom)
# importing library

  
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
status_list = []
response_code=['Sorry, this page is no longer available.',"If this is your website and you've just created it, try refreshing in a minute",'The specified bucket does not exist','Repository not found','Trying to access your account?','404 Not Found', 'Domain uses DO name serves with no records in DO','404: This page could not be found.','The thing you were looking for is no longer here, or never was',"There isn't a GitHub Pages site here.","404 Blog is not found","We could not find what you're looking for.","No settings were found for this company:","Uh oh. That page doesn't exist.",'is not a registered InCloud YouTrack','No Site For Domain',"It looks like you may have taken a wrong turn somewhere. Don't worry...it happens to all of us.","Tunnel *.ngrok.io not found",'404 error unknown site!',"Sorry, couldn't find the status page",'Project doesnt exist... yet!','Link does not exist','This job board website is either expired or its domain name is invalid.','page not found',"Whatever you were looking for doesn't currently exist at this address","Non-hub domain, The URL you've accessed does not provide a hub.",'page not found','This UserVoice subdomain is currently available!',"Do you want to register *.wordpress.com?","Hello! Sorry, but the website you&rsquo;re looking for doesn&rsquo;t exist." ]

def exists(i):
    try:
        r=requests.get(i)
        print(i + "\tStatus=" + str(r.status_code))
        if str(r.status_code) == '404' or str(r.status_code) == '200':
            status_list.append(i)
            if r.text in response_code:
                
                print("it is vulnerable")
                print("-"*100)
            else:
               
                print("Not vulnerable")
                print("-"*100)
            
        else:
            print(f'{i} has nothing to take over..')
            print("-"*100)
            
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
    # print(sub_domain)
    with ThreadPoolExecutor() as executer:
        executer.map(exists,sub_domain)

    # for i in range(len(status_list)):
    #     cname_founder(status_list[i])