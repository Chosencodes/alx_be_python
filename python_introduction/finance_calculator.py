# finance_calculator.py

# Prompt user for income and expenses
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Calculate annual savings
annual_savings = monthly_savings * 12

# Calculate interest (5% of annual savings)
interest = annual_savings * 0.05

# Projected savings after 1 year with interest
projected_savings = annual_savings + interest

# Display results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")

