from datetime import datetime, timedelta

# Get the current datetime
now = datetime.now()

# Set the datetime for New Year's Eve of 2023
new_year = datetime(2023, 12, 31)

# Calculate the time between now and New Year's Eve
time_to_new_year = new_year - now

# Create a timedelta object representing 7 days
seven_days = timedelta(days=7)

# Calculate the datetime 7 days from now
time_in_seven_days = now + seven_days

# Print the datetime 7 days from now
print(time_in_seven_days)
