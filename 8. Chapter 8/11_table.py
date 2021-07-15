# #multiplication table using a function

# # 

# def mul_table(n,i):       
#     if (i>10):            # base case. if the value called recursively is greater than 10, exit from the function
#         return            # here default value none is returned.
#     print(n*i)
#     return mul_table(n, (i+1))    #Recursive call to next iteration
    
# print(mul_table(4,1))


# def mul_table(n, i):                   # default value of ‘i’ is 1
#     print (n*i)
#     if i != 10:                          # for i=10, if condition false s0, it exits.
#        return mul_table(n,i+1)

# print(mul_table(4))


def mul_table(n, i=1):
     print (n*i)                   # default value of ‘i’ is 1
     if i != 10:                   # for i=10, if condition false s0, it exits. 

        return mul_table(n,i+1)
                             
print(mul_table(4))
