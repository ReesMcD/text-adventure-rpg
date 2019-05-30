from engine.base.classes import CharacterClass

STAT_BLOCK = {
    "strength": 0,
    "dexterity": 0,
    "constitution": 0,
    "intelligence": 0,
    "wisdom": 0,
    "charisma": 0
}



class PlayerClass(CharacterClass):
    """
    Player Classes
    """

    def __init__(
      self, name="", class_type="", hitpoints=0, stats=STAT_BLOCK, armor_class=0,
      abilites={}, actions={}, hit_dice=0):

        super().__init__(
          name, class_type, hitpoints, stats, armor_class, abilites, actions)
        self.hit_dice = hit_dice

    def print(self):
        """Prints full character class info. """
        print("Class: {}".format(self.name))
        self.stats.print()
        print("Armor Class: {}".format(self.armor_class))
        # TODO: Abilites and Actions
