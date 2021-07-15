# n! = (n-1)! * n 
# sum(n) = sum(n-1) + n

# calculate sum of n natural numbers using recursive function. natural numbers= 1,2,3...

def sum_naturalnum(n):
    if n==1 or n==0:        #if we comment these conditions then stackoverflow occurs.
        return 1

    return sum_naturalnum(n-1)+n
    
print(sum_naturalnum(4))

