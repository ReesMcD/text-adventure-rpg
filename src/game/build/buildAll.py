from .items import BuildItems
from .classes import BuildClasses
import json


class BuildAll():
    ''' Builds all objects for the game. '''

    def __init__(self):
        print("Initializing Build...")
        self.__clearDatabase()
        self.buildItems = BuildItems()
        self.buildClasses = BuildClasses()

    def build(self):
        print("Building...")

        self.__clearDatabase()
        self.buildItems.build()
        self.buildClasses.build()

        print("Build Complete")

    def __clearDatabase(self):
        with open("db.json", "w") as json_data:
            json.dump(None, json_data)
