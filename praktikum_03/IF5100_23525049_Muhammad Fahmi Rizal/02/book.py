"""
    Praktikum 3
    IF5100 Programming for Data Analytics
    2. Library
    2a. Book Class

    Nama    : Muhammad Fahmi Rizal
    NIM     : 23525049
"""

class Book(object):
    def __init__(self, book_id="", title="", author="", genre="", status="available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.status = status