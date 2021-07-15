l1 = [2,'liva', 'liza', False, 89.1, 66, True]        # index is 0 to 6 here

for index, item in enumerate(l1):          # printing items of odd index
    if index%2!=0:
        print([index],item)
           

    

# l2 = [i for i in l1 if i%2!=0 ]         # this doesnt work as i is not for index in list, its for elements
# print(l2)