# --- Inheritance Hierarchy ---

class Book:
    """
    Base Class: Represents a generic book with core attributes.
    """
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        """Standard representation for the base class."""
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """
    Derived Class: Represents a digital book, inheriting from Book.
    """
    def __init__(self, title: str, author: str, file_size: int):
        # Call the base class constructor to initialize title and author
        super().__init__(title, author)
        # Initialize the unique attribute
        self.file_size = file_size

    def __str__(self):
        """Overridden representation to include file size."""
        # Note: We use the inherited attributes (title, author)
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """
    Derived Class: Represents a physical book, inheriting from Book.
    """
    def __init__(self, title: str, author: str, page_count: int):
        # Call the base class constructor to initialize title and author
        super().__init__(title, author)
        # Initialize the unique attribute
        self.page_count = page_count

    def __str__(self):
        """Overridden representation to include page count."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# --- Composition Class ---

class Library:
    """
    Composition Class: Manages a collection of Book, EBook, and PrintBook instances.
    The Library "has a" relationship with the Book objects.
    """
    def __init__(self):
        # Attribute to store all book instances
        self.books = []

    def add_book(self, book: Book):
        """Adds any instance derived from Book to the library's collection."""
        self.books.append(book)

    def list_books(self):
        """
        Prints the details of every book in the collection.
        This automatically demonstrates polymorphism, as print(book) calls 
        the specific __str__ method of the book's actual class (Book, EBook, or PrintBook).
        """
        for book in self.books:
            print(str(book))