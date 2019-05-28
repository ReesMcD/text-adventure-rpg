from engine.base.characters import Character
from engine.base.classes import CharacterClass
from engine.base.statblock import StatBlock
from engine.base.inventory import Inventory

class NPC(Character):
    """
    An non playable character that could be encountered within the game
    """

    def __init__(
      self, name="", playerClass={}, inventory={}, maxHitPoints=0, currentHitPoints=0, ):

        super().__init__(
          self, name, playerClass, inventory, maxHitPoints, currentHitPoints)
