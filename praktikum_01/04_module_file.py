"""
    Practicum Week 1
    Saturday, September 21 - 2025
    
    4. Modules and Files

    Nama    : Muhammad Fahmi Rizal
    NIM     : 23525049
"""

#delete content if not empty
def delete_content_if_not_empty(filename):    
    with open(filename, 'r+') as file_del:
        content = file_del.read()
        if content != "":
            file_del.truncate(0)

# save to file
def save_to_file(string, filename):
    with open(filename, 'a') as file_write:
        file_write.write(string+'\n')

# check even number
def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# read file
def read_file(filename):
    with open(filename, "r") as file_read:
        print(file_read.read())


file = "First_Ten_Even_Numbers.txt"
delete_content_if_not_empty(file)

# get first ten even number
i = 1
even = 0
while even < 10:
    if check_even(i) == True:
        save_to_file(str(i), file)
        even = even + 1
    i = i + 1

# call read_file function
read_file(file)