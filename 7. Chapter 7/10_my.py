# multiplication table     

number = int(input('enter any number: '))

# for i in range(1,11):         # for loop run for 1 to 10
#     # print(number*i)         # simply prints the final values of any table
#     # print(str(number) + '*' + str(i) + '=' + str(i*number)) #prints in a format. '+' used for concatenation of all the strings to br printed
    
#     #use of f-strings for nice format for printing output
#     print(f'{number} * {i} = {number*i}')                           

# using while loop

# j = 1                   # in while loop always initialize the variable and give a condition in while loop.
# while j<11:             # loops runs for n-1
#     print(f'{number} * {j} = {number*j}')   
#     j= j+1
    

# multiplication table in reverse order

for i in range (10,0,-1):            #range(start_value, end_value, step). -1 stepsize means loop executes in reverse step.  
    print(number*i)


#can we reverse the list

# for i in range(1,11):                # number*i returns int. cant use list() to convert it.
#     l1= [number*i]                   # i is an iterable object. so reverse() and reversed() doesnt work.
  
#     # print(l1)  
#     l2= list(l1)
#     print(*l2)
    # print(type(l1))
     #print(type(l2))
    
   
    # print(reversed(l1))
    # print((number*i))         
    
    # print([number*i])
    # # print(*l1)
    # print(l1.reverse())
    
       
    # print (l1[::-1])        # not working why?
    # print (*l1)             # *l1 prints the output of list without []
    # print(l1.reverse())     # why reverse() is not wroking
    # print(*l1) 
                                 
    # print(number*i)

# only method thats working for printing table in reverse

# for i in reversed (range(1,11)):        # reversed()-returns a reversed iterator of a given iterable object(e.g i).
#     print(i*number)
