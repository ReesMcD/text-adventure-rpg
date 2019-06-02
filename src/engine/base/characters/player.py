''' '''
from engine.base.characters.character import Character
from engine.base.classes.playerclass import PlayerClass
from engine.core.database import Database

class Player(Character):
    """
    An playable character 
    """

    def __init__(
      self, name="", race="", class_name="", inventory={}, level=1):

        super().__init__(name, race, class_name, inventory)
        self.level = level
        
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

    def __setPlayerClass(self, class_name):
        player_class = PlayerClass().get(class_name)
        self.max_hitpoints = player_class.hitpoints
        self.current_hitpoints = self.max_hitpoints
        self.armor_class = player_class.armor_class
        self.stats = player_class.stats
        self.actions = player_class.actions
        self.abilites = player_class.abilites
        self.hit_dice = player_class.hit_dice