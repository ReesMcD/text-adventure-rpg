from .build import Build


class BuildItems(Build):
    ''' Class that builds all items in the game. '''

    def __init__(self):
        super().__init__("items.json")
        itemData = self.importData()
        self.rarity = itemData["rarity"]

    def build(self):
        print(self.rarity)
