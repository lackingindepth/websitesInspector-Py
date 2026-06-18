"""-----------------------------------------------------------
WeB Inspector - A simple web inspector tool to analyze and extract information from websites.

♣ Input: A URL of the website to inspect.

♣ Output: A report containing the following information:
    - Headers HTTP
    - Status code
    - Response time
    - Server information
    - TLS/SSL details
    - Cookies
    - Technologies used (e.g., CMS, frameworks, libraries)
    - HSTS status
    - CSP (Content Security Policy) 
-----------------------------------------------------------"""
import sys
import requests
from requests.exceptions import Timeout, ConnectionError
from src.cookies import get_cookies
from src.headers import get_headers
from src.redirects import get_redirects
from src.TLS import get_tls_details
from src.dynamicNS import get_dns_records



user_input = input("Enter the URL of the website to inspect: ")

def web_inspec(user_input):

    try:

        site = requests.get(user_input, timeout=(5, 10), allow_redirects=True)
        #outputs
        print(f"URL final: {site.url}")
        print(f"Status Code: {site.status_code}")
        print(f"Response time: {site.elapsed.total_seconds()} seconds")
        get_headers(site)
        get_redirects(site)
        get_tls_details(site, user_input)
        get_dns_records(user_input)
        get_cookies(site)

    except (Timeout, ConnectionError) as e:
        print(f"Error occurred while fetching the website: {e}")
        sys.exit(1)

   
web_inspec(user_input)


