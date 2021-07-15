try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
else:                              #executes only if the try was successful, means when try runs sucessfully, it doesnt go to except.
    print("We were successful")