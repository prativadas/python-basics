try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
    exit()                       #if we comment out this, tr-except-finally loop doesnt exit and pprint last msg if error occurs.

finally:                        # finally ensures execution of code irrespective of errors. even if we exit program, finally will execute.
    print("We are done")

print("Thanks for using the program")   # runs when no exception occurs