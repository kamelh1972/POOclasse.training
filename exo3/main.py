# coding: utf8

from books import Book
from reader import Reader
from library import Library
from books_list import books_list

if __name__ == '__main__':
    # We open the library, for now it does not have any book
    library = Library()

    # For each book data in the list, we instanciate a book object and add it to the library
    for books in books_list:
        books = Book(title=books[0], pages=books[1])
        library.add_book(books)

    # A new reader come in the library
    reader = Reader()
    # He wants to borrow a book but this one does not exists so an exception shows up
    reader.borrow_book(library, 'test')
    # Instead he borrows Harry Potter (OK it is not a title but let's keep things simple)
    reader.borrow_book(library, 'Harry Poter')
    # Then he read the whole book
    reader.read_book()
