names = ['liva', 'anna', 'pinka', 'ashu', 'juju']

findname = input('enter name')

if (findname in names):            # as list [] cant be passed as the left operand of 'in', we take user input
    print('your name is in the list')
else:
    print('your name is not in the list')