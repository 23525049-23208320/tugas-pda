"""
    Practicum Week 1
    Saturday, September 21 - 2025
    
    5. Data Structures
        c. List and Dictionary

    Nama    : Muhammad Fahmi Rizal
    NIM     : 23525049
"""

student = [
            {"Name":"Adi", "Age":34, "NIM":"23524001"},
            {"Name":"Budi", "Age":26, "NIM":"23524001"},
            {"Name":"Cahyo", "Age":28, "NIM":"23524001"},
            ]

max_char = 7
index_kolom = 0
str_kolom = "Index Number"
for key, value in student[0].items():
    str_kolom = str_kolom+" | "+str(key)+" "*(max_char-len(str(key)))
    index_kolom = index_kolom + 1
print(str_kolom)
print("-----------------------------------------------")

index_baris = 0
for row in student:
    # print(row)
    str_baris = str(index_baris)+"           "
    for key, value in row.items():
        str_baris = str_baris+" | "+str(value)+" "*(max_char-len(str(value)))
    index_baris = index_baris + 1
    print(str_baris)
