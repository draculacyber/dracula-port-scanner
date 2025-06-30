import socket
import datetime

print("🧛 Starting Dracula Port Scanner...")
target = input("Enter target IP address: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))
print(f"Scanning {target} from port {start_port} to {end_port}...\n")

start_time = datetime.datetime.now()

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"🟥 Port {port} is OPEN")
    sock.close()

end_time = datetime.datetime.now()
print(f"\nScan completed in: {end_time - start_time}")
