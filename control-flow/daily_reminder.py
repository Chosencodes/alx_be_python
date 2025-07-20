# daily_reminder.py

# Ask the user to input a task
task = input("Enter your task: ")

# Ask for the priority of the task
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize reminder message
reminder = ""

# Match-case statement for different priority levels
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a HIGH priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a LOW priority task."
    case _:
        reminder = f"Reminder: '{task}' has an UNKNOWN priority."

# If statement to modify the reminder if it's time-bound
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
else:
    reminder += " Please plan accordingly."

# Final customized reminder
print(reminder)

