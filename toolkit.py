from modules import port_scanner
from modules import brute_force
from modules import whois_lookup
from modules import dns_lookup
from modules import banner_grabber

def main():
    while True:
        print("""
        === Penetration Testing Toolkit ===
        1. Port Scanner
        2. SSH Brute Force
        3. WHOIS Lookup
        4. DNS Lookup
        5. Banner Grabbing
        0. Exit
        """)

        choice = input("Enter your choice: ")

        if choice == '1':
            target = input("Enter target IP/domain: ")
            port_scanner.scan_ports(target)

        elif choice == '2':
            ip = input("Enter target IP address: ")
            username = input("Enter SSH username: ")
            pwd_file = input("Enter path to password list file: ")

            try:
                with open(pwd_file, 'r') as f:
                    passwords = f.read().splitlines()
                brute_force.ssh_brute_force(ip, username, passwords)

            except FileNotFoundError:
                print("[!] Password file not found.")
            except Exception as e:
                print(f"[!] Error: {e}")

        elif choice == '3':
            domain = input("Enter domain name (e.g., google.com): ")
            whois_lookup.lookup_domain(domain)

        elif choice == '4':
            domain = input("Enter domain name (e.g., openai.com): ")
            dns_lookup.dns_lookup(domain)

        elif choice == '5':
            ip = input("Enter target IP address: ")
            port = int(input("Enter port to grab banner from: "))
            banner_grabber.grab_banner(ip, port)

        elif choice == '0':
            print("Exiting Toolkit...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

