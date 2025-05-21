class Employee:
    def __init__(self, name, employee_id):
        self.name = name  # Public
        self._employee_id = employee_id  # Protected
    
    def display_info(self):
        print(f"Employee: {self.name}, ID: {self._employee_id}")

class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)  # Call parent constructor
        self.department = department
    
    def display_manager_info(self):
        # Can access protected variable from parent class
        print(f"Manager: {self.name}, ID: {self._employee_id}, Department: {self.department}")

# Create objects
employee = Employee("Jane Smith", "E123")
manager = Manager("John Doe", "M456", "Engineering")
print(employee._employee_id)
# Display info
employee.display_info()
manager.display_manager_info()