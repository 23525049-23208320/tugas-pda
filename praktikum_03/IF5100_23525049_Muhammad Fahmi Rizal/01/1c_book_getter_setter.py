"""
    Praktikum 3
    IF5100 Programming for Data Analytics
    1. Simple OOP
    1c. Book Class - Getter & Setter

    Nama    : Muhammad Fahmi Rizal
    NIM     : 23525049
"""

class Book(object):
    def __init__(self, title="", author="", price=0):
        self.title = title
        self.author = author
        self.price = price

    # setter
    def set_title(self, title:str):
        self.title = title
    def set_author(self, author:str):
        self.author = author
    def set_price(self, price:float):
        self.price = price
    
    # getter
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def get_price(self):
        return self.price
    
nice_book = Book()

nice_book.set_title("The Psichology of Money")
nice_book.set_author("Morgan Housel")
nice_book.set_price(23000)

print("Title  :",nice_book.get_title())
print("Author :",nice_book.get_author())
print("Price  :",nice_book.get_price())
