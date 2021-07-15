# reverse right angle pyramid

n = 3
for i in range(3):                   # i = 0,1,2. i indicates rows
    print(" " * (n-i-1), end="")     # print space in left side. for i=0, leftspace=2, i=1, leftspace=1 so on
    print("*" * (2*i+1), end="")     # print *, odd number of * printed. for i=0, * printed= 1 so on
    print(" " * (n-i-1))             # print space in right side. for i=0,rs=2; i=1,rs=1 so on

