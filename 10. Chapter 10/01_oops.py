#object oriented method

class Number:                            #class name always written in PascalCase
    def sum(self):                       # self refers to the instance of class. automatically passed with a function call from an object.
        return self.a + self.b

num = Number()                 # a new object of class Number is instantiated.
num.a = 12                     # attributes of object num, called instance attributes
num.b = 34
s = num.sum()
print(s)

#procedural oriented prog   
# a = 12
# b = 34

# print("The sum of a and b is ", a+b)

'''
PascalCase 
EmployeeName -->PascalCase 

camelCase
isNumeric, isFloatOrInt -->camelCase
'''