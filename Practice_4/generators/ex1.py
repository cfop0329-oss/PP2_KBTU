def squares_up_to_n(n):
    """Generate squares of numbers from 0 to n"""
    for i in range(n + 1):
        yield i * i

# Test
print("Exercise 1: Squares up to N")
for square in squares_up_to_n(5):
    print(square, end=" ")
print()