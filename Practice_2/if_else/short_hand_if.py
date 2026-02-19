#Example 1
a, b = 10, 5
if a > b: print(f"{a} is greater than {b}")
#Example 2
x, y = 8, 12
max_val = x if x > y else y
print(f"Max of {x} and {y} is {max_val}")

min_val = x if x < y else y
print(f"Min of {x} and {y} is {min_val}")
#Example 3
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Age {age} → {status}")

num = -7
print(f"{num} is {'positive' if num >= 0 else 'negative'}")
#Example 4
score = 85
result = "Pass" if score >= 60 else "Fail"
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
print(f"Score {score}: {result} with grade {grade}")