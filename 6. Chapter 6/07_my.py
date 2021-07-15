sub1 = int(input('enter marks for subject1:'))  #convert to int type for adding integers
sub2 = int(input('enter marks for subject2:'))
sub3 = int(input('enter marks for subject3:'))

obtainedmarks = sub1 + sub2 + sub3

#totalmarks = 300

print(obtainedmarks)

#percentage = (obtainedmarks/totalmarks)*100

percentage = obtainedmarks/3

print(percentage)
# below code doesnt satisfy the 'and' condition where both conditions satisfy

# if (sub1>33 or sub2>33 or sub3>33):   #atleast condition is is '<'. so error in o/p if we use this code
#     print('passed in each subject')
# else:
#     print('failed as you have less than 33% atleast in one of the subjects')

# if(percentage>40):
#         print('overall percentage is greater than 40. so you are passed')
# else:
#     print('you are failed because total percentage is less than 40')


if (sub1<33 or sub2<33 or sub3<33):   #atleast condition is 'or'
    print('failed in one of the subjects. so you are failed')
else:
    print('passed as you have greater than 33% atleast in all of the subjects')

if(percentage>40):
        print('overall percentage is greater than 40. so you are passed')
else:
    print('you are failed because total percentage is less than 40')






