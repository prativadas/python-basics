#multi-level inheritence
class Animals:           #base class
    animalType = "Mammal"

class Pets(Animals):              # derived class 1
    color = "White"

class Dog(Pets):             # derived class 2
    @staticmethod           # used as bark() not using any class atrr/instance attr
    def bark():
        print("Bow bow!")

d  = Dog()
d.bark()                # format for priniting o/p of methods

print(d.color) # Dog() class doesnt have color attr, so it searches in its parent class and prints, format for printing o/p for attr