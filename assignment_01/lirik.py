"""
ASSIGNMENT - STRUCTURE TYPES AND MUTABILITY
Functions to Analyze Song Lyrics

Nama    : Muhammad Fahmi Rizal
NIM     : 23525049
"""

# function for create dictionary
def lyric_dictionary(file):
    try:
        with open(file, "r") as file_handle:
            # print("OK! File "+file+" ditemukan dan akan diproses.")

            list_word = []
            #loop per line and split by space
            for line in file_handle:
                list_word += line.split()

            # masukkan ke dictionary {"word":count}
            word_dictionary = {}

            # print list word
            for word in list_word:
                # delete comma or dot or question mark or ()
                true_word = word.replace(",","")
                true_word = true_word.replace(".","")
                true_word = true_word.replace("?","")
                true_word = true_word.replace("(","")
                true_word = true_word.replace(")","")

                # convert to lower case
                true_word = true_word.lower()

                # jika belum ada di dictionary masukkan nilai 1, dan jika sudah ada increment +1 
                if true_word in word_dictionary:
                    word_dictionary[true_word] += 1
                else:
                    word_dictionary[true_word] = 1
            
    except FileNotFoundError:
        print("Error! File "+file+" tidak ditemukan!")
    
    return word_dictionary

# function for get highest frequency tuple
def high_freq_word(dict):
    list_max_word = []

    # get list value
    list_value = dictionary.values()

    # get the highest count
    highest_count = max(list_value)
    
    # loop dictionary to get same frequency
    for word in dict:
        # jika ada key yang sama, masukkan ke dalam tuple
        if dict[word] == highest_count:
            list_max_word.append(word) 

    return (list_max_word, highest_count)


# Input nama file lyric
# file_lirik = input("Masukkan filename Lirik: ")
# file_lirik = "fix_you.txt"
file_lirik = "black_hole_sun.txt"
print("Filename: "+file_lirik)
print("")
print("Word Count Dictionary for Lyric: "+file_lirik)

# call function lyric_dictionary()
dictionary = lyric_dictionary(file_lirik)

# print dictionary
for key in dictionary:
    print("- ", key, ":", dictionary[key])

print("")
print("Tuple Highest Frequency Word for Lyric : "+file_lirik)

# call function high_freq_word()
high_tuple = high_freq_word(dictionary)

# print tuple
print(high_tuple)
