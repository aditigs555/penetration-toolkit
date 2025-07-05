# modules/whois_lookup.py

import whois  # Library to get WHOIS info

def lookup_domain(domain):
    """
    Perform WHOIS lookup on the given domain.
    Args:
        domain (str): The target domain name (e.g., google.com)
    """

    print(f"\n[+] Performing WHOIS lookup for: {domain}\n")

    try:
        info = whois.whois(domain)

        # Display selected WHOIS information
        print(f"    Domain Name: {info.domain_name}")
        print(f"    Registrar: {info.registrar}")
        print(f"    Creation Date: {info.creation_date}")
        print(f"    Expiration Date: {info.expiration_date}")
        print(f"    Country: {info.country}")
        print(f"    Organization: {info.org}")

    except Exception as e:
        print(f"[!] Failed to perform WHOIS lookup: {e}")

