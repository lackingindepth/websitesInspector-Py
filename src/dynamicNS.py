
import socket
import dns.resolver

#DNS records retrieval function
def get_dns_records(hostname):
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
