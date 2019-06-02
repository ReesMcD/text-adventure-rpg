from .build import Build
from src.engine.base.classes.npcclass import NPCClass
from src.engine.base.classes.playerclass import PlayerClass


class BuildClasses(Build):
    ''' Class that builds all classes in the game. '''

    def __init__(self):
        super().__init__("classes.json")

        item_data = self.importData()
        self.npc_classes = item_data["npc_classes"]
        self.player_classes = item_data["pc_classes"]

    def build(self):
        print("Building Classs...")
        self.__buildPlayerClasses()
        self.__buildNPCClasses()

    def __buildNPCClasses(self):
        print("Building NPC Classes...")
        npc_classes = self.npc_classes
        for key, value in npc_classes.items():
            print("Added {}".format(value["name"]))
            npc_class = NPCClass(
                value["name"], value["class_type"], value["hitpoints"],
                value["stats"], value["armor_class"], value["abilites"],
                value["actions"], value["challenge_rating"])

            npc_class.save()

    def __buildPlayerClasses(self):
        print("Building Player Classes...")
        player_classes = self.player_classes
        for key, value in player_classes.items():
            print("Added {}".format(value["name"]))
            player_class = PlayerClass(
                value["name"], value["class_type"], value["hitpoints"],
                value["stats"], value["armor_class"], value["abilites"],
                value["actions"], value["hit_dice"])

            player_class.save()
