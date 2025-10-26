from animal import Animal

class Bird(Animal):
    def __init__(self, name:str, species:str, sound:str, wing:bool, lay_eggs:bool):
        Animal.__init__(self, name, species, sound)
        self.wing = wing
        self.lay_eggs = lay_eggs
    
    def speak(self):
        return f"Bird {self.name} speak : '{self.sound}'"

    def eat(self):
        return f"Bird {self.name} eating.."
    
    def sleep(self):
        return f"Bird {self.name} sleeping.."

    def move(self):
        return f"Bird {self.name} moving.."
    
    def fly(self):
        return f"Bird {self.name} flying.."
    
    def nest(self):
        return f"Bird {self.name} nesting.."
    
    def lay_eggs(self):
        return f"Bird {self.name} laying eggs.."
    