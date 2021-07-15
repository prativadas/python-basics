text = input('enter your text: ')

# mylist = ['make a lot of money', 'buy now', 'subscribe this', 'click this'] cant pass a list in below code

if('buy now' in text): # here we can only give strings in the left operand instead of a list
    print('spam alert')
elif('click this' in text):
    print('spam alert')
elif('make money' in text):
    print('spam alert')
elif('subscribe this' in text):
    print('spam')
else:
    print('no spam')