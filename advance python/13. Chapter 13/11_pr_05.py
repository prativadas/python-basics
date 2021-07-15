from functools import reduce
l = [3, 8, 455, 2, 5, 45]

a = reduce(max, l) # we dont have to call max() here, we just write the name
print(a)