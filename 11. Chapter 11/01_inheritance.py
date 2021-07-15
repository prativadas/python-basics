class Employee:                     # parent/ base class
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):        # derived/child class
    language = "Python"
    # company = "Youtube"         #atrributes of base class is overwritten in derived class

    def getLanguage(self):
        print(f"The language is {self.language}")
    
    # def showDetails(self):              # when this dunctionis not defined in Programmer class, p.showDetails() inherits from base class.
    #     print("This is an programmer")  # this function is ovrwritten in derived class from base class


e = Employee()      # object of Employee class created
e.showDetails()
p = Programmer()
p.showDetails()      # object of Programmer class created, #In p.showDetails(), object p cant find any such method in Programmer class, so it inherits from parent class 
print(p.company)