for i in range(10):                         
    print(i)                                 #if range = n, it will run upto n-1. then it will come out of the for loop. 
                                             #then executes else.
    if i == 5:                               # when i==5, if condition is true so it will go to next line break.for loop will now run upto 0 to 5 because of if stmnt. then loop breaks.
        break                               #break stmnt instructs program to exit loop now
else:                                       # else statement will not be executed when break stmnt is executed. So for loop doesnt run completely. it will to go to else stmnt.
    print("This is inside else of for")


# for j in range(10):                          # for loop will execute and print upto 9, then if condition restuns true when j==10. 
#     print(j)
#     if j == 10:
#         break
# else:
#     print("This is inside else of for")      # else statement is executed when for loop  sucessfully executed. when j==10. for loops executes completely.
                                               # so else stmnt is executed

# else statemet executes on suscessful termination of for loop.