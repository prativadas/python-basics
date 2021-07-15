def greet(name):
    print(f"Good morning, {name}")    #reuse this block of code in m07_file2.py by importing this file. import allowed when file name starts with alphabet

# print(__name__)         #__name__ evaluates to the name of module from where the program is ran
                          # for this file module is __main__
                          # for m07_file2.py, this prints module name as m06_file1.py
if __name__ == "__main__":        # acts as entry point for a prog  # the below codes executes only when its running from same file, it doesnt run in m07_file2.py when importing this file.
    n = input("Enter a name\n")
    greet(n)
