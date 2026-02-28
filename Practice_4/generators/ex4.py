def squares(a, b):
    """Generate squares of numbers from a to b"""
    for i in range(a, b + 1):
        yield i * i

# Test
print("\nExercise 4: Squares from a to b")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(f"Squares from {a} to {b}:")
for value in squares(a, b):
    print(value)