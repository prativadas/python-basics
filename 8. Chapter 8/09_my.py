# print pattern using function. 

# n= int(input('enter any num:' ))

# for i in range(n):
#     print('*'*(n-i))

#python function to print such pattern?

#function to print pyramid pattern

def print_pattern(n,i):
      print('*'*(n-i))
      if i<0:                  # when i < 0 is false it comes out of the loop if loop.
          return
      return print_pattern(n,(i-1))

print(print_pattern(4,3))


# def print_pattern(n,i):
#       print('*'*(n+i-1))
#       if i<-1:                  # when i < 0 is false it comes out of the loop if loop.
#           return
#       return print_pattern(n,(i-1))

# print(print_pattern(4,3))