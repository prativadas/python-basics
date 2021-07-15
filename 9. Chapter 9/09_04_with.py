# if we open a file with 'with' stmnt, then we dont need to use f.close() explicitly.

# # with open('another1.txt', 'r') as f:
# #     a = f.read()
# with open('another2.txt', 'w') as f:    # if a file is not created, it will be created when use w mode.
#     a = f.write("i will slap you")
# print(a)                    # when file not opened in r mmode, total characters will be printed intead of 


f = open('thismy.txt','w')   #all the w modes allow multiple writes before f.close(). 
f.write('thi is me')
f.write('i love you')
f.write('thi is nice')

f.close()

# f = open('thismy.txt','w') # but when you again use w mode, all previous data wipe out