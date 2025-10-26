"""
    Praktikum 2
    (Recursive - Assertion & Exception)
    
    4. Custom Average - Assertions & Exception

    Nama    : Muhammad Fahmi Rizal
    NIM     : 23525049
"""

def custom_average(list_dictionary):
    try:
        #check parameter
        assert type(list_dictionary) is list, "Input must be a list!"
        final_score = []
        #looping
        for student in list_dictionary:
            #check name
            assert student["name"] != "", "Invalid name!"

            #check age
            assert student["age"] >= 18 and student["age"] <=30, "Invalid age!"

            #check grade
            assert type(student["grades"]) is list, "Grades must be a list!"
            sum_grade = 0
            for nilai in student["grades"]:
                assert type(nilai) is int, "Grade must be a integer!"
                assert nilai >=0 and nilai <=100, "Invalid grades!"
                sum_grade += nilai
            
            average_grade = sum_grade/len(student["grades"])
            final_score.append({"name":student["name"], "average_grade":average_grade})

        return final_score
    
    except AssertionError as e:
        return f"Validation failed: {e}"
    
# print list
def print_list(lists):
    x = 0
    for list in lists:
        print(f"{x} : {list}")
        x += 1
    
student_info = [
    [
        {"name": "Alice", "age": 22, "grades": [85, 92, 78]},
        {"name": "Bob", "age": 25, "grades": [88, 90, 92]}
    ],
    [
        {"name": "Charlie", "age": 17, "grades": [92, 90, 75]},
    ],
    
    {"name": "David", "age": 29, "grades": [80, 92, 88]},
    
    [
        {"name": "Fay", "age": 22, "grades": [120, 90, 80]},
    ],
    [
        {"name": "Elva", "age": 23, "grades": 90},
    ],
]

print_list(student_info)
selected_list = int(input(f"\nSelect list number [0-{str(len(student_info)-1)}] : "))

print("\nAverage Grade:")
print(custom_average(student_info[selected_list]))