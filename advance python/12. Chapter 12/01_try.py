while(True):
    print("Press q to quit")           #indicates what to type to quit game
    a = input("Enter a number: ")   #throws error if entered anything other than int
    if a == 'q':                   # exits while loop when entered q 
        break
    try:                         # if user entered anything other than int or q, the error is handled by try
        print("Trying...")
        a = int(a)
        if a>6:
            print("You entered a number greater than 6")
    except Exception as e:
        print(f"Your input resulted in an error: {e}")       #the error is printed

print("Thanks for playing this game")   #when while loop exits, this prints.