"""
    Practicum Week 1
    Saturday, September 21 - 2025
    
    5. Data Structures
        a. List of Indonesian food

    Nama    : Muhammad Fahmi Rizal
    NIM     : 23525049
"""

def print_menu(list):
    x = 0
    for food in list:
        print(f"{x} {food}")
        x = x + 1

#list food
list_indonesian_food = ["Nasi Goreng", "Bakso", "Soto", "Rawon", "Sate", "Gudeg", "Mie Ayam"]

print("- Menu -")
print_menu(list_indonesian_food)
print()

del_index = input("Masukkan nomor yang akan dihapus: ")
print(f"Anda menghapus menu {list_indonesian_food[int(del_index)]}!")
# pop selected index
list_indonesian_food.pop(int(del_index))

print("\n- New Menu -")
print_menu(list_indonesian_food)
