# salaryAfterIncrement =  salary * increment

class Employee:
    salary = 1000          #class attr added as per question
    increment = 1.5
    
    @property                             # a.k.a getter method/decorator. if we dont use this
    def salaryAfterIncrement(self):
        return self.salary*self.increment     #returned as a property

    
    # def salaryAfterIncrement(self):        # if we comment out @property, we have to call function like salaryAfterIncrement() to print o/p.
    #     print(self.salary*self.increment) 
    
    @salaryAfterIncrement.setter          #helpful in defining the properties without manually calling the inbuilt function property(). return the property attr
    def salaryAfterIncrement(self, sai):
        self.increment = sai/self.salary

e = Employee()
print(e.salary)                      #original salary=1000
print(e.increment)                   #increament of 1.5
print(e.salaryAfterIncrement)        # 1000*1.5

# e.salaryAfterIncrement()


           
e.salaryAfterIncrement = 2000       #we set a new value to 2000
print(e.increment)
