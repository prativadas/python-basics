# join() - creates a str from iterable objects

l = ["Camera", "Laptop", "Phone", "ipad", "Hard Disk", "Nvidia Graphic 3080 card"]    # we can also use tuple instead of list

# sentence = "~~".join(l)
# sentence = "==".join(l)
sentence = "\n".join(l)
print(sentence)
print(type(sentence))         #returns str not list here.