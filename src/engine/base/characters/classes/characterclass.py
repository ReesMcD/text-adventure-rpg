''' Abstract Character Player Class '''
from src.engine.core.model import Model
from abc import abstractmethod

TABLE = "classes"
PK = "name"


class CharacterClass(Model):
    '''
    Playable classes for PCs.

    Attributes:
        name: String of the name of the class
        class_type: String of the possible class types
        hitpoints: Integer of the classes base hitpoints
        stats: Dictionary that contains the classes stats
        armor_class: Integer that denotes the classes armor rating
        abilites: Dictionary of different class abilites
        aciton: Dictionary of different actions a player with
          this class can take
    '''

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
