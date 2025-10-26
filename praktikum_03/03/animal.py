class Animal(object):
    def __init__(self, name:str, species:str, sound:str):
        self.name = name
        self.species = species
        self.sound = sound
    
    def speak(self):
        return f"Animal {self.name} speak : '{self.sound}'.."

    def eat(self):
        return f"Animal {self.name} eating.."
    
    def sleep(self):
        return f"Animal {self.name} sleeping.."

    def move(self):
        return f"Animal {self.name} moving.."