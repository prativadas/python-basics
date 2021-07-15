a = [3, 6, 7, 8, 9, 2, 4, 23, 75, 23, 123, 67]
# b = []                   # first you have to create an empty list the new items will append in this list.
# for item in a:
#     if item%2==0:
#         b.append(item)
# print(b)

# Shortcut to write the same:
b = [i for i in a if i%2==0]
print(b)

t = [1, 4, 2, 4, 1, 2, 3]      #repeated values in list
s = {i for i in t}             # no repeated values allowed in set
print(s)