def squares(a, b):
    for i in range(a, b + 1):
        yield i * i


a = int(input())
b = int(input("Enter b: "))
print(f"Squares from {a} to {b}:")
for value in squares(a, b):
    print(value)