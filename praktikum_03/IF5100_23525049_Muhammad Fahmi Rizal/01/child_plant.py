"""
    Praktikum 3
    IF5100 Programming for Data Analytics
    1. Simple OOP
    1e. Child Class
    1g. Polymorphism Flower Class

    Nama    : Muhammad Fahmi Rizal
    NIM     : 23525049
"""

from plant import Plant

class Tree(Plant):
    pass

class Shrub(Plant):
    pass

class Flower(Plant):
    def __init__(self, year_planted, plant_type, plant_name, farmer_name):
        Plant.__init__(self, year_planted, plant_type, plant_name)
        self.farmer_name = farmer_name

    def __str__(self):
        return "This "+self.plant_type+" named "+self.plant_name+" was planted in "+str(self.year_planted)+" by "+self.farmer_name

    def cetak(self):
        return "This "+self.plant_type+" named "+self.plant_name+" was planted in "+str(self.year_planted)+" by "+self.farmer_name
