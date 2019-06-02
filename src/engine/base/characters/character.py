''' Abstract Character Class '''
from src.engine.core.model import Model

TABLE = "characters"
PK = "name"


class Character(Model):
    '''
    Abstact Class for a generic characters within the game

    Attributes:
        name: String of the name of the character
        race: String of the race of the character
        class_name: String of the characters given player class
        inventory: Dictionary of a characters inventory

    '''
    def __init__(self, name: str, race: str, class_name: str, inventory: dict):

        super().__init__(TABLE, PK)
        self.name = name
        self.race = race
        self.class_name = class_name
        self.inventory = inventory

    def print(self):
        print("Character")
