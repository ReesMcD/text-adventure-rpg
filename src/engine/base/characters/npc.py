''' '''
from engine.base.characters.character import Character
from engine.base.classes.npcclass import NPCClass


class NPC(Character):
    """
    An non playable character that could be encountered within the game
    """

    def __init__(
      self, name="", race="", className="", inventory={}, dialoge={}):

        super().__init__(name, race, className, inventory)
        self.dialoge = dialoge

        playerClass = NPCClass().get(className)
        self.max_hitpoints = playerClass.hit_points
        self.current_hitpoints = self.max_hitpoints
        self.armor_class = playerClass.armor_class
        self.stats = playerClass.stats
        self.actions = playerClass.actions
        self.abilites = playerClass.abilites
        self.challenge_rating = playerClass.challenge_rating

    def print(self):
        print()
        print("------ {} ------".format(self.name))
        print("Race: {}".format(self.race))
        print("HP: {}/{}".format(self.current_hitpoints, self.max_hitpoints))
        print("Armor Class: {}".format(self.armor_class))
        print("Stats: ")
        for key, value in self.stats.items():
            print(" {}:{}".format(key, value))
        print("CR: {}".format(self.challenge_rating))
        print("Actions: {}".format(self.actions))
