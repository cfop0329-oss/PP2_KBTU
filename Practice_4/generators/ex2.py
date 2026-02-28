def even_numbers(n):
    """Generate even numbers from 0 to n"""
    for i in range(0, n + 1, 2):
        yield i

# Test
print("\nExercise 2: Even Numbers")
n = int(input("Enter n: "))
even_nums = list(even_numbers(n))
print(",".join(map(str, even_nums)))