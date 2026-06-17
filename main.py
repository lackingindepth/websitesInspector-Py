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
import re
import socket
import ssl
import sys
import requests
import dns.resolver
from requests.exceptions import Timeout, ConnectionError


user_input = input("Enter the URL of the website to inspect: ")

def web_inspec(user_input):

    try:
        site = requests.get(user_input, timeout=(5, 10), allow_redirects=True)
        print(f"URL final: {site.url}")
        print(f"Status Code: {site.status_code}")

        #Redirects
        if site.history:
            print("Redirects:")
            for response in site.history:
                print(f" - {response.status_code} -> {response.headers.get('Location', 'ABSENT')}")
        
        #Headers
        #if security headers absent, can be a security risk, so we will check for them
        print("Security headers:")
        security_headers = [
            'Strict-Transport-Security', #HSTS
            'Content-Security-Policy', #CSP
            'X-Frame-Options',
            'X-Content-Type-Options',
            'Referrer-Policy'
        ]
        for h in security_headers:
            valor = site.headers.get(h, 'ABSENT')
            print(f" - {h}: {valor}")

        #Server informations
        server = site.headers.get('Server', None)
        if server is None:
            print(f"Server: ABSENT")
        elif any(cdn in server.lower()
                 for cdn in ['cloudflare', 'akamai', 'fastly', 'cloudfront']):
            print(f"Server: {server} (CDN detected)")
        elif "/" in server:
            print(f"Server: {server} (Version info may be exposed)")
        else:
            print(f"Server: {server} (Version info not exposed)")

        #Cookies
        print("Cookies:")
        for cookie in site.cookies:
            print(f"{cookie.name}: Secure: {cookie.secure}, HttpOnly: {cookie.has_nonstandard_attr('HttpOnly')}, SameSite: {cookie.get_nonstandard_attr('SameSite', 'ABSENT')}")

        #TLS/SSL details
        parsed_url = re.match(r'^(https?)://([^/]+)', user_input)
        if parsed_url:
            protocol, hostname = parsed_url.groups()
            if protocol == 'https':
                try:
                    context = ssl.create_default_context()
                    with socket.create_connection((hostname, 443), timeout=5) as sock:
                        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                            cert = ssock.getpeercert()
                            print("TLS/SSL details:")
                            print(f" - Subject: {cert.get('subject', 'ABSENT')}")
                            print(f" - Issuer: {cert.get('issuer', 'ABSENT')}")
                            print(f" - Valid from: {cert.get('notBefore', 'ABSENT')}")
                            print(f" - Valid to: {cert.get('notAfter', 'ABSENT')}")
                except Exception as e:
                    print(f"Error fetching TLS/SSL details: {e}")
            else:
                print("The website does not use HTTPS, so TLS/SSL details are not available.")
        else:
            print("Invalid URL format. Unable to extract hostname for TLS/SSL details.")

        #DNS
        try:
            ip_address = socket.gethostbyname(hostname)
            print(f"DNS: {hostname} resolves to {ip_address}")
        except Exception as e:
            print(f"Error resolving DNS: {e}")

        print("DNS records:")
        for record_type in ['A', 'AAAA', 'CNAME', 'MX', 'TXT']:
            try:
                answers = dns.resolver.resolve(hostname, record_type)
                for rdata in answers:
                    print(f" - {record_type}: {rdata.to_text()}")
            except dns.resolver.NoAnswer:
                print(f" - {record_type}: No records found")
            except dns.resolver.NXDOMAIN:
                print(f" - {record_type}: Domain does not exist")

        print(f"Response time: {site.elapsed.total_seconds()} seconds")
    except (Timeout, ConnectionError) as e:
        print(f"Error occurred while fetching the website: {e}")
        sys.exit(1)

   
web_inspec(user_input)


