class MyClass:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    def instance_method(self):
        return f"This is an instance method. Instance variable: {self.instance_variable}"

    @classmethod
    def class_method(cls):
        return f"This is a class method. Class variable: {cls.class_variable}"

    @staticmethod
    def static_method():
        return "This is a static method. It does not access class or instance variables."
# Example usage
my_instance = MyClass("I am an instance variable")
print(my_instance.instance_method())  # Accessing instance method
print(MyClass.class_method())         # Accessing class method
print(MyClass.static_method())        # Accessing static method