class Animal:
    def __init__(self):
        pass

    def make_sound(self):
        return "The animal makes a sound"


class Cat(Animal):
    def make_sound(self):
        return "Meow"


animal = Animal()
cat = Cat()
print(animal.make_sound())
print(cat.make_sound())
