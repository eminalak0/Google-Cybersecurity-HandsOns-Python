# Check if OS needs update
user_os = "Windows 7"
if user_os in ["Windows 7", "Windows 8"]:
    print(f"{user_os} requires an update.")
else:
    print(f"{user_os} is up to date.")

# Check login attempts
approved_users = ["alice", "bob", "charlie"]
login_user = "alice"
login_hour = 10  # 24-hour format

if login_user in approved_users:
    if 9 <= login_hour <= 17:
        print("Login attempt by approved user during work hours.")
    else:
        print("Login attempt by approved user outside work hours.")
else:
    print("Login attempt by unapproved user.")
