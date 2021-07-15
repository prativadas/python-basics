num1 = input('enter 1st num:')
num2 = input('enter 2nd num:')
num3 = input('enter 3rd num:')
num4 = input('enter 4th num:')


# works only when numbers are sotred 

# if(num1>num2):
#     print('num1 is greater')
# elif(num2>num3):
#     print('num2 is greater')
# elif(num3>num4):
#     print('num3 is greater')
# else:
#     print('num4 is greater')

# divide the problem into 2 sub-roblem.
#comapre num1 & num2 and strore result in new var
# then compare num3 & num 4 and store in new var
# then comapre those 2 var

if (num1>num2):
    newnum1 = num1
else:
    newnum1 = num2

if(num3>num4):
    newvar2 = num3
else:
    newvar2 = num4

if(newnum1> newvar2):
    greatestnum = newnum1
else:
    greatestnum = newvar2
      
print('greatest among 4 number is: ', greatestnum)

print(type(num1))

