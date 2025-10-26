"""
    Practicum Week 1
    Saturday, September 21 - 2025
    
    3. Abstract and Function
        a. Display star-sign pattern

    Nama    : Muhammad Fahmi Rizal
    NIM     : 23525049
"""

def star_pattern(n):
    baris = 1
    while baris <= n:
        print("*" * baris)
        baris = baris+1


N = int(input("N = "))

print()

star_pattern(N)