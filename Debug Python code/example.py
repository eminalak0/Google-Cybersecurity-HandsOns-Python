# This is the buggy version
users = {"alice": 3, "bob": 0, "charlie": 5}

for user in users:
    print("Checking:", user)
    print("Login attempts:", users[user])
    print("Average per day:", 10 / users[user])  # This will crash for 'bob'

if user = "alice"
    print("Alice has admin access")


# Fixed version with debugging strategies
users = {"alice": 3, "bob": 0, "charlie": 5}

for user in users:
    print("Checking:", user)
    print("Login attempts:", users[user])

    try:
        average = 10 / users[user]
        print("Average per day:", average)
    except ZeroDivisionError:
        print("⚠️ Cannot divide by zero — login attempts are zero!")

# Logic and syntax fixed
if user == "alice":
    print("Alice has admin access")
