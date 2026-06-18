
import requests

#get cookies from the site
def get_cookies(site):
    print("Cookies:")
    for cookie in site.cookies:
        print(f"{cookie.name}: Secure: {cookie.secure}, HttpOnly: {cookie.has_nonstandard_attr('HttpOnly')}, SameSite: {cookie.get_nonstandard_attr('SameSite', 'ABSENT')}")