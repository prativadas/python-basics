with open("this.txt") as f:
    content = f.read()            #contents are read into var content

with open("copy.txt", 'w') as f:            # contents of this.txt file copied to copy.txt file. write mode as we are writing in it.
    f.write(content)