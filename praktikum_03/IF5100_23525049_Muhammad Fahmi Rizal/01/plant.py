"""
    Praktikum 3
    IF5100 Programming for Data Analytics
    1. Simple OOP
    1d. Plant Class
    1f. Display Function

    Nama    : Muhammad Fahmi Rizal
    NIM     : 23525049
"""

class Plant(object):
    def __init__(self, year_planted:int, plant_type:str, plant_name:str):
        self.year_planted = year_planted
        self.plant_type = plant_type
        self.plant_name = plant_name

    def __str__(self):
        return "This "+self.plant_type+" plant with the name "+self.plant_name+" is planted in the year of "+str(self.year_planted)
    
    def cetak(self):
        return "This "+self.plant_type+" plant with the name "+self.plant_name+" is planted in the year of "+str(self.year_planted)