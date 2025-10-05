class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
    
    def check_out(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                return True
        return False
    
    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                return True
        return False
    
    def list_available_books(self):
        available_books = []
        for book in self.books:
            if book.available:
                available_books.append(book.title)
        return available_books
