# Initial lists
approved_users = ["alice", "bob", "charlie"]
user_devices = ["laptop-1", "desktop-2", "tablet-3"]

# Add a new user and their device
approved_users.append("david")
user_devices.append("phone-4")

# Remove a user who left the company
approved_users.remove("bob")
user_devices.pop(1)  # Remove bob's device

# Check if a user is approved
user_check = "david"
if user_check in approved_users:
    print(f"{user_check} is approved to access the system.")
else:
    print(f"{user_check} is NOT approved to access the system.")

# Match device to user by index
device_check = "tablet-3"
if device_check in user_devices:
    device_index = user_devices.index(device_check)
    corresponding_user = approved_users[device_index]
    print(f"Device '{device_check}' is assigned to user: {corresponding_user}")
else:
    print("Device not found in the system.")
