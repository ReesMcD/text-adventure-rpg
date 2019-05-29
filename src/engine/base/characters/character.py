''' Character Module '''
from engine.core.model import Model
from abc import abstractmethod

TABLE = "characters"
PK = "name"


class Character(Model):
    def __init__(
      self, name: str, race: str, class_name: str, inventory: dict):

        super().__init__(TABLE, PK)
        self.name = name
        self.race = race
        self.class_name = class_name
        self.inventory = inventory
