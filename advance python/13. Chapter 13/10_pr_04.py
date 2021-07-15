l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 54, 23, 55, 90, 60]

a = list(filter(lambda a: a%5==0, l))             # Filter Syntax: list(filter(function, list))
# print(list(a))          # can also print like this
print(a)