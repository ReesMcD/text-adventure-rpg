from .buildingblocks.statblock import StatBlock
from .buildingblocks.statblock import Inventory


class Player():
    """
    The player character.
    """

    def __init__(self, name: str, level: int, race: str,
                 stats: StatBlock, inventory: Inventory):
        self.name = name
        self.level = level
        self.race = race
        self.stats = stats
        self.inventory = inventory
