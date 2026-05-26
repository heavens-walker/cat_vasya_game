from unit import Unit
import math


class Character(Unit):
    VALID_CLASSES = ("warrior", "mage", "hunter")

    def __init__(self, strength, dexterity, constitution,
                 wisdom, intelligence, charisma, character_class):

  
        if character_class not in self.VALID_CLASSES:
            raise ValueError(
                "Некорректный класс персонажа. "
                "Допустимые классы: warrior, mage, hunter"
            )

        super().__init__(
            strength,
            dexterity,
            constitution,
            wisdom,
            intelligence,
            charisma
        )

        self.character_class = character_class

        # Расчёт характеристик
        self.max_health = self.calculate_max_health()
        self.current_health = self.max_health

        self.damage = self.calculate_damage()
        self.defense = self.calculate_defense()

        self.max_mana = self.calculate_max_mana()
        self.mana = self.max_mana

    def calculate_max_health(self):
        value = self.constitution * 10 + self.strength / 2
        return math.floor(value)

    def calculate_damage(self):
        if self.character_class == "warrior":
            value = self.strength * 2.2 + self.constitution / 3

        elif self.character_class == "mage":
            value = self.intelligence * 2.5 + self.wisdom / 2

        elif self.character_class == "hunter":
            value = self.dexterity * 1.9 + self.strength / 3

        return math.floor(value)

    def calculate_defense(self):
        if self.character_class == "warrior":
            value = self.constitution * 1.8 + self.strength / 4

        elif self.character_class == "mage":
            value = self.wisdom * 1.3 + self.intelligence / 6

        elif self.character_class == "hunter":
            value = self.dexterity * 1.6 + self.constitution / 5

        return math.floor(value)

    def calculate_max_mana(self):
        if self.character_class == "warrior":
            value = self.intelligence + self.strength / 2

        elif self.character_class == "mage":
            value = self.intelligence * 3 + self.wisdom

        elif self.character_class == "hunter":
            value = self.dexterity * 1.5 + self.wisdom / 2

        return math.floor(value)
