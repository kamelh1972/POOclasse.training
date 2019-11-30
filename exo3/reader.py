# coding: utf8
from library import*

class Reader():
    """"""
    def __init__(self):
        self.books= None
        self.pages = 0


    def borrow_book(self, Library, title):
        """methode qui emprunt un livre et lève une exception si le titre n'est pas disponible"""
        self.books = Library.get_book(title)
        if self.books is None:
            raise Exception
        else:
            self.pages = 1

    def go_to_page(self):
        """methode qui va à la page souhaitee"""
        if current_pages != pages:
            current_pages = pages
            read(pages)


    def next_page(self):
        """ methode qui va à la page suivante"""
        self.page = pages+1
        current_pages = pages
        read(pages)

    def previous_page(self):
        """ methode qui va à la page précédente"""
        self.page = pages-1
        current_pages = pages
        read(pages)

    def read(self):
        """"""
        pass

    def read_book(self):
        """"""
        pass
