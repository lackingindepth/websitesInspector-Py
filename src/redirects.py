
#Redirects and history of the site
def get_redirects(site):
    if site.history:
            print("Redirects:")
            for response in site.history:
                print(f" - {response.status_code} -> {response.headers.get('Location', 'ABSENT')}")