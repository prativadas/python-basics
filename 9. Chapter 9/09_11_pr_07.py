content = True                 #initialize var value
i = 1                          # i is a counter that counts the lines in log.txt
with open("log.txt") as f:
    while content:                 #when all lines are read, while condition will be false, then exits
        content = f.readline()     # while loops runs untill f.readline() evaluates true. means when all lines are read, condition is false.
        if 'python' in content.lower():
            print(content)
            print(f"Yes python is present on line number {i}")    #works if python is present in multile lines
        i+=1