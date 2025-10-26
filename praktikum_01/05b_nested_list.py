"""
    Practicum Week 1
    Saturday, September 21 - 2025
    
    5. Data Structures
        b. Nested list

    Nama    : Muhammad Fahmi Rizal
    NIM     : 23525049
"""

nested_list = [[3,4,7], [5,3,7], [8,4,-3], [9,3,1]]

index_kolom = 0
str_kolom = "Index Number |"
for kolom in nested_list[0]:
    str_kolom = str_kolom+"   "+str(index_kolom)
    index_kolom = index_kolom + 1
print(str_kolom)
print("--------------------------------")

index_baris = 0
for baris in nested_list:
    str_baris = str(index_baris)+"            |"
    for kolom in baris:
        str_baris = str_baris+"   "+str(kolom)
    index_baris = index_baris + 1
    
    print(str_baris)