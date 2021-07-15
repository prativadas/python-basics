# n! = 1 * 2 * 3 * 4...*n
# n! = [1 * 2 * 3 * 4... n-1] *n
# n! = n * (n-1)! 


# number = int(input('enter a number:'))

# for i in range(number):
#     fact= number*(number-1)            # here this doesnt work for 0 and 1
# print(fact)                

# n = 0
# product = 1 
# for i in range(n):                           #initialize the product value.
#     product = product * (i+1)
# print(product)

# def factorial_iter(n):
#     product = 1
#     for i in range(n):
#         product = product * (i+1)
#     return product

# def factorial_recursive(n):
#     if n == 1 or n == 0:
#         return 1
#     return n * factorial_recursive(n-1)

# # f = factorial_iter(5)
# f = factorial_recursive(0)
# print(f)

##### careful of stack overflow or infinite loop while using recursion. if the base condition not set right then it happens.

def factorial_recursive(n):
    # if n == 1 or n == 0:              # if we comment these conditions then stackoverflow occurs.
    #     return 1
    return n * factorial_recursive(n-1)
f = factorial_recursive(0)
print(f)