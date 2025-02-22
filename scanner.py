import sys
import socket
import datetime
import threading

# Function to scan a port
def scan_port(target, port):
    # scanning a single port
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target,port)) # error indicator; if 0, port is open
        if result == 0:
            print(f"Port {port} is open")
        s.close()  # Closing the connection
    
    except socket.error as e:
        print(f"Socket error on port {port}: {e}") # For errors such as host name doesn't resolve, timeout (settimeout()), connection gets refused etc.
    
    except Exception as e:
        print(f"Unexpected error on port {port}: {e}") # When not sure what the error is

# Main function - Argument Validation and Target Definition
# python.exe port_scanner.py 192.168.2.3

def main():
    if len(sys.argv) == 2: # number of arguments = 2
        target = sys.argv[1]    # target definition

    else:
        print("Invalid number of arguments")
        print("Usage: python.exe port_scanner.py <target>")
        sys.exit(1) # exiting with a 1 -> exiting with an error; exiting with a 0 -> clean exit

    # Resolve the target hostname to an IP address
    try:
        target_ip = socket.gethostbyname(target)
    
    except socket.gaierror: # hostname resolution issue
        print(f"Error: Unable to resolve hostname {target}")

    sys.exit(1) # exit with error

    # Adding a pretty banner
    print("-" * 50)
    print(f"Scanning target {target_ip}")
    print(f"Time started: {datetime.datetime.now()}")
    print("-" * 50)

    try:
        # Using multithreading to scan ports concurrently
        threads = []
        for port in range(1,65536):
            thread = threading.Thread(target=scan_port,args=(target_ip,port)) # creating a thread for each port
            threads.append(thread)
            thread.start() # not using this will only define the thread, but not execute the thread

        # Best Practise - Wait for all threads to complete
        for thread in threads:
            thread.join()

    except KeyboardInterrupt:
    	print("\nExiting program")
    	sys.exit(0)

    except socket.error as e:
    	print(f"Socket error: {e}")
    	sys.exit(1)

    print("\nScan complete!")

# Best Practise - Prevent this script from being imported (being a main script)
if __name__ == "__main__":
    main()          
# Technical details - Running the program directly sets name to main, but importing it (import scanner.py) sets it to scanner
