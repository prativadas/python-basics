username = input('enter username: ')

print(len(username))

if(len(username)<10):
    print('username has less than 10 char')
else:
    print('username has more than 10 char')