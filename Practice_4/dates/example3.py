from datetime import datetime

# Current datetime with microseconds
now_with_micro = datetime.now()
print("With microseconds:", now_with_micro)

# Remove microseconds
now_without_micro = now_with_micro.replace(microsecond=0)
print("Without microseconds:", now_without_micro)