# modules/port_scanner.py

import socket

def scan_ports(target):
    """
    Scan ports 1 to 1024 on the given target IP or domain.
    Args:
        target (str): IP address or domain name to scan
    """

    print(f"\n[+] Scanning target: {target}")

    try:
        # Resolve domain to IP
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("[-] Error: Unable to resolve domain.")
        return

    # Scan first 100 ports (or full 1–1024 if you want)
    for port in range(1, 101):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"    [OPEN] Port {port}")
        s.close()

    print("[✓] Port scan complete.\n")

