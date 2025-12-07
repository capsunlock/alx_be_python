class Book:
    """
    A class to model a book, implementing key Python magic methods 
    for initialization, representation, and cleanup.
    """
    def __init__(self, title: str, author: str, year: int):
        """
        Constructor (Initializer). Sets the initial state of the Book object.
        """
        self.title = title
        self.author = author
        self.year = year
        print(f"Book instance created: {self.title}")

    def __str__(self):
        """
        String Representation (for human-readable output, like the print() function).
        Format: "(title) by (author), published in (year)"
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official Representation (for developers, showing how to recreate the object).
        Format: "Book('{title}', '{author}', {year})"
        """
        # Ensure string attributes are quoted, but integer year is not.
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """
        Destructor. Called when the object is about to be garbage collected (deleted).
        """
        print(f"Deleting {self.title}")

# Example of __del__ execution timing:
# Note that __del__ is triggered when the reference count to the object drops to zero.
# In the main() function below, 'del my_book' forces this immediately.