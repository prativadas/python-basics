with open("sample2.txt") as f:                   #by default takes read mode
    content = f.read()

content = content.replace("donkey", "$%^@$^#")

with open("sample2.txt", "w") as f:
    f.write(content)

