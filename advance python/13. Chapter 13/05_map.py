def square(num):
    return num*num

l = [1, 2, 4]

# Method 1
l2 = []
for item in l:
    l2.append(square(item))
print(l2)

# map() - applies a function to all items in a i/p list- syntax: list(map(function, i/p list)). function can be a lamda function also

# Method 2- no need to create an empty list
print(list(map(square, l)))          # alternative method. we typecast map to list to print the values