class Person:
    def __init__(self, age, name, ssn):
        self.name = name # Public variable - accessible from anywhere
        self._age = age # Protected variable - should only be accessed by class and subclasses
        self.__ssn = ssn # Private variable - should only be accessed within this class

    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}, SSN: {self.__ssn}")

# Create a Person object
john = Person("John", 30, "123-45-6789")

# Accessing variables
print(john.name)  # Works fine - public variable
print(john._age)  # Works but shouldn't do this - protected variable
#print(john.__ssn)  # Error! - private variable cannot be accessed directly

# But can access through class methods
john.display_info()  # This works because we're accessing __ssn from inside the class

    