# class method- is bound to the class not its objects

class Employee:
    company = "Camel"      
    salary = 100            # class atrr
    location = "Delhi"

    # def changeSalary(self, sal):  # function to change class atrr value by adding instance attr
    #     self.salary=sal           # sal value will be new value for salary attr
  
    # def changeSalary(self, sal):    #changing class atrr salary without adding instance attr. __class__ is a dunder method
    #     self.__class__.salary = sal         

    @classmethod       #accessing class using classmethod. # other easier method to change class attr salary value is y using static method.
    def changeSalary(cls, sal): #cls is reference to class. #changing class atrr salary without adding instance attr
        cls.salary = sal         # this changes the class attr directly. print(Employee.salary) changes from 100 to 455

e = Employee()
print(e.salary)  #initial salary
e.changeSalary(455)     #added instance attr to change value # assigned sal a new value that is new value for salary
print(e.salary)
print(Employee.salary) #class attr doesnt changes its value
