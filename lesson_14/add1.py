class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return self.books

library = Library()
book1 = Book("1", "11")
book2 = Book("2", "22")
library.add_book(book1)
library.add_book(book2)
for book in library.get_books():
    print(f'Title: {book.title}, Author: {book.author}')