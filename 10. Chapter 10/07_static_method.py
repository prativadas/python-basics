class Employee:
    company = "Google"

    def getSalary(self, signature):     #can take many arguments along with
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod           #its a decorator to make a function static. function==method.  #static methods doesnt use self parameter 
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

harry = Employee()
harry.salary = 100000
harry.getSalary("Thanks!") # Employee.getSalary(harry)
harry.greet() # Employee.greet()
harry.time()

