''' Non Playable Character Class '''
from src.engine.base.characters.character import Character
from src.engine.base.classes.npcclass import NPCClass
from src.engine.core.database import Database

TABLE = "npc"


class NPC(Character):
    '''
    NPC or Non Playable Character is a character within the game that a player
    can interact with

    Attributes:
        name: String of the name of the character
        race: String of the race of the character
        class_name: String of the characters given player class
        inventory: Dictionary of a characters inventory
        dialoge: String that acts as a key for this characters dialog

    '''
    def __init__(
      self, name="", race="", class_name="", inventory={}, dialoge=""):

        super().__init__(TABLE, name, race, class_name, inventory)
        self.dialoge = dialoge
        self.max_hitpoints = 0
        self.current_hitpoints = 0
        self.armor_class = 0
        self.stats = {}
        self.actions = {}
        self.abilites = {}
        self.challenge_rating = 0

        if class_name:
            self.__set_player_class(class_name)

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
        database = Database()
        result = database.search(self.table, self.pk, query)
        try:
            npc = result[0]
        except IndexError:
            print("\n ERROR - Object Not Found \n")

        self.name = npc["name"]
        self.race = npc["race"]
        self.class_name = npc["class_name"]
        self.inventory = npc["inventory"]
        self.dialoge = npc["dialoge"]
        self.max_hitpoints = npc["max_hitpoints"]
        self.current_hitpoints = npc["current_hitpoints"]
        self.armor_class = npc["armor_class"]
        self.stats = npc["stats"]
        self.actions = npc["actions"]
        self.abilites = npc["abilites"]
        self.challenge_rating = npc["challenge_rating"]

    def __set_player_class(self, class_name):
        player_class = NPCClass().get(class_name)
        self.max_hitpoints = player_class.hitpoints
        self.current_hitpoints = self.max_hitpoints
        self.armor_class = player_class.armor_class
        self.stats = player_class.stats
        self.actions = player_class.actions
        self.abilites = player_class.abilites
        self.challenge_rating = player_class.challenge_rating
