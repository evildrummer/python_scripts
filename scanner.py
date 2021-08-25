#!/usr/bin/python3

import sys
import socket
from datetime import datetime
import pyfiglet

#Define the target

if len(sys.argv) >= 3:
        target = socket.gethostbyname(sys.argv[1]) #Translate Hostname to IP
else:
    print("invalid amount of arguments.")
    print("usage: python3 port_scanner.py <ip> <first port> <last port>")

first_port = sys.argv[2]
last_port = sys.argv[3]

#Add a pretty banner
ascii_banner = pyfiglet.figlet_format("PNPT Scanner")

print(ascii_banner)


print("[+] Scanning the target " + target)
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
                print(f"[+] Scanning Port {port}", sep='\n', end='\r', flush=True) #overwrites the scanned port until open port is found
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
