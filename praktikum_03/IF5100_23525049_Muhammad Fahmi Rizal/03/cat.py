from mammal import Mammal

class Cat(Mammal):
    def __init__(self, name:str, species="Cat", sound="meow..meow..meow..", fur=True, milk=True, is_pet=True):
        Mammal.__init__(self, name, species, sound, fur, milk)
        self.is_pet = is_pet
    
    def speak(self):
        return f"{self.name} the {self.species} is speaking : '{self.sound}'"

    def eat(self, prey):
        return f"{self.name} the {self.species} is eating {prey.name} the {prey.species}.."
    
    def sleep(self):
        return f"{self.name} the {self.species} is sleeping.."

    def move(self):
        return f"{self.name} the {self.species} is moving.."
    
    def give_birth(self):
        return f"{self.name} the {self.species} is giving birth.."
    
    def gestation_period(self):
        return 9
    
    def nurse(self):
        return f"{self.name} the {self.species} is nursing.."
    
    def meow(self):
        return f"{self.name} the {self.species} is meowing.."
    
    def purr(self):
        return f"{self.name} the {self.species} is purring.."
    
    def scratch(self):
        return f"{self.name} the {self.species} is scratching.."