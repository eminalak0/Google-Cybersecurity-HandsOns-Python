import re

# Sample log data
log_data = """
User: alice, Device ID: DEV-A12X, IP: 192.168.1.101
User: bob, Device ID: DEV-B44Z, IP: 10.0.0.4
User: charlie, Device ID: DEV-C77M, IP: 172.16.0.99
"""

# Extract device IDs that contain "A" or "C"
device_ids = re.findall(r'DEV-[AC]\w+', log_data)
print("Filtered Device IDs:", device_ids)

# Extract all IP addresses from log
ip_addresses = re.findall(r'\d+\.\d+\.\d+\.\d+', log_data)
print("All IP addresses found:", ip_addresses)

# Compare against a flagged IP list
flagged_ips = ["10.0.0.4", "8.8.8.8"]
for ip in ip_addresses:
    if ip in flagged_ips:
        print(f"⚠️ Flagged IP detected: {ip}")
    else:
        print(f"✔️ IP is clean: {ip}")
