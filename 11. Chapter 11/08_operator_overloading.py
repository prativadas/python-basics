# operators in python can be overloaded using dunder methods

class Number:
    def __init__(self, num1):  # dunder method-->double underscore methods
        self.num1 = num1

    def __add__(self, num2):  # if you want to overload '+' operator , use builtin function __add__.# these dunder methods - called when a given operator is used on the objects.
        print("Lets add")
        return self.num1 + num2.num1

    def __mul__(self, num2):
        print("Lets multiply")
        return self.num1 * num2.num1

n1 = Number(4)
n2 = Number(6)
sum = n1 + n2 #calls add method.
mul = n1 * n2  # calls mul method
print(sum)
print(mul)