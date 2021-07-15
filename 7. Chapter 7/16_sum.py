# sum of n natural numbers using while loop

num = int(input('entera number: '))

# total = 0       # initialize first

# i = 1           # works only for non-zero integers

# while i <=num:        # loop runs until num 
#     total = total + i     # updates total. for num = 3, i =1: total=0+1=1, i=2: total=1+2=3, i=3: total=3+3=6
#     i = i + 1
#     # print('sum is: ', total )        # if print is inside while loop, o/p will be printed after each iteration
# print('sum is: ', total )


#using formula num(num+1)/2


finalsum = 0              # if we are using the num value in formula we get error: 'int' object is not callable
finalsum = num*(num+1)/2      ######## very important. python doesn't understand n(n+1)/2. it understands n*(n+1)/2. use * operator
print('total sum is : ', finalsum)    
