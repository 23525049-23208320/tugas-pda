from bird import Bird

class Chicken(Bird):
    def __init__(self, name:str, species="Chicken", sound="petok..petok..petok..", wing=True, lay_eggs=True, can_talk=False):
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
    
    def fight(self):
        return f"{self.name} the {self.species} is fighting.."
    
    def run(self):
        return f"{self.name} the {self.species} is running.."
    
    def sleep(self):
        return f"{self.name} the {self.species} is sleeping.."
    