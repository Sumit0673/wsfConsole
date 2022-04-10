import dns.resolver
import sys
# record_types = ['A','AAAA','NS','CNAME','MX','PTR','SOA','TXT']
def cname_founder(subd_list):
    record_types =['CNAME']
    subdomain=subd_list
    for records in record_types:
        try:
            answer=dns.resolver.resolve(subdomain, records)
            print(f'{records} Records')
            print('-'*30)
            for server in answer:
                print(server.to_text() + '\n')
        except dns.resolver.NoAnswer:
            print('no record found.')
            pass
        except dns.resolver.NXDOMAIN:
            print(f'{subdomain} CNAME does not exist')
            

        except Exception as e:
            print(f'{subd_list}  {e}')

subdomain = ['https://www.geeksforgeeks.org', 'https://api.geeksforgeeks.org', 'https://news.geeksforgeeks.org', 'https://marketing.geeksforgeeks.org', 'https://media.geeksforgeeks.org', 'https://origin.geeksforgeeks.org']

for i in range(len(subdomain)):
    cname_founder(subdomain[i])