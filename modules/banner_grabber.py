# modules/banner_grabber.py

import socket

def grab_banner(ip, port):
    """
    Attempts to grab the service banner of a given IP and port.
    Args:
        ip (str): Target IP address
        port (int): Target port number
    """
    print(f"\n[+] Grabbing banner from {ip}:{port}...\n")

    try:
        # Create socket connection
        s = socket.socket()
        s.settimeout(3)
        s.connect((ip, port))
        banner = s.recv(1024).decode().strip()
        s.close()

        if banner:
            print(f"[+] Banner: {banner}")
        else:
            print("[!] No banner received.")
    except Exception as e:
        print(f"[!] Error grabbing banner: {e}")

