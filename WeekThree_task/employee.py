class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        self.salary = self.salary*12
        return f"{self.name}'s annual salary is {self.salary}"


employee1 = Employee("Tibebe", 25000)
print(employee1.annual_salary())
