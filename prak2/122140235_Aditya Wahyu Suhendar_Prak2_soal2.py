import time

# Decorator to check if the book is available
def check_availability(func):
    def wrapper(*args, **kwargs):
        if args[0].available:
            result = func(*args, **kwargs)
            args[0].available = False  # Mark the book as borrowed
            return result
        else:
            print(f"Sorry, {args[0].title} is not available for borrowing.")
    return wrapper

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        print(f"Book '{self.title}' by {self.author} added to the library.")

    def __del__(self):
        print(f"Book '{self.title}' by {self.author} returned to the library.")

    @check_availability
    def borrow_book(self):
        print(f"Book '{self.title}' by {self.author} has been borrowed.")

# Creating instances of Book
book1 = Book(title="Introduction to Python", author="John Smith", isbn="978-1-1234-5678-9")
book2 = Book(title="Data Science Essentials", author="Jane Doe", isbn="978-2-9876-5432-1")

# Borrowing books
book1.borrow_book()  # This should be successful
book2.borrow_book()  # This should be successful

# Attempting to borrow an already borrowed book
book1.borrow_book()  # This should fail

# Returning a book to the library
del book1  # This triggers the destructor and prints a return message
