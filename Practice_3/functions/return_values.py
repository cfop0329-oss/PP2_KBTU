#Using *args to accept any number of arguments
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus") 

def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus") 
"""Вы можете комбинировать регулярные параметры с *args.

Регулярные параметры должны быть перед *args
    """
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)
    
my_function("Hello", "Emil", "Tobias", "Linus")

#Practical Example with *args
def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5)) 

#Using **kwargs to accept any number of keyword arguments:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

"""The **kwargs parameter allows a function to accept any number of keyword arguments.

Inside the function, kwargs becomes a dictionary containing all the keyword arguments:
    """
def my_function(**kwargs):
  print("Type:", type(kwargs))
  print("First name:", kwargs["fname"])
  print("Last name:", kwargs["lname"])
  print("All keyword arguments:", kwargs)
my_function(fname = "Tobias", lname = "Refsnes")
"""You can combine regular parameters with **kwargs.

Regular parameters must be before **kwargs
    """
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")
#Combining *args and **kwargs
def my_function(*args, **kwargs):
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)
my_function(1, 2, 3, name="Alice", age=30)
"""The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.
    """
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result) 