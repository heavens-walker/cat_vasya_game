from spell import Spell

class Fireball(Spell):
    def __init__(self):
        super().__init__("Fireball", 35, 15)
    
    def cast(self):
        return self.damage

class IceLance(Spell):
    def __init__(self):
        super().__init__("IseLance", 25, 10)
    
    def cast(self):
        return self.damage

class LightningBolt(Spell):
    def __init__(self):
        super().__init__("LightningBolt", 40, 20)

    def cast(self):
        return self.damage
