"""
    Praktikum 2
    (Recursive - Assertion & Exception)
    
    5. Alpha AI

    Nama    : Muhammad Fahmi Rizal
    NIM     : 23525049
"""

def generate_password(characters, lenght):
    """
        check length:
        - should be integer
        - max=8
    """
    assert type(lenght) is int, "Lenght must be integer!"
    assert lenght <=8, "Max lenght is 8!"

    """
        validate character:
        - char length > lenght generated password
        - no duplicate char
    """
    assert len(characters) > lenght, "Character lenght must me more than the lenght generated password!"
    duplicate = False
    x = 0
    for cx in characters:
        y = x+1
        for cy in characters[y:len(characters)-1]:
            if cx == cy:
                duplicate = True
                break
            y +=1
        x +=1
    
    assert duplicate==False, "Duplicate character not allowed!"

    
    list = [characters[0:lenght]]
    #get combination after len-1
    for c in characters[lenght:]:
        list += [characters[0:lenght-1]+c]

    # list2 = [characters[0:lenght-1]]
    # #get combination after len-1
    # for c in characters[lenght-1:]:
    #     list2 += [characters[0:lenght-2]+c]


    return list
    
    # #base case
    # if lenght == 0:
    #     return ""
    #  #recursive step
    # else:
    #     return characters[0:lenght-1] + generate_password(characters[lenght+1:],lenght-1)


print(generate_password("ABC123", 4))