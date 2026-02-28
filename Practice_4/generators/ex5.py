def countdown(n):
    """Generate numbers from n down to 0"""
    while n >= 0:
        yield n
        n -= 1

# Test
print("\nExercise 5: Countdown from n to 0")
n = int(input("Enter n: "))
for num in countdown(n):
    print(num, end=" ")
print()