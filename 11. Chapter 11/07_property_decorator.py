class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybonus = 400
    # totalSalary = 6100            #if we hard code this, then when change occured in bonus/salary, totalsalary also have to be changed.
                                    # this atrr depends on 2 other attributes, so we use propoerty decorator inside which totalSalary() used. 
    
    @property                       # a.k.a getter method/decorator. # if we comment out @pproperty, we call e.totalSalary()- like this to print o/p
    def totalSalary(self):         # helpful in defining the properties without manually calling the inbuilt function property(). Which is used to return the property attributes
        return self.salary + self.salarybonus

   
    # def totalSalary(self):         # helpful in defining the properties without manually calling the inbuilt function property(). Which is used to return the property attributes
    #     print(self.salary + self.salarybonus) 


    @totalSalary.setter      #a.k.a setter decorator
    def totalSalary(self, val):
        self.salarybonus = val - self.salary

e = Employee()

print(e.totalSalary)          #original salaray # here we dont have to call the function to print values. if we comment out @pproperty, it just runs without giving o/p.

# e.totalSalary()                 

e.totalSalary = 5800                #we set totalsalaryvalue and using setter method, 
print(e.salary)                     #setter decorator adjust bonus and salary value so that it sums to total salary 5800.
print(e.salarybonus)