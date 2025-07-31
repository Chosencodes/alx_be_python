from datetime import datetime

def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

# Call the function to display date and time
display_current_datetime()

