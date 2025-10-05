class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class Library:
    def __init__(self):
        self.books = []
        self.current_book = None  # Track the currently checked out book
    
    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
    
    def check_out(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                self.current_book = book  # Store the current book
                return True
        return False
    
    def return_book(self):
        if self.current_book and not self.current_book.available:
            self.current_book.available = True
            returned_title = self.current_book.title
            self.current_book = None
            return True
        return False
    
    def list_available_books(self):
        available_books = []
        for book in self.books:
            if book.available:
                available_books.append(book.title)
        return available_books
