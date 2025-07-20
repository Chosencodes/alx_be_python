# daily_reminder.py

# Prompt for task
task = input("Enter your task: ")

# Prompt for priority
priority = input("Priority (high/medium/low): ").lower()

# Prompt for time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process using match-case and if
match priority:
    case "high" | "medium" | "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level entered.")

