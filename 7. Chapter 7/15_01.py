 
#simple pyramid pattern

# for i in range(3):             #executes for 0 to 2. means rows=3. i = no of rows = 0,1,2
#     for j in range(3-i):       #executes for 3 to 1. cols=3. j = 3,2,1. 
#         print('*', end='')     #for 1st row j extecutes 3 times then exits loop and i increaments. goes on like this
#     print()

    
# for i in range(3):              # 1st row is only empty space as j has  range = i=0 false stmnt. i =0,1,2
#     for j in range(i):          # if j range is till 3 it will print star in 3 col. when i=0,for loop is false and goes to outer for loop print.
#         print('*', end='')      # i=2, j executes 2 times for i= 0,1. so prints 2 *
#     print()

# # prints * smaller to larger
# for i in range(3):
#     for j in range(i+1):        # to avoid empty space at 1st row, j runs for 1 time for i=0, j runs 2 times for i =1 so on
#         print('*', end='')
#     print()


# upper program in different ways
# prints * larger to smaller 

# prints o/p one by one if we use print() one by one

# difficult to understand. as shown in video

n = 4
for i in range(3):                  #loop runs 0 to 2 times. i idicates rows.for i=0 all print() executes at once one by one
    print('*' * (n-i-1), end="")    #for i = 0, (n-1-i)=3; i=1,(n-1-i)=2; i=2,(n-1-i)=1 row wise * will print in a single line. no leftspace required.
    # print(" " * (n-i-1))          #for rigtspace, for i=0,rs=3; i=1,rs=2; i=2,rs=1. these spaces are not visible. just imagine the rs there.
    print(" " * (i))  
    # print(" " * (n))        
    
   
                                 
