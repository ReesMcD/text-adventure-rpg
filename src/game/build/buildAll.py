from .items import BuildItems
from .classes import BuildClasses
from .npcs import BuildNPCs
import json


class BuildAll():
    ''' Builds all objects for the game. '''

    def __init__(self):
        print("Initializing Build...")
        self.__clearDatabase()
        self.build_items = BuildItems()
        self.build_classes = BuildClasses()
        self.build_npc = BuildNPCs()

    def build(self):
        print("Building...")

        self.build_items.build()
        self.build_classes.build()
        self.build_npc.build()

        print("Build Complete")

    def __clearDatabase(self):
        with open("db.json", "w") as json_data:
            json.dump(None, json_data)
