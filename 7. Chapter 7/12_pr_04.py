num = int(input("Enter the number: "))
prime = True

for i in range(2, num):
    if(num%i == 0):
        prime = False
        break
if prime:
    print("This number is Prime")
else:
    print("This number is not Prime")

# here also for 1 and 2 o/p is prime number. why? - modify it by using if num>1:
# 1 and 2 has no divisor other than 1 and number itself. so for loops exits and else stmnt prints.
# but why and how?? it works for num=2