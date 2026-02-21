#Example 1
def my_function(*args):
    for arg in args:
        print(arg)
my_function(1, 2, 3)
#Example 2
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
my_function(name="Alice", age=30, city="New York")
#Example 3
def my_function(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)
    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
my_function(1, 2, 3, name="Alice", age=30, city="New York")