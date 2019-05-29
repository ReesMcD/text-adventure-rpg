from engine.base.classes.characterClass import CharacterClass
from engine.base.statblock import StatBlock
from engine.base.inventory import Inventory
from engine.base.placeholders.placeholder import statBlock


class NPCClass(CharacterClass):
    """
    For creating the assortment of classes for NPCs
    """

    def __init__(
      self, name="", classType="", hitPoints=0, stats=statblock, armorClass=0,
      abilites={}, actions={}, challengeRating=0):

        super().__init__(
          name, classType, hitPoints, stats, armorClass, abilites, actions)
        self.challengeRating = challengeRating

    def print(self):
        """Prints full character info, ie Name, Race, Stats, etc.  """
        print("Class: {}".format(self.name))
        self.stats.print()
        print("Armor Class: {}".format(self.armorClass))
        print("CR: {}".format(self.challengeRating))
        # TODO: Abilites and Actions
