words = ["donkey", "kaddu", "mote"]             #given a list of words that needs to be rplaced.

with open("sample3.txt") as f:
    content = f.read()


for word in words:
    content = content.replace(word, "$%^@$^#")
    with open("sample3.txt", "w") as f:
        f.write(content)