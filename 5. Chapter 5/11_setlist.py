#s = {8, "8", ["s", 7]}  # will throw error as we sets cant have list inside them. lists items can be updated later 
                        #which is not valid for sets.
                        # unhashable type.

print(s)

s = {8, "8"}

print(s)

s1 = {8, ("a", "8")}  # set can have tuples. as tuple items cant be changed later.

print(s1)