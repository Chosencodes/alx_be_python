from library import Book, EBook, PrintBook, Library

# Create library
my_library = Library()

# Add books
book1 = EBook("Python Basics", "John Doe", "123456789", 5)
book2 = PrintBook("Learn OOP", "Jane Smith", "987654321", 300)

my_library.add_book(book1)
my_library.add_book(book2)

# Display all books
for book in my_library.list_books():
    print(book)
