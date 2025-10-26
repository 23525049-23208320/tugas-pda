"""
    Praktikum 3
    IF5100 Programming for Data Analytics
    2. Library
    2c. Library Class

    Nama    : Muhammad Fahmi Rizal
    NIM     : 23525049
"""
import global_var

class Library(object):
    def __init__(self, library_code="", book_list=[], library_status="closed"):
        self.library_code = library_code
        self.book_list = book_list
        self.library_status = library_status

    def insert_card(self, card):
        # if card inserted
        if card.card_number != "":
            self.library_status = "open"

    def validate_pin(self, card, pin):
        # validate pin
        if card.PIN == pin:
            return True
        return False
    
    def add_book(self, book):
        self.book_list.append(book)

    def print_books(self):
        for book in self.book_list:
            print(f"{book.book_id} | {book.title} | {book.author} | {book.genre} | {book.status}")

    def borrow_book(self, card, book_id):
        # max borrow
        if len(card.borrowed_books) >= global_var.MAX_BORROW_BOOK:
            print("You have reach max limit borrow!")
            return False
        
        # search availability book
        for s in self.book_list:
            if s.book_id == book_id and s.status == "available":
                print("Book found and available!")
                print("Processing..")
                card.add_borrowed_book(book_id)
                s.status = "not available"
                return True
        
        print("Book not found or not available!")
        return False
        
    def display_borrowed_books(self, card):
        for book_id in card.borrowed_books:
            for book in self.book_list:
                if book.book_id == book_id:
                    print(f"{book.book_id} | {book.title} | {book.author} | {book.genre}")


    def return_book(self, card):
        for book_id in card.borrowed_books:
            for book in self.book_list:
                if book.book_id == book_id:
                    book.status = "available"
        # reset 
        card.borrowed_books = []