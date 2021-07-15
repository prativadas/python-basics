a = 54                                  # Global variable
def func1():  
    global a                              #global keyword used to modify the variable outside of the current scope. 
    print(f"Print statement 1: {a}")
    a = 8                                 # Local Variable if global keyword is not used. changes a to 8 from 54
    print(f"Print statement 2: {a}")

func1()                                  #prints the local variable a value inside func1()
print(f"Print statement 3: {a}")         #prints global var a value outside funct1()