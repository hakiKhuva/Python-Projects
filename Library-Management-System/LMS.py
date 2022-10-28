class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books: 
            print(" *" + book)
    
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")

class Student: 
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ").strip()
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ").strip()
        return self.book
         

if __name__ == "__main__":
    centraLibrary = Library(["DSA", "Machine Learning for Beginners", "C in Depth", "Deep Learning and Computer Vision", "Django", "Clrs", "Python", "IoT", "Cybersecurity"])
    # Assuming only one copy of every book is present
    student = Student()
    # centraLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg = '''\n ======== Welcome to Central Library ========
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: ").strip())
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
