def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter n: "))
even_nums = list(even_numbers(n))
print(",".join(map(str, even_nums)))