class Library:                                 
    def __init__(self, listOfBooks):            #constructor- instantiates object
        self.books = listOfBooks                # books is an class attr         
 
    def displayAvailableBooks(self):          #function displays all books available
        print("Books present in this library are: ")
        for book in self.books: 
            print(" *" + book)
    
    def borrowBook(self, bookName):    
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)          #when a book is being issued to someone it will be removed from available boo lists
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False

    def returnBook(self, bookName):             #when book is retuned it will be added to th book list
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")

class Student: 
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book
         

if __name__ == "__main__":                   # entrypoint for program
    centraLibrary = Library(["Algorithms", "Django", "Clrs", "Python Notes"]) # Library class object. initialize by constructor __init__    
    student = Student()                          # object of student class
    # centraLibrary.displayAvailableBooks()
    while(True):               #its an infinite loop
        welcomeMsg = '''\n ====== Welcome to Central Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centraLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")

        
