#!/usr/bin/python3

import sys
import socket
from datetime import datetime
import pyfiglet

#Define the target
# Scan through given ports FIRST/LAST or do full range scan


if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translate Hostname to IP
    first_port = 1
    last_port = 65535

elif len(sys.argv) == 4:
    target = socket.gethostbyname(sys.argv[1]) #Translate Hostname to IP
    first_port = sys.argv[2]
    last_port = sys.argv[3]

else:
    print("[-] Invalid amount of arguments.")
    print("[-] Usage for full range scan: python3 port_scanner.py <ip or hostname>")
    print("[-] Usage for custom range scan: python3 port_scanner.py <ip> <first port> <last port>")
    sys.exit()



#Add a pretty banner
ascii_banner = pyfiglet.figlet_format("Port Scanner")

print(ascii_banner)

print("[+] Scanning the target " + target)
print(f"[+] Scanning port range: {first_port} to {last_port}")
print("[+] Scan started at " + str(datetime.now()))


def port_scanner(first_port, last_port):

    try:
        for port in range(int(first_port), int(last_port)):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target,port)) # returns an error indicator

            if result == 0:
                print(f"Port {port} is open     ")
                s.close()
            else:
                print(f"[+] Scanning Port {port}", sep='\n', end='\r', flush=True)
                s.close()
                

    except KeyboardInterrupt:
            print("\[-] Exiting script")
            sys.exit()

    except socket.gaierror:
            print("[-] Hostname could not be resolved")
            sys.exit()

    except socket.error:
            print("[-] Couldnt connect to server")
            sys.exit()

port_scanner(first_port,last_port)
