"""
    Praktikum 3
    IF5100 Programming for Data Analytics
    1. Simple OOP
    1a. Maximum Price

    Nama    : Muhammad Fahmi Rizal
    NIM     : 23525049
"""

class Product(object):
    def __init__(self, prices):
        self.prices = prices

    def get_max_price(self):
        max = 0
        for price in self.prices:
            if price > max:
                max = price
        return max
    
# Array Price
arr_price = [3000, 5000, 35000, 12000, 67000, 16000]

product = Product(arr_price)

print("Maximum Price Product :",product.get_max_price())