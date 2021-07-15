# fruits = ['Banana', 'Watermelon', 'Grapes', 'Mangoes']
# i = 0
# while i<len(fruits):
#     print(fruits[i])
#     i = i+1


names = ['liva', 'liza', 'rinku', 'anna', 'moti', 'juju']   # print elements of a list with index number using only for loop

# for item in range(len(names)):
#     print(item, names[item])

# print(names.index('moti'))  #element-wise index search

# print(len(names))    # len() counts total elements in a list

# print(names[0:])   # print the elements in list

# print elements of a list using while loop


j = 0
while j < len(names):
    for j in range(len(names)):
        print(j, names[j])
    j = j + 1


