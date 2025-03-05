import socket
import threading

# Function to scan a single port
def scan_port(target, port):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Set timeout for faster scanning

        # Try to connect to the target port
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        s.close()
    except:
        pass

# Main function
def port_scanner(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}...\n")

    # Creating threads for faster scanning
    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("\nScanning complete.")

# Taking user input
if __name__ == "__main__":
    target_ip = input("Enter target IP or domain: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    
    port_scanner(target_ip, start_port, end_port)
