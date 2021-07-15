#print multiplication table vertically

# l = [str(i*7) for i in range(1, 11)]    #typecast to str to all the items. 
# print(l)

# verticalTable = "\n".join(l)            # .join() works only for for str. so we typecast the list
# print(verticalTable)

#alternative ways 

# l = [i*7 for i in range(1, 11)] 

# using list comprehension
# listToStr = ' \n'.join([str(item) for item in l])
# print(listToStr)

# using map()- map() - applies a function to all items in a i/p list

l = [i*7 for i in range(1, 11)] 
listToStr = ' \n'.join(map(str, l))
  
print(listToStr) 

