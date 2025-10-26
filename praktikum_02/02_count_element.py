"""
    Praktikum 2
    (Recursive - Assertion & Exception)
    
    2. Count Element - Recursive concept

    Nama    : Muhammad Fahmi Rizal
    NIM     : 23525049

"""

def count_element(element, list_number):
    # base case: jika elemen list tinggal 1 dan value nya sama dengan yang dicari -> return 1
    if len(list_number) == 1 and list_number[0] == element:
        return 1
    # base case: jika elemen list tinggal 1 dan value nya tidak sama dengan yang dicari -> return 0
    elif len(list_number) == 1 and list_number[0] != element:
        return 0
    # recursive step: hasil pencarian karakter dengan elemen yang paling terakhir + hasil pencarian pada list elemen range [0:len-1] 
    else:
        if list_number[len(list_number)-1] == element:
            found = 1
        else:
            found = 0
        return found + count_element(element, list_number[0:len(list_number)-1])

# print list
def print_list(lists):
    x = 0
    for list in lists:
        print(f"{x} : {list}")
        x += 1

search_list = [[1, 2, 2, 3, 2, 4, 2, 5], 
         [21, 42, 52, 53, 21, 42, 20, 50], 
         [11, 21, 21, 30, 20, 40, 20, 50]]

print_list(search_list)
selected_list = int(input("\nSelect list number [0-2] : "))

element = int(input("Search element : "))
print(f"\nCount element {element} :",str(count_element(element, search_list[selected_list])))