# f = open('another.txt', 'w')  #creates a new txt file
# f.write("I am cooking") #overwrites in the txt file.

# # data = f.read()      # as f is open in w mode, we cant read.

# # print(data)        #why cant we print datahere

# f = open('another.txt', 'r')  # for reading the data, open in r mode.
# data = f.read()
# print(data) 


# f.close()

# for appending
f = open('another.txt', 'a')
f.write('i am appending')  # append at the end
f.close()