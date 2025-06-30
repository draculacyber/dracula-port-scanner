
# 🧛 Dracula Port Scanner

A basic TCP port scanner built using Python and the `socket` library.

## 🔍 What It Does

This script scans common ports on a given IP address (e.g. 192.168.x.x)  
to check whether each port is open or closed.

## 🛠️ How It Works

- Accepts IP address input from the user
- Scans ports 21, 22, 23, 25, 53, 80, 110, and 443
- Prints open or closed status for each port

## ⚙️ How to Run

1. Make sure you have Python installed
2. Save the script as `dracula-port-scanner.py`
3. Run it using:
   ```bash
   python dracula-port-scanner.py
Enter the IP address to scan (e.g. 192.168.1.1)

🧪 Example Output
swift
Copy
Edit
Scanning 192.168.1.1...
[-] Port 21 is CLOSED
[-] Port 22 is OPEN
...
🎯 Why I Built This
As part of my journey to become a Cybersecurity Consultant,
I'm learning how ports work, how scanners operate,
and how to script basic security tools from scratch.
