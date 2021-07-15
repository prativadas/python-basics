# factorial of n numbers

num = int(input('enter number: '))

fact = 1 

# for i in range(1,num+1):      # for loop executes 1 to num. 
#     fact = fact * i           # updates variable fact. for num =3, loop runs for 1,2,3. so fact= 1*1=1; fact=1*2=2;fact=2*3=6
# print('factorial is: ', fact)


#using while loop

i = 1

while i<=num:
    fact = fact* i
    i = i + 1
print('factorial is: ', fact)




