class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

# Creating an instance of the Book class
book1 = Book("To Kill a Mockingbird", "Harper Lee", 0)

# Setting the publication year for the book1 instance
book1.publication_year = 1960

# Printing the details of the book to verify
print(f"Title: {book1.title}")
print(f"Author: {book1.author}")
print(f"Publication Year: {book1.publication_year}")
