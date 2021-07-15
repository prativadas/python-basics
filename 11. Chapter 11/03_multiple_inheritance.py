# multiple inheritence---> when child inherits from more than 1 parent class.


class Freelancer:            # base class 1
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Employee:                        # base class 2
    company = "Visa" 
    eCode = 120


# class Programmer(Employee, Freelancer):  # print(p.company) gives Visa as Employee class is pased as 1st argument
#     name = "Rohit"

class Programmer(Freelancer, Employee): # derived class inherits both base class1 and 2 here. # print(p.company) gives Fiverr as Freelancer class is pased as 1st argument
    name = "Rohit"

p = Programmer()    # object of derived class
print(p.company)    # prints the company name of 1st argument- base class thats is passed 1st when derived class created. 

p.upgradeLevel()   # upgradeLevel() is used in base class 1, and here derived class also using it.
print(p.level)

p.upgradeLevel()   # as many times this method is called, the level increases.
print(p.level)