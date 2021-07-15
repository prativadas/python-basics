class Employee:
    company = "Google"        #class attr
    def getSalary(self):   #remove self, error throws  # if using a function in class, then have to pass self as argument.
        print(f"Salary for this employee working in {self.company} is {self.salary}") # by using self, we can use both class and instance attr of any class and object

harry = Employee()
harry.salary = 100000          #instance attr
harry.getSalary() # harry.getSalary() gets converted to Employee.getSalary(harry) internally. both are same. so 1 argument is passed wich is invisible
                  # throws error when self is not passed in function under class.
                  # frequently used is harry.getSalary() as its readability is better.