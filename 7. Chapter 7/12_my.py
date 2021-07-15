# 1 is neither prime nor composite.
# a prime number has exactly two positive divisors. it is divisible by 1 and itself.
# However, 1 only has one positive divisor (1 itself), so it is not prime.

number = int(input('enter number: '))

# if number > 1:                    # prime numbers are always > 1
# for i in range(2,number):         # due to if-else loop - here for 4 all conditions are satisfying. 4%2 ==0, 4%3==1
#     if (number%i==0):
#         print(number, "is not a prime number")
#     else:
#         print(number,'is a prime number')
# print(number, "is a prime number")


if number > 1: 
    for i in range(2,number):          # for loop runs for 2 to number-1 times. as all numbers are divisible by 1 and itself. so we check from 2 to (number-1)
        if (number%i==0):              
            print(number, "is not a prime number")
            break                      # break stmnt is must here. for loop will end after the if condition is true
        # else:
        #     print(number, "is a prime number")      # if we have else in if stmnt, when if=false->else executes.for loop again iterates between 2 to number-1.              

    else:                            # when if condition is false, if loop breaks and goes to else of for loop.
        print(number,'is a prime number')
else:
    print(number, "is not a prime number")
    

#why this code is giving 1, 2 is prime o/p? #1 and 2 has no divisor other than 1 and number itself. so for loops exits and else stmnt prints.
              
# for i in range(1,number):        # any number is always divisible by 1, 
#                                  # so we dont check range(1,number). check number=2. it gives 2 is not a prime number as 2%1=0. so logic is wrong.
#     if (number%i==0):
#         print(number, "is not a prime number")
#         break
# else:
#     print(number,'is a prime number')
