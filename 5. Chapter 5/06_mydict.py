my_dict = {
    "temple": "mandir",
    "dog": "kutta",
    "cat": "billi"
}

print(my_dict)

print(my_dict.keys())

print(my_dict.items())

print(my_dict.values())

user = input("enter any key:")

#print('the corresponding value of the key is:', my_dict[user]) # this line will throw error 
                                                                #if you enter an invalid key not present in you dict

print('the corresponding value of the key is:', my_dict.get(user))  # will return None if key entered not present in the dict.

