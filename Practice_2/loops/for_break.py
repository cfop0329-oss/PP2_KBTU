#With the break statement we can stop the loop before it has looped through all the items
#Example 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#Example 2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#Example 3
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!") 