with open('story.txt','w') as f:                # we 1st create a file and write into it.
    b = f.write(('thi is a twinkle star'))

with open('story.txt','r') as f:                #then we read from the file.
    b= f.read()

print(b)

if 'twinkle' in b:
    print('yes')
else:
    print('no')

