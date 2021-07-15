class Employee:
    company = "Google"             # class attributes
    salary = 100                   # this value will be printed when instance attr of objects are not initialized.

harry = Employee()            # objects of class Emplyoee.
rajni = Employee()
harry.salary = 300            #instance attributes
# rajni.salary = 400          # instance attributes takes preferenace over class attribute during assignmnet and retrieval.
                              # when we comment out rajni.salary, print(rajni.salary) will search for salary attr in instance attr then in class attr  
                              
print(harry.company)
print(rajni.company)
# Employee.company = "YouTube"         #changing class attr updates the value
print(harry.company)
print(rajni.company)
print(harry.salary)
print(rajni.salary)