"""Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.
    """
    
class MyClass:
    x = 5
#Now we can use the class named MyClass to create objects
p1 = MyClass()
print(p1.x)

#You can delete objects by using the del keyword:
del p1

#Multiple objects can be created from the same class, and can be treated as separate objects.
p1 = MyClass()
p2 = MyClass()
print(p1.x)
print(p2.x)

"""Challenge: Classes/Objects

Test your understanding of Python classes by completing a small coding challenge.
Instructions
Inside the editor, complete the following steps:

    Create a class called Person
    Add an __init__ method that takes name and age as parameters
    Add a method called greet that prints "Hello, my name is " followed by the name
    Create an object p1 of the class with name "John" and age 36
    Call the greet method on p1
    """
# Create a class called Person
class Person:
    # Add an __init__ method that takes name and age as parameters
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Add a method called greet that prints greeting
    def greet(self):
        print("Hello, my name is " + self.name)

# Create an object p1 of the class with name "John" and age 36
p1 = Person("John", 36)

# Call the greet method on p1
p1.greet()