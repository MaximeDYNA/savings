# Initial amount saved on the first day
initial_savings = 100

# Total number of days in a year
total_days = 365

# Initialize the total savings
total_savings = 0

# Loop over each day of the year
for day in range(1, total_days + 1):
    # Calculate savings for the current day
    daily_savings = initial_savings * day
    # Add the daily savings to the total savings
    total_savings += daily_savings

# Print the total savings at the end of the year
print(f"The total savings after {total_days} days is: {total_savings} FCFA")
