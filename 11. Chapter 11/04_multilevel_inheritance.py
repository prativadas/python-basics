# when a child class become a parent for another child class

class Person:                #parent/base class 1
    country = "India"
    def takeBreath(self):      
        print("I am breathing...")

class Employee(Person):       # derived/child class 1
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreath(self):                                       # method overwritten from base class 1
        print("I am an Employee so I am luckily breathing..")

class Programmer(Employee):       # child/derived class 2. Person child class is parent class of Programmer child class
    company = "Fiverr"
    
    def getSalary(self):                            # method overwritten from base class 2 
        print(f"No salary to programmers")
    
    def takeBreath(self):                             # method overwritten from base class 1
        print("I am a Progarmmer so I am breathing++..")

p = Person()                # object of base class 1 is instantiated
p.takeBreath()
# print(p.company) # throws an error as no atrr named company is found in that class

e = Employee()              # object of base class 2 is instantiated
e.takeBreath()
print(e.company)

pr = Programmer()            #object of base class 1 is instantiated
pr.takeBreath()
print(pr.company)

print(pr.country)        # Programmer class doesnt have country attr, so it search in its parent class Person and prints india.
