from engine.base.classes import CharacterClass
from engine.base.statblock import StatBlock

TABLE = "npc_classes"
PK = "name"


class PlayerClass(CharacterClass):
    """
    Player Classes
    """

    def __init__(
      self, name="", classType="", hitPoints=0, stats={}, armorClass=0,
      abilites={}, actions={}, hitDice=0):

        super().__init__(
          name, classType, hitPoints, stats, armorClass, abilites, actions)
        self.hitDice = hitDice

    def print(self):
        """Prints full character class info. """
        print("Class: {}".format(self.name))
        self.stats.print()
        print("Armor Class: {}".format(self.armorClass))
        # TODO: Abilites and Actions
