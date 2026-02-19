def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus") 

"""

From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the actual value that is sent to the function when it is called.

    """
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument 


#This function expects 2 arguments, and gets 2 arguments::
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes") 

"""Default Parameter Values

You can assign default values to parameters. If the function is 
called without an
argument, it uses the default value:
    """
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")
#Keyword Arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy") 
#Positional Arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy") 
#Mixing Positional and Keyword Arguments
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5) 
#Passing Different Data Types

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits) 

#Returning Different Data Types
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2]) 
#Positional-Only Arguments
def my_function(name, /):
  print("Hello", name)

my_function("Emil")
#Keyword-Only Arguments 
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")