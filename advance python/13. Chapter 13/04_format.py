# f string is introduced in python 3.6

name = "Harry"
channel = "CodeWithHarry"
type = "Coding"

# a = f"This is {name}"                          ## f-string example
# a = "This is {}".format(name)

# format method 

# a = "This is {} and his channel is {}".format(name, channel)
# a = "This is {0} and his {2} channel is {1}".format(name, channel, type)    # when we want to print arguments in different order, then use the index
a = "This is {} and his {} channel is {}".format(name, channel, type)

print(a)