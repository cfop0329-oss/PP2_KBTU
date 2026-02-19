#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc
#Example 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#Example 2
for x in "banana":
  print(x)
#Example 3
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) 