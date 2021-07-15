class Employee:
    company = "Google"          #class attr
    salary = 100

harry = Employee()        # objects of class  employee. here object is intialized
rajni = Employee()

# Creating instance attribute salary for both the objects
# harry.salary = 300
# rajni.salary = 400
harry.salary = 45          #instance attr. instance attributes takes preferenace over class attribute during assignmnet and retrieval.
print(harry.salary)
print(rajni.salary)       #when we comment out rajni.salary, print(rajni.salary) will search for salary attr in instance attr then in class attr

# Below line throws an error as address is not present in instance/class 
# print(rajni.address) 

print(Employee.salary)