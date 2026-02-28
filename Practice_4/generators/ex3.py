def divisible_by_3_and_4(n):
    """Generate numbers divisible by both 3 and 4 (i.e., divisible by 12)"""
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Test
print("\nExercise 3: Divisible by 3 and 4")
n = int(input("Enter n: "))
for num in divisible_by_3_and_4(n):
    print(num, end=" ")
print()