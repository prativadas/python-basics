# def greet(name):
def greet(name='liva'):                        # default paramete value here is liva
    print("Good Day, "+ name)

# greet("Harry")                    # calling the greet() here

greet()                        # when nor arguemnet passed it will take default parameter.

def mySum(num1, num2):                     #function with more than one arguement
    return num1 + num2


s = mySum(6, 32)
print(s)