#find greatest of 3 numbers

def max(n1,n2,n3):
    if (n1>n2):                      #if this condition is true then we check between n1 and n3
        if (n1>n3):
            return n1
        else:
            return n3
    else:                            #if n2 > n1 in 1st if condition
        if(n2>n3):
            return n2
        else:
            return n3

print(max(4,10,1))
# max_num= max(4,10,1)
# print(max_num)