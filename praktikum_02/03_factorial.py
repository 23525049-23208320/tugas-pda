"""
    Praktikum 2
    (Recursive - Assertion & Exception)
    
    3. Recursive Factorial - Recursive concept & assertions

    Nama    : Muhammad Fahmi Rizal
    NIM     : 23525049
"""

def recursive_factorial(number, limit):
    #excessive recursion depth
    assert limit > 0, "Excessive Recursion Depth!"
    
    #base case: jika 1! return 1
    if number == 1:
        return 1

    #recursive step: angka * faktorial(angka-1)
    else:
        return number * recursive_factorial(number-1, limit-1)
    
    
    
input_fact = int(input("Masukkan angka : "))
assert input_fact > 0, "Masukkan inputan positif integer!"

input_limit = int(input("Masukkan limit : "))
assert input_limit > 0, "Masukkan inputan positif integer!"

print(f"\nFaktorial dari {input_fact}! =", recursive_factorial(input_fact, input_limit))
