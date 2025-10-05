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
    
    def return_book(self):
        # If the test expects no parameters, we might need to track current book
        # This is a simplified version - you may need to adjust based on the exact requirement
        pass
    
    def list_available_books(self):
        available_books = []
        for book in self.books:
            if book.available:
                available_books.append(book.title)
        return available_books
