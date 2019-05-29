from engine.base.classes.characterclass import CharacterClass

STAT_BLOCK = {
    "strength": 0,
    "dexterity": 0,
    "constitution": 0,
    "intelligence": 0,
    "wisdom": 0,
    "charisma": 0
}


class NPCClass(CharacterClass):
    """
    For creating the assortment of classes for NPCs
    """

    def __init__(
        self, name="", class_type="", hit_points=0, stats=STAT_BLOCK, armor_class=0,
        abilites={}, actions={}, challenge_rating=0):

        super().__init__(
            name, class_type, hit_points, stats, armor_class, abilites, actions)
        self.challenge_rating = challenge_rating

    def print(self):
        """Prints full character info, ie Name, Race, Stats, etc.  """
        print("Class: {}".format(self.name))
        print("Armor Class: {}".format(self.armor_class))
        print("CR: {}".format(self.challenge_rating))
       # TODO: Abilites and Actions
