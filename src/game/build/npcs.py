from .build import Build


class BuildNPCs(Build):
    ''' Creates and save all npcs in the game to database file '''

    def __init__(self):
        super().__init__("npcs.json")
        npcData = self.importData()

    def build(self):
        pass
