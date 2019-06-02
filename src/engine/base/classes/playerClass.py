''' Player Playable Class '''
from src.engine.base.classes.characterclass import CharacterClass

STAT_BLOCK = {
    "strength": 0,
    "dexterity": 0,
    "constitution": 0,
    "intelligence": 0,
    "wisdom": 0,
    "charisma": 0
}


class PlayerClass(CharacterClass):
    '''
    Abstract class for players classes type.

    Attributes:
        name: String of the name of the class
        class_type: String of the possible class types
        hitpoints: Integer of the classes base hitpoints
        stats: Dictionary that contains the classes stats
        armor_class: Integer that denotes the classes armor rating
        abilites: Dictionary of different class abilites
        aciton: Dictionary of different actions a player with
          this class can take
        challenge_rating: Integer that denotes how difficult an NPC is
    '''

    def __init__(
      self, name="", class_type="", hitpoints=0, stats=STAT_BLOCK,
            armor_class=0, abilites={}, actions={}, hit_dice=0):

        super().__init__(
          name, class_type, hitpoints, stats, armor_class, abilites, actions)
        self.hit_dice = hit_dice

    def print(self):
        """Prints full character class info. """
        print("Class: {}".format(self.name))
        self.stats.print()
        print("Armor Class: {}".format(self.armor_class))
        # TODO: Abilites and Actions
