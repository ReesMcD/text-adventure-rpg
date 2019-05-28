from engine.core.model import Model
from engine.base.classes.class import Class
from engine.base.inventory import Inventory
from abc import abstractmethod

TABLE = "classes"
PK = "name"


class CharacterClass(Model):
    ''' Abstract class for Character Classes'''

    def __init__(
      self, name: str, classType="", hitPoints=0, stats={},
      armorClass=0, abilites={}, actions={}):
        super().__init__(TABLE, PK)
        self.name = name
        self.hitPoints = hitPoints
        self.stats = stats
        self.armorClass = armorClass
        self.abilites = abilites
        self.actions = actions
        self.initiative = stats.dexterity
