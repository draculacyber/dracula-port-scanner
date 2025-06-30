# 🦇 Dracula Port Scanner

A sleek PowerShell-based port scanner built by DraculaCyber — designed for ethical hacking, cybersecurity training, and local network reconnaissance.

## ⚔️ Features

- Scan custom IP addresses and port ranges
- See which ports are open or closed
- Built entirely in **PowerShell**
- Lightweight, fast, and easy to run
- Great for students and aspiring cybersecurity consultants

---

## 🧪 How It Works

The scanner tries to connect to each specified port on a given IP address. If it connects, the port is **open**. If not, it’s **closed**. This script uses `System.Net.Sockets.TcpClient` for low-level socket testing.

---

## 🧠 Usage

```powershell
.\dracula-scan.ps1
You’ll be prompted to enter:

Target IP (e.g. 192.168.1.1)

Start Port (e.g. 20)

End Port (e.g. 80)

The script will check each port and return the status.

📦 Example Output
pgsql
Copy
Edit
Port 22 is OPEN
Port 23 is CLOSED
Port 80 is OPEN
Scan complete.
🛡️ Disclaimer
This script is intended for educational and ethical testing only. Do not use it on systems you do not own or have permission to test.

🧛 About the Creator
Built by DraculaCyber, a rising cybersecurity consultant on a mission to build a powerful arsenal of tools and knowledge.

Follow the journey, contribute ideas, or fork this tool to upgrade your own security toolkit.

