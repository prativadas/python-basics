name = input("Enter your name: ")
marks = input("Enter your marks: ")   # we didnt typecast to int as we only display, no operations required.
phone = input("Enter you phone Number: ")

# template = "The name of the student is {}, his marks are {} and phone number is {} "
# output = template.format(name, marks, phone)
# print(output)

#also we can write like this

a = "The name of the student is {}, his marks are {} and phone number is {} ".format(name, marks, phone)
print(a)