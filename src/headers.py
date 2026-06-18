
#Headers and server information
def get_headers(site):
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