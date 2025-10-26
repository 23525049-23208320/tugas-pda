"""
    Practicum Week 1
    Saturday, September 21 - 2025
    
    2. Conditional Statement and Looping

    Nama    : Muhammad Fahmi Rizal
    NIM     : 23525049
"""

a = int(input("Input A: "))
b = int(input("Input B: "))

print()

if a > 10 and b < 10 and a > 0 and b > 0:
    print("Do add (+) operation on A and B")
    print(f"A + B = {str(a+b)}")
elif a<=10 and b < 10 and a > 0 and b > 0:
    print("Do subtract (-) operation on A and B")
    print(f"A - B = {str(a-b)}")
elif a>10 and b >= 10 and a > 0 and b > 0:
    print("Do division (/) operation on A and B")
    print(f"A / B = {str(a/b)}")
elif a<=10 and b >= 10 and a > 0 and b > 0:
    print("Do multiply (*) operation on A and B")
    print(f"A * B = {str(a*b)}")
else:
    print("Input number <A> and <B> is invalid!")