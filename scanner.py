#!/bin/python3

import sys
import os
import socket
from datetime import datetime as dt

# Syntax: ./Port\ Scanner.py <ip_addr>

# checking arguments and defining our target
if len(sys.argv) == 1:
	target = socket.gethostbyname(argv[0]) # translating hostname to IPv4
else:
	print("[+] Invalid number of arguments")
	print("[+] Syntax: ./Port\ Scanner.py <ip_addr>")

print("[+] Scanning target " + target)
print("[+] Time started: " + str(dt.now()))

try:
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setdefaulttimeout(1) # setting a default timeout of 1 sec when making a connection
		result = s.connect_ex((target, port)) # returns an error indicator
		if result == 0:
			print("Port {} is open".format(port))
		s.close()

except KeyboardInterrupt:
	print("[+] \nExiting program")
	sys.exit()

except socket.gaierror:
	print("[+] Hostname couldn't be resolved") # Handling DNS failure
	sys.exit()

except socket.error:
	print("[+] Couldn't connect to the host, please try again") # Handling connection failure
	sys.exit()
