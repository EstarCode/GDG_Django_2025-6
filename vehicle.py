class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        return f"Brand: {self.brand}, Year: {self.year}"


class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def info(self):
        return f"brand: {self.brand}, model:{self.model}, year: {self.year} "


vehicle = Vehicle("Toyota", 2018)
car = Car("Tesla", 2023, "Model 3")

print(vehicle.info())
print(car.info())
