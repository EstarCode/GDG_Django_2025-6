class Car:
    def __init__(self, make):
        self.make = make

    def get_make(self):
        return f"New model of car: {self.make}"


car1 = Car("BMW")
print(car1.get_make())
