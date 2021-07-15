#syntax of reduce() - reduce(function, list), function can be lamda() also

from functools import reduce         #alway have to import to use reduce()

sum = lambda a, b: a+b

l = [1, 2, 3, 4]          # 1+2=3, 3+3=6, 6+4=10
val = reduce(sum, l)
print(val)