# super method used to access methods of a super class in the derived class

class Person:                        #base class
    country = "India"

    def __init__(self):                 
        print("Initializing Person...\n")

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):      # child class 1
    company = "Honda"

    def __init__(self):         
        super().__init__()               # super() - used to run constructor of its superclass Person.                   
        print("Initializing Employee...\n")

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreath(self):
        super().takeBreath()      # prints value from the takeBreath() of base class Person
        print("I am an Employee so I am luckily breathing..") # then this prints

class Programmer(Employee):       # child class 2
    company = "Fiverr"

    def __init__(self):
        super().__init__()                        # super() - used to run constructor of its superclass Employee.    
        print("Initializing Programmer...\n")

    def getSalary(self):
        print(f"No salary to programmers")
    
    def takeBreath(self):
        super().takeBreath() # this goes to its super class Emplyoee's takeBreath(), the from then it goes its superclass to Person's  takeBreath()
        print("I am a Progarmmer so I am breathing++..")

# p = Person()     # prints the value inside __init__ constructor of Person class
# # p.takeBreath() # prints only whats inside takeBreath() of person class.

e = Employee()     # prints the value inside __init__ constructor of Employee class and its superclass -Person 
# e.takeBreath()  

# pr = Programmer()   # prints the value inside __init__ constructor of Programmer class and its superclass -Person and Employee
# # pr.takeBreath() 
