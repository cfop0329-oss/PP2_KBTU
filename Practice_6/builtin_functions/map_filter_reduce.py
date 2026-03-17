from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]
# 1. filter: оставляем только четные (2, 4, 6)
# 2. map: возводим в квадрат (4, 16, 36)
# 3. reduce: суммируем всё (4 + 16 + 36 = 56)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
squared_numbers = list(map(lambda x: x ** 2, even_numbers))
total = reduce(lambda x, y: x + y, squared_numbers)
print(total)  # Вывод: 56
