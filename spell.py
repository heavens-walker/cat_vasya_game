from abc import ABC, abstractmethod

class Spell(ABC):
    def __init__(self, name, damage, mana_cost):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
    @abstractmethod
    def cast(self):
        pass
