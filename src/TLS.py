
#TLS/SSL details
import re
import socket
import ssl

def get_tls_details(hostname, user_input):
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