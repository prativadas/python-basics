with open("log.txt") as f:
    content = f.read()

if 'python' in content.lower():                 # search will be case sensitive. lower case will be checked
    print("Yes python is present")
else:
    print("No python is not present")