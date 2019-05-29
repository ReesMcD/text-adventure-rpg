from .build import Build
from engine.base.classes.npcclass import NPCClass


class BuildClasses(Build):
    ''' Class that builds all classes in the game. '''

    def __init__(self):
        super().__init__("classes.json")

        item_data = self.importData()
        self.npc_classes = item_data["npc_classes"]

    def build(self):
        print("Building Classs...")

        print("Building NPC Classes...")
        npc_classes = self.npc_classes
        for key, value in npc_classes.items():
            print("Added {}".format(value["name"]))
            npc_classes = NPCClass(
                value["name"], value["class_type"], value["hit_points"], value["stats"],
                value["armor_class"], value["abilites"], value["actions"],
                value["challenge_rating"])

            npc_classes.save()
