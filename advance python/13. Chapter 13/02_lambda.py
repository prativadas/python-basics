#syntax - lamda arguments: expressions       # here expression is the return of function
# using lamda method/anonymous functions - we can define function in one line

# def func(a):
#     return a+5

func = lambda a: a+5      #useful when we pass function as an arguement
square = lambda x: x*x
sum = lambda a, b, c: a+b+c

x = 3
print(func(x)) # Prints 8
print(square(x)) # Prints 9
print(sum(x, 1, 2)) # Prints 6