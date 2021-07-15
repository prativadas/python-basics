# printing 3rd,5th, 7th elemnet of the list

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index, item in enumerate(l):
    if index==2 or index== 4 or index==6:    # for printing 3rd,5th, 7th elemnet of the list, there index is 2, 4, 6 as indexing starts from 0. 
        # print(index, item)                 # this prints actual index number, 3rd,5th, 7th elemnet of the list
        print(f"The {index + 1}th element is {item}") #as index starts from 0 in python we add +1 to index number