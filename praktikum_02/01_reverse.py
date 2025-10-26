"""
    Praktikum 2
    (Recursive - Assertion & Exception)
    
    1. Reverse String - Recursive concept

    Nama    : Muhammad Fahmi Rizal
    NIM     : 23525049
"""

def reverse_string(text):
    # base case: jika jumlah karakter tinggal 1, maka return karakter tersebut
    if len(text) == 1:
        return text[0]
    # recursive step: karakter elemen terakhir + reverse karakter elemen ke 0 sampai lenght-1
    else:
        return text[-1] + reverse_string(text[0:len(text)-1])

string = input("Masukkan string : ")

print("Hasil reverse   :",reverse_string(string))