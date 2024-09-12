import re
import sys

def unique_ip(logs_file):
    ip_addrs = set()  # Use a set to automatically handle uniqueness
    ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    
    with open(logs_file, 'r') as data:
        for line in data:
            ip_addresses = re.findall(ip_pattern, line)
            ip_addrs.update(ip_addresses)  # Add each IP to the set

    with open('outfile.txt', 'w') as output_file:
        for ip in ip_addrs:
            output_file.write(ip + '\n')  # Write each IP address on a new line

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python unique_ip.py <filename>")
    else:
        unique_ip(sys.argv[1])

