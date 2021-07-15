a = input("Enter your name: ")

print(type(a))


b = input('enter your age: ')
print(type(b)) # type of b is str then converted to int

b = int(b) # Convert a to an Integer(if possible) 
print(type(b))

c = input('enter your name: ') # input () always takes str type variable. use type() to convert to other datatypes

print(type(c))

#c = int(c) # cant convert str to int. throws error
# print(type(c))

