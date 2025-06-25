# Working with employee IDs
emp_id_number = 456
emp_prefix = "EMP"
full_emp_id = emp_prefix + str(emp_id_number)
print("Full Employee ID:", full_emp_id)
print("Length of Employee ID string:", len(full_emp_id))

# Extracting parts of a device ID using indexing
device_id = "DEV12345X"
print("First 3 characters (prefix):", device_id[:3])
print("Numeric section:", device_id[3:8])
print("Last character (type flag):", device_id[-1])

# Working with a URL using .index() and slicing
url = "https://companysite.com/devices/ABC123"
slash_index = url.index("/devices/")
device_segment = url[slash_index + 9:]  # Get the part after '/devices/'
print("Extracted device ID from URL:", device_segment)
