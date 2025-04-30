class Book:
    total_books = 0
    
    def __init__(self, title):
        self.title = title
        Book.increment_book_count()
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1


b1 = Book("Book1")
b2 = Book("Book2")
print(f"Total books: {Book.total_books}")
print(f"Book 1 title: {b1.title}")
print(f"Book 2 title: {b2.title}")