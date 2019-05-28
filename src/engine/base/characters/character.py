from engine.core.model import Model
from engine.base.classes.class import Class
from engine.base.inventory import Inventory
from abc import abstractmethod

TABLE = "characters"
PK = "name"


class Character(Model):
    def __init__(
      self, name: str, playerClass: Class, inventory: Inventory,
      maxHitPoints: number, currentHitPoints: number):

        super().__init__(TABLE, PK)
        self.name = name
        self.playerClass = playerClass
        self.inventory = inventory
        self.maxHitPoints = playerClass.hitPoints
        slef.currentHitPoints = self.maxHitPoints
