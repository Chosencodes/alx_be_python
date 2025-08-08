class Book:
    """Base Book class with title and author."""
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """EBook adds a file_size attribute (in KB)."""
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = int(file_size)

    def __str__(self) -> str:
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """PrintBook adds a page_count attribute."""
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = int(page_count)

    def __str__(self) -> str:
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """A simple Library demonstrating composition (has-many Books)."""
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book (or subclasses) instances can be added to the library.")
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(str(book))
