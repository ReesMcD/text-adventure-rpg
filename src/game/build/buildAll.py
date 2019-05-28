from .items import BuildItems
import json


class BuildAll():
    ''' Builds all objects for the game. '''

    def __init__(self):
        print("Initializing Build...")
        self.buildItems = BuildItems()

    def build(self):
        print("Building...")

        self.__clearDatabase()
        self.buildItems.build()

        print("Build Complete")

    def __clearDatabase(self):
        with open("db.json", "w") as json_data:
            json.dump(None, json_data)
