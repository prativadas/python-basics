class Calculator:
    def __init__(self, number):             # number is a variable/argumnet inside a function
        self.number = number                # object instantiated.

    def square(self):     #define function under class calculator then only can use number argument here in this function
        print(f'square of:{self.number} is {self.number **2}')

    def cube(self):
        print(f'cube of:{self.number} is {self.number **3}')

    def sqrt(self):
        print(f'sqrt of:{self.number} is {self.number **0.5}')

num = Calculator(5)

num.square()
num.sqrt()
num.cube()

