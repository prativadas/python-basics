# a = "35fgrfg34"
# a = int(a)
# print(type(a))
# print(a + 5)


b = '55'
print(type(b))

# print(b+5) throws error as b is a str and 5 is int

# lets convert b to int type

b = int(b)

print(type(b))

print(b + 5) # now this will not throw error


c = '34ghh'
print(type(c))

# c = int(c) throws error as we cant covert c to int as alphabets are also present in it