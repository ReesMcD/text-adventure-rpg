''' Playable Character Class '''
from src.engine.base.characters.character import Character
from src.engine.base.classes.playerclass import PlayerClass
from src.engine.core.database import Database


class Player(Character):
    '''
    NPC or Non Playable Character is a character within the game that a player
    can interact with

    Attributes:
        name: String of the name of the character
        race: String of the race of the character
        class_name: String of the characters given player class
        inventory: Dictionary of a characters inventory
        level: Integer that denotes a character's level

    '''
    def __init__(
      self, name="", race="", class_name="", inventory=None, level=1):

        super().__init__(name, race, class_name, inventory)
        self.level = level
        self.max_hitpoints = 0
        self.current_hitpoints = 0
        self.armor_class = 0
        self.stats = {}
        self.actions = {}
        self.abilites = {}
        self.hit_dice = 0

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
        print("Actions: {}".format(self.actions))

    def get(self, query):
        db = Database()
        result = db.search(self.table, self.pk, query)
        try:
            player = result[0]
        except IndexError:
            print("\n ERROR - Object Not Found \n")

        self.name = player["name"]
        self.race = player["race"]
        self.class_name = player["class_name"]
        self.inventory = player["inventory"]
        self.level = player["level"]
        self.max_hitpoints = player["max_hitpoints"]
        self.current_hitpoints = player["current_hitpoints"]
        self.armor_class = player["armor_class"]
        self.stats = player["stats"]
        self.actions = player["actions"]
        self.abilites = player["abilites"]
        self.hit_dice = player["hit_dice"]

    def __set_player_class(self, class_name):
        player_class = PlayerClass().get(class_name)
        self.max_hitpoints = player_class.hitpoints
        self.current_hitpoints = self.max_hitpoints
        self.armor_class = player_class.armor_class
        self.stats = player_class.stats
        self.actions = player_class.actions
        self.abilites = player_class.abilites
        self.hit_dice = player_class.hit_dice
