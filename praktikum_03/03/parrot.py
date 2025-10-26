from bird import Bird

class Parrot(Bird):
    def __init__(self, name:str, species="Parrot", sound="cuit..cuit..cuit..", wing=True, lay_eggs=True, can_talk=True):
        Bird.__init__(self, name, species, sound, wing, lay_eggs)
        self.can_talk = can_talk
    
    def speak(self):
        return f"{self.name} the {self.species} is speaking : '{self.sound}'.."

    def eat(self):
        return f"{self.name} the {self.species} is eating.."
    
    def sleep(self):
        return f"{self.name} the {self.species} is sleeping.."

    def move(self):
        return f"{self.name} the {self.species} is moving.."
    
    def fly(self):
        return f"{self.name} the {self.species} is flying.."
    
    def nest(self):
        return f"{self.name} the {self.species} is nesting.."
    
    def lay_eggs(self):
        return f"{self.name} the {self.species} is laying eggs.."
    
    def talk(self):
        return f"{self.name} the {self.species} is talking.."
    
    def imitate(self):
        return f"{self.name} the {self.species} is imitating.."
    
    def dance(self):
        return f"{self.name} the {self.species} is dancing.."
    