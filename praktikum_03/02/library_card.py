"""
    Praktikum 3
    IF5100 Programming for Data Analytics
    2. Library
    2b. LibraryCard Class

    Nama    : Muhammad Fahmi Rizal
    NIM     : 23525049
"""

class LibraryCard(object):
    def __init__(self, card_number="", PIN="", borrowed_books=[]):
        self.card_number = card_number
        self.PIN = PIN
        self.borrowed_books = borrowed_books

    def add_borrowed_book(self, book_id):
        self.borrowed_books.append(book_id)
