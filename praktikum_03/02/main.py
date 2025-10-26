"""
    Praktikum 3
    IF5100 Programming for Data Analytics
    2. Library
    2d. Main Program

    Nama    : Muhammad Fahmi Rizal
    NIM     : 23525049
"""

from book import Book
from library_card import LibraryCard
from library import Library

kartu_perpus = LibraryCard("P001.01", "1234")
perpus = Library("P001")

# insert card
print("Inserting Card...")
perpus.insert_card(kartu_perpus)
print("Library Status :",perpus.library_status)

# validate PIN
print("\nValidating PIN...")
status_pin = False
while(status_pin==False):
    pin = input("Input PIN number: ")
    status_pin = perpus.validate_pin(kartu_perpus, pin)
    if status_pin:
        print("PIN is correct!\n")
    else:
        print("PIN is incorrect! Please try again.\n")

# library's book
book_1 = Book("B001", "Start With Why", "Simon Sinek", "Motivation")
book_2 = Book("B002", "The Psychology of Money", "Morgan Housel", "Self Improvement")
book_3 = Book("B003", "Culture Code", "Daniel Coyle", "Office")
book_4 = Book("B004", "The Pheonix Project", "Kim, Behr, Spafford", "DevOps")
book_5 = Book("B005", "Mathematical Thinking", "Albert Rutherford", "Math")

# insert book 
perpus.add_book(book_1)
perpus.add_book(book_2)
perpus.add_book(book_3)
perpus.add_book(book_4)
perpus.add_book(book_5)

menu = '1'

while int(menu) >0:
    # library's menu
    print(".: MAIN MENU :.")
    print("[1] Borrow Books")
    print("[2] Return Books")

    print("\n[0] Exit")

    menu = input("\nSelect Menu [0-2] : ")

    # menu 1
    if menu == '1':

        print("\n>> Borrow Book")

        # borrow book
        again = 'Y'
        while again == 'Y' or again == 'y':
            # cetak pilihan buku
            perpus.print_books()
            book_id = input("\nInsert Book ID : ")
            perpus.borrow_book(kartu_perpus, book_id)

            # cetak borrowed book
            print(f"\nBorrowed Books Card Number {kartu_perpus.card_number} :")
            perpus.display_borrowed_books(kartu_perpus)

            again = input("\nDo you want to borrow more book? [Y/N] : ")

            print("\nThank you for borrowing our books! Don't forget to return it! :)")
    
    elif menu == '2':
        print("\n<< Return Book")

        if len(kartu_perpus.borrowed_books) > 0:
            # cetak borrowed book
            print(f"\nBorrowed Books Card Number {kartu_perpus.card_number} :")
            perpus.display_borrowed_books(kartu_perpus)

            return_book = input("\nDo you want to return all books? [Y/N] : ")

            if return_book == 'Y' or return_book == 'y':
                perpus.return_book(kartu_perpus)
                print("Thank you for returning the books! :)\n")

        else:
            print("You don't have any borrowed books!\n")

print("\nGood Bye! :)")
# borrow books
# perpus.borrow_book(kartu_perpus, book_1)