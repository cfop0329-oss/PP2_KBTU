"""Add a method 
    called welcome to the 
    Student class
    """
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname,
          self.lastname,
          "to the class of"
          , self.graduationyear) 
    """If you add a method in the
    child class with the same
    name as a function in the parent class, 
        the inheritance of 
    the parent method will be overridden.
              """