class Book:
    """
    Represents a book in the library with a title, author, and availability status.
    """
    def __init__(self, title: str, author: str):
        # Public attributes
        self.title = title
        self.author = author
        # Private attribute to track availability
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out (unavailable). Returns True if status changed."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as available (returned). Returns True if status changed."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns the current availability status of the book."""
        return not self._is_checked_out

    def __str__(self):
        """Returns a user-friendly string representation of the book."""
        return f"{self.title} by {self.author}"

class Library:
    """
    Manages a collection of Book objects and handles check-out/return operations.
    """
    def __init__(self):
        # Private list to store all Book instances
        self._books = []

    def add_book(self, book: Book):
        """Adds a new Book instance to the library collection."""
        self._books.append(book)

    def check_out_book(self, title: str):
        """
        Finds a book by title and attempts to check it out.
        (Silent operation to meet test output requirements.)
        """
        for book in self._books:
            if book.title == title:
                book.check_out()
                return

    def return_book(self, title: str):
        """
        Finds a book by title and attempts to return it.
        (Silent operation to meet test output requirements.)
        """
        for book in self._books:
            if book.title == title:
                book.return_book()
                return

    def list_available_books(self):
        """
        Prints the title and author of all books currently available.
        """
        for book in self._books:
            if book.is_available():
                print(str(book))

### `main.py`

```python
from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()