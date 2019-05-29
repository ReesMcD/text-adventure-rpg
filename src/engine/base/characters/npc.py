from engine.base.characters import Character
from engine.base.classes import CharacterClass
from engine.base.placeholders.placeholder import npcClass, inventory


class NPC(Character):
    """
    An non playable character that could be encountered within the game
    """

    def __init__(
      self, name="", playerClass=npcClass, inventory=inventory, maxHitPoints=0,
      currentHitPoints=0, dialoge={}):

        super().__init__(
          self, name, playerClass, inventory, maxHitPoints, currentHitPoints)
        self.dialoge = dialoge
