from .build import Build
from src.engine.base.characters.npc import NPC


class BuildNPCs(Build):
    ''' Creates and save all npcs in the game to database file '''

    def __init__(self):
        super().__init__("npcs.json")
        npc_data = self.importData()
        self.npc = npc_data["npc"]

    def build(self):
        print("Building NPCs...")
        npc = self.npc
        for key, value in npc.items():
            print("Added {}".format(value["name"]))

            npc = NPC(
                value["name"], value["race"], value["class_name"],
                value["inventory"], value["dialoge"])

        npc.save()
