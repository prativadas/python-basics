def readFile(filename):
    try:
        with open(filename, "r") as f:         # opening file in read mode.
            print(f.read())                    # prints content of file
    except FileNotFoundError:             
        print(f"File {filename} is not found")
        
readFile("1.txt")        # function call that prints contents of eaach file
readFile("2.txt")
readFile("3.txt")