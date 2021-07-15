post = input('write your post: ')

if 'harry' in post:
    print('post mentioned harry')
elif 'HARRY' in post:
    print('post mentioned HARRY')
elif 'Harry' in post:
    print('post mentioned Harry')

else:
    print('post doesnt discuss harry')