import requests
import time
from tabulate import tabulate

# List of subdomains to check from Google.com (listed few):
subdomains = [
    'https://mail.google.com',
    'https://drive.google.com',
    'https://calndar.google.com',   
    # mentioned wrong URL just to showcase the down status due to connection error.
    'https://ads.google.com',
    'https://support.google.com'
]

while True:
    status_all = []
    for subdomain in subdomains:
        try:
            response = requests.get(subdomain, timeout=2)
            if response.status_code == 200:
                status = 'Up'
            else: 
                status = 'Down'
        except requests.ConnectionError:
            status = 'Down'
        status_all.append([subdomain, status])
    table = tabulate(status_all, headers=['Subdomain', 'Status'], tablefmt='grid')
    print(table)
    time.sleep(60) # creating sleep timer of 60secs for each run, meanwhile "While" loop will run forever.