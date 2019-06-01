''' '''
from engine.base.characters.character import Character
from engine.base.classes.npcclass import NPCClass
from engine.core.database import Database

class NPC(Character):
    """
    An non playable character that could be encountered within the game
    """

    def __init__(
      self, name="", race="", class_name="", inventory={}, dialoge=""):

        super().__init__(name, race, class_name, inventory)
        self.dialoge = dialoge

        if class_name: 
            self.__setPlayerClass(class_name)

    def print(self):
        print()
        print("------ {} ------".format(self.name))
        print("Race: {}".format(self.race))
        print("Class: {}".format(self.class_name))
        print("HP: {}/{}".format(self.current_hitpoints, self.max_hitpoints))
        print("Armor Class: {}".format(self.armor_class))
        print("Stats: ")
        for key, value in self.stats.items():
            print(" {}:{}".format(key, value))
        print("CR: {}".format(self.challenge_rating))
        print("Actions: {}".format(self.actions))
    
    def get(self, query):
        db = Database()
        result = db.search(self.table, self.pk, query)
        try:
            npc = result[0]
        except IndexError:
            print("\n ERROR - Object Not Found \n")

        self.name = npc["name"]
        self.race = npc["race"]
        self.class_name = npc["class_name"]
        self.inventory = npc["inventory"]
        self.dialoge = npc["dialoge"]

        self.__setPlayerClass(self.class_name)

    def __setPlayerClass(self, class_name):
        player_class = NPCClass().get(class_name)
        self.max_hitpoints = player_class.hitpoints
        self.current_hitpoints = self.max_hitpoints
        self.armor_class = player_class.armor_class
        self.stats = player_class.stats
        self.actions = player_class.actions
        self.abilites = player_class.abilites
        self.challenge_rating = player_class.challenge_rating