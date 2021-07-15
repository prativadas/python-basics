num = int(input("Enter your number: "))

table = [num*i for i in range(1, 11)]
print(table)
with open("tables.txt", "a") as f:                #append values in the file
    f.write(str(table))                           # all contents in file is printed as str by default so use str
    f.write('\n')