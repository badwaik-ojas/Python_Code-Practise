class Car:
    def __init__(self, windows, doors, engine_type):
        self.windows = windows
        self.doors = doors
        self.engine_type = engine_type

    def drive(self):
        print(f"The person will drive {self.engine_type}")

class Tesla(Car):
    def __init__(self, windows, doors, engine_type, is_self_driving):
        super().__init__(windows, doors, engine_type)
        self.is_self_driving = is_self_driving

    def self_driving_car(self):
        print("the car is self driving: ", self.is_self_driving)

tesla = Tesla(4, 5, 'Electric', True)
print(tesla.self_driving_car())
print(tesla.drive())        