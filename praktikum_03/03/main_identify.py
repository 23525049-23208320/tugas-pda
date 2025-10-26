from cat import Cat
from dog import Dog
from parrot import Parrot
from chicken import Chicken


selected_species = '1'

while int(selected_species) >0:
    print("\n.: Animal Identification :.")
    print("[1] Cat")
    print("[2] Dog")
    print("[3] Chicken")
    print("[4] Parrot")

    print("\n[0] Exit")

    selected_species = input("\nSelect Menu [0-4] : ")

    if int(selected_species) > 0:
        list_species = [Cat, Dog, Chicken, Parrot]
        list_name = ["Jelly", "Daisy", "Badut", "Parry"]

        SelectedSpecies = list_species[int(selected_species)-1]
        selected_name = list_name[int(selected_species)-1]

        animal = SelectedSpecies(selected_name)

        print()
        for attr in dir(animal):
            method = getattr(animal, attr)

            # skip private methods and non-callables
            if callable(method) and not attr.startswith("__") and not attr.startswith("eat"):
                print(method())

        again = input("\nDo you want to identify more animal? [Y/N] : ")
        if not (again == 'Y' or again == 'y'):
            selected_species = 0



