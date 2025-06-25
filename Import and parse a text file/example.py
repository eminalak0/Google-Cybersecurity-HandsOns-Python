# Read from an existing file
with open("device_log.txt", "r") as file:
    log_data = file.read()

print("Original Log Data:")
print(log_data)

# Split the log into a list of lines
log_lines = log_data.split("\n")
print("\nParsed Lines:")
print(log_lines)

# Append a new entry to the log
new_entry = "User: david, Device: LAPTOP-9, Status: active"
with open("device_log.txt", "a") as file:
    file.write("\n" + new_entry)

# Create a new file and write filtered data
filtered_lines = [line for line in log_lines if "active" in line]
with open("active_devices.txt", "w") as file:
    for line in filtered_lines:
        file.write(line + "\n")

print("\nNew file 'active_devices.txt' created with active entries.")
