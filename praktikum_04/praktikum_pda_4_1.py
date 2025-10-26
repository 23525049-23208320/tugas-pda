"""
    Praktikum 4

    1. Pendekatan Brute Force

    Nama    : Muhammad Fahmi Rizal
    NIM     : 23525049
"""

def get_index(arr_num, target):
    arr_lenght = len(arr_num)

    # check constrait
    assert arr_lenght >=2 and arr_lenght<=1000, "Array lenght must be between 2 - 1000"
    assert target >= -10000000 and target <=10000000, "Target must be between -10,000,000 - 10,000,000"
    for x in arr_num:
        assert x >=  -10000000 and x <=10000000, "Value array must be between -10,000,000 - 10,000,000"

    print()
    i = 0
    while i<arr_lenght:
        j = i+1
        while j<arr_lenght:
            if (arr_num[i]+arr_num[j]) == target:
                return f"Output: [{i},{j}]" 
            j += 1
        i += 1

def print_input(x, arr_num, target):
    print(f"Example {x}:")
    print(f"Input: nums = {arr_num}, target = {target}")

arr_example =[{"nums":[3,4,5,6], "target":7},
              {"nums":[4,5,6], "target":10},
              {"nums":[5,5], "target":10}]

x = 1
for example in arr_example:
    print(f"[{x}] nums = {example["nums"]}, target = {example["target"]}")
    x += 1

pilihan = int(input("\nMasukkan pilihan example: "))
index = pilihan-1
nums = arr_example[index]["nums"]
target = arr_example[index]["target"]

print()
print_input(pilihan, nums, target)
print(get_index(nums, target))