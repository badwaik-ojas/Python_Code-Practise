
# Define the class blueprint for Housekeeper
class Housekeeper:
    def __init__(self, name, responsible_floor):
        self.name = name  # Attribute: name of the housekeeper
        self.responsible_floor = responsible_floor  # Attribute: responsible floor
        self.is_cleaning_now = False  # Attribute: initially not cleaning
    
    # Method: start cleaning
    def start_cleaning(self):
        self.is_cleaning_now = True
        print(f"{self.name} is now cleaning the {self.responsible_floor}.")
    
    # Method: notify supervisor
    def notify_supervisor(self, issue):
        print(f"{self.name} is notifying the supervisor about: {issue}")

# Creating objects (instances) of the Housekeeper class
mary = Housekeeper("Mary", "2nd and 3rd floors")
jane = Housekeeper("Jane", "4th and 5th floors")

# Calling methods on the objects
mary.start_cleaning()  # Mary starts cleaning
jane.notify_supervisor("leaking sink on the 5th floor")  # Jane reports an issue
