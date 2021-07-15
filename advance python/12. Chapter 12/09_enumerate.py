#enumerate() adds counter to an iterable and returns it. here iterable is i/item

list1 = [3, 53, 2, False, 6.2, "Harry"]

# index = 0                      # we have to initilize index first, to use it in for loop. its extra work. so use enumerate()
# for i in list1:                  # i can be replaced with item
#     print([index], i)
#     index += 1                   #python doesnt understand ++, only += works. to print index of items in an list using for loop.

for index, item in enumerate(list1):         # to print index of items in an list using enumerate()
    print([index], item)