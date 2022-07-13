class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books: 
            print(" *" + book)
    
    def borrowBook(self, bookName):
        if bookName in self.books:
            f = open("Library Book Reciept.txt", "w")
            StudentName = input("Enter your name: ")
            StudentContact = input("Enter you contact number: ")
            StudentRoll = input("Enter your roll number:")
            print("Book has been issued! Please collect the reciept")
            f.write("Book issued successfully \n")
            f.write(f"Name of student: {StudentName}\n")
            f.write(f"Roll Number of student: {StudentRoll}\n")
            f.write(f"Contact Number of student: {StudentContact}\n")
            f.write(f"Book Issued: {bookName} \n")
            f.write("Please return the book within 30 days of issued date")
            self.books.remove(bookName)

        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
 
    def returnBook(self, bookName):
        f = open("Library Book Reciept.txt", "w")
        StudentName = input("Enter your name: ")
        StudentContact = input("Enter you contact number: ")
        StudentRoll = input("Enter your roll number:")
        f.write("Book returned successfully \n")
        f.write(f"Name of student: {StudentName}\n")
        f.write(f"Roll Number of student: {StudentRoll}\n")
        f.write(f"Contact Number of student: {StudentContact}\n")
        f.write(f"Book Returned: {bookName} \n")
        print("Thanks for returning this book! \n Hope you enjoyed reading it\n")
        self.books.append(bookName)




if __name__ == "__main__":
    centraLibrary = Library(["physics", "chemistry", "maths", "english", "hindi"])
    while True: 
        welcomemsg = '''Welcome to central library 
press 1 : List all the books
press 2 : Borrow book
press 3 : Return book
press 4 : Exit Library'''
        
        print(welcomemsg)
        user  =  int(input("Enter your choice: "))
        if user == 1:
            centraLibrary.displayAvailableBooks()

        elif user == 2:
            x = input("Enter book name you want to borrow: ")
            centraLibrary.borrowBook(x)

        elif user == 3:
            y= input("Enter Book name which you want to return: ")
            centraLibrary.returnBook(y)
        
        elif user == 4:
            print("Thanks for using this library")
            exit()
        
        else:
            print("Invalid Choice! Enter a valid number")
