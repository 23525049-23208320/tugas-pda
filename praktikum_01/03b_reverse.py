"""
    Practicum Week 1
    Saturday, September 21 - 2025
    
    3. Abstract and Function
        b. Reversed order string

    Nama    : Muhammad Fahmi Rizal
    NIM     : 23525049
"""

def convert_string(text):
    new_str = ""
    index = len(text)
    while index > 0:
        new_str = new_str + text[index-1]
        index = index - 1
    return new_str

string = input("Masukkan string : ")

print("Hasil reverse   :",convert_string(string))