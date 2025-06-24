# Simple loop simulating network connection attempts
for attempt in range(1, 6):
    print(f"Attempting to connect to network, try {attempt}...")

# For loop comparing login IPs with allowed IPs
allowed_ips = ["192.168.1.10", "192.168.1.15", "192.168.1.20"]
login_attempt_ips = ["192.168.1.10", "10.0.0.5", "192.168.1.20"]

for ip in login_attempt_ips:
    if ip in allowed_ips:
        print(f"Login attempt from allowed IP: {ip}")
    else:
        print(f"Login attempt from unauthorized IP: {ip}")

# While loop to generate unique employee IDs
employee_id = 1000
max_employees = 5
ids_generated = []

while len(ids_generated) < max_employees:
    ids_generated.append(employee_id)
    print(f"Generated employee ID: {employee_id}")
    employee_id += 1
