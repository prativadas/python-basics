class Number:
    def __init__(self, num):           # __init__ is a dunder method, a.k.a double underscore
        self.num = num

    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Lets multiply")
        return self.num * num2.num
    
    def __str__(self):                           #executes when you are directly printing the object.
        return f"Decimal Number: {self.num}"
    
    def __len__(self):
        return 1

n = Number(9)
print(n)
print(len(n))