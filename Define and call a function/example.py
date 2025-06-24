# Simple loop to simulate network connection attempts
for attempt in range(1, 6):
    print(f"Attempt {attempt}: Connecting to network...")

# For loop to check login IP addresses against allowed IPs
allowed_ips = ["192.168.1.10", "192.168.1.20", "10.0.0.5"]
login_ips = ["192.168.1.10", "192.168.1.50", "10.0.0.5"]

for ip in login_ips:
    if ip in allowed_ips:
        print(f"Login from allowed IP: {ip}")
    else:
        print(f"Login attempt from unauthorized IP: {ip}")

# While loop to generate unique employee IDs
employee_id = 1000
new_employees = 5
generated_ids = []

while new_employees > 0:
    generated_ids.append(employee_id)
    employee_id += 1
    new_employees -= 1

print("Generated employee IDs:", generated_ids)
