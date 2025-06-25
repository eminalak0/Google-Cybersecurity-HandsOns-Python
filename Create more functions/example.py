# Sample data: number of failed login attempts over the last 7 days
failed_logins = [12, 5, 9, 18, 4, 6, 22]

# Use built-in functions to analyze the data
max_attempts = max(failed_logins)
sorted_attempts = sorted(failed_logins)

print(f"Maximum failed login attempts in a day: {max_attempts}")
print(f"Sorted failed login attempts: {sorted_attempts}")

# Define a function to compare today's failed logins to the average
def analyze_login_activity(today_count, login_history):
    average = sum(login_history) / len(login_history)
    print(f"Today's failed logins: {today_count}")
    print(f"Average failed logins: {average:.2f}")

    if today_count > average:
        return "Warning: Today's failed login attempts are above average."
    else:
        return "Normal: Today's login activity is within normal range."

# Call the function and print the result
today_failed_logins = 17
result = analyze_login_activity(today_failed_logins, failed_logins)
print("Analysis Result:", result)
