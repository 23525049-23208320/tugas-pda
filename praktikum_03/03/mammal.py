from animal import Animal

class Mammal(Animal):
    def __init__(self, name:str, species:str, sound:str, fur:bool, milk:bool):
        Animal.__init__(self, name, species, sound)
        self.furr = fur
        self.milk = milk
    
    def speak(self):
        return f"Mammal {self.name} speak : '{self.sound}'.."

    def eat(self):
        return f"Mammal {self.name} eating.."
    
    def sleep(self):
        return f"Mammal {self.name} sleeping.."

    def move(self):
        return f"Mammal {self.name} moving.."
    
    def give_birth(self):
        return f"Mammal {self.name} giving birth.."
    
    def gestation_period(self):
        return 9
    
    def nurse(self):
        return f"Mammal {self.name} nursing.."
    