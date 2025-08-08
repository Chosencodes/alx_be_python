class Book:
    """A simple Book class demonstrating magic methods:
    - __init__ (constructor)
    - __del__ (destructor)
    - __str__ and __repr__ (string representations)
    """
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = int(year)

    def __str__(self) -> str:
        # User-friendly string representation
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        # Official representation that could recreate the object
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        # Called on object deletion
        print(f"Deleting {self.title}")
