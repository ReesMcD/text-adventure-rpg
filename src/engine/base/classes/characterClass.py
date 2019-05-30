from engine.core.model import Model
from abc import abstractmethod

TABLE = "classes"
PK = "name"


class CharacterClass(Model):
    ''' Abstract class for Character Classes'''

    def __init__(
      self, name: str, class_type: str, hitpoints: int, stats: dict,
      armor_class: int, abilites: dict, actions: dict):
        super().__init__(TABLE, PK)
        self.name = name
        self.class_type = class_type
        self.hitpoints = hitpoints
        self.stats = stats
        self.armor_class = armor_class
        self.abilites = abilites
        self.actions = actions
