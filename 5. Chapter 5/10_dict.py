mydict = {}

print(type(mydict))

# dont forget to use comma between key,value pair

mydict = {
    "raj" : input("enter fav lang of raj:"), 
    "rahul" : input("enter fav lang of rahul:"), 
    "rohit" : input("enter fav lang of rohit:")
}

print(mydict)

if 2 keys are same what will happen : last entry will be in the output as that key will be updated and given the latest value.
keys will be unique always

mydict = {
    "raj" : input("enter fav lang of raj:"), 
    "rahul" : input("enter fav lang of rahul:"), 
    "raj" : input("enter fav lang of raj:")    
}

print(mydict)

if 2 values are same. then everything will be printed

mydict = {
    "raj" : input("enter fav lang of raj:"), 
    "rahul" : input("enter fav lang of rahul:"), 
    "rohit" : input("enter fav lang of rohit:")    
}

print(mydict)
