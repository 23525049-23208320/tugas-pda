import random
from cat import Cat
from dog import Dog
from parrot import Parrot
from chicken import Chicken

# predator name
predator_name = ["Jim", "Tom", "Jerry", "Becky", "Mikey", "Garry"]

# predator species
predator_species = [Cat, Dog]

# prey name
prey_name = ["Tweety", "Patty", "Skippy", "Tony", "Parry", "Steve"]

# prey species
prey_species = [Parrot, Chicken]

# get random predator
SelectedPredator = random.choice(predator_species)
selected_predator_name = random.choice(predator_name)
predator = SelectedPredator(selected_predator_name)

# get random prey
SelectedPrey = random.choice(prey_species)
selected_prey_name = random.choice(prey_name)
prey = SelectedPrey(selected_prey_name)

print(predator.eat(prey))