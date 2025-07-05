# modules/dns_lookup.py

import dns.resolver

def dns_lookup(domain):
    """
    Performs DNS lookup for A, MX, and NS records.
    Args:
        domain (str): Domain name to query
    """

    print(f"\n[+] Performing DNS lookup for: {domain}")

    # A Record
    try:
        a_records = dns.resolver.resolve(domain, 'A')
        print("\n[+] A Records (IP Addresses):")
        for rdata in a_records:
            print(f"    {rdata.to_text()}")
    except Exception as e:
        print(f"    [!] A Record Error: {e}")

    # MX Record
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        print("\n[+] MX Records (Mail Servers):")
        for rdata in mx_records:
            print(f"    {rdata.exchange} (Priority: {rdata.preference})")
    except Exception as e:
        print(f"    [!] MX Record Error: {e}")

    # NS Record
    try:
        ns_records = dns.resolver.resolve(domain, 'NS')
        print("\n[+] NS Records (Name Servers):")
        for rdata in ns_records:
            print(f"    {rdata.to_text()}")
    except Exception as e:
        print(f"    [!] NS Record Error: {e}")

    print("\n[✓] DNS lookup complete.\n")

