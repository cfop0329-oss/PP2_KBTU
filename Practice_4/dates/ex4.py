from datetime import datetime

# Define two datetime objects
date1 = datetime(2024, 1, 1, 10, 30, 0)
date2 = datetime(2024, 1, 5, 14, 45, 30)

# Calculate difference
difference = date2 - date1
total_seconds = difference.total_seconds()

print("Date 1:", date1)
print("Date 2:", date2)
print("Difference in seconds:", total_seconds)
print("Difference in days:", difference.days)
print("Difference in hours:", total_seconds / 3600)