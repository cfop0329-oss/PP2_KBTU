# class_variables.py
# Understanding Class Variables vs Instance Variables

class Employee:
    # Class Variable: Shared among ALL instances of this class
    num_employees = 0
    company_name = "TechCorp"

    def __init__(self, name, salary):
        # Instance Variables: Unique to EACH instance
        self.name = name
        self.salary = salary
        
        # Modify the class variable
        Employee.num_employees += 1

    def display(self):
        print(f"Employee: {self.name} | Salary: ${self.salary} | Company: {self.company_name}")

    @classmethod
    def show_count(cls):
        print(f"Total Employees at {cls.company_name}: {cls.num_employees}")

# --- Example 1: Basic Usage ---
print("=== Example 1: Basic Class vs Instance Variables ===")
e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)

e1.display()
e2.display()
Employee.show_count()