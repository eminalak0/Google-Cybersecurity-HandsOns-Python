# Simulate reading a file containing allowed IPs
with open("allowlist.txt", "r") as file:
    allowlist_data = file.read()

# Convert string to list of IP addresses
allowlist = allowlist_data.strip().split("\n")

# List of IPs that should no longer have access
revoked_ips = ["192.168.1.10", "10.0.0.8"]

# Remove revoked IPs from the allowlist
updated_allowlist = [ip for ip in allowlist if ip not in revoked_ips]

# Write updated list back to a new file
with open("updated_allowlist.txt", "w") as file:
    for ip in updated_allowlist:
        file.write(ip + "\n")

print("✅ Updated allowlist written to 'updated_allowlist.txt'.")
