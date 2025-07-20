# daily_reminder.py

# Ask the user for the task
task = input("Enter your task: ")

# Ask the user for priority level
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to handle different priorities
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Task: '{task}' has an unknown priority level"

# Modify the message if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif "Note:" not in reminder:
    reminder += " — plan accordingly."

# Print the final reminder
print(reminder)

