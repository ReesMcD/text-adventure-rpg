from engine.core.model import Model
from engine.items.item import Item


class Inventory(Model):
    """
    Class that acts as inventory for a Player, NPC, or even storage container.
    Contains items in inventory, carrying capacity of this inventory, and
    the functions that modify the list of items
    """

    def __init__(self, carry_cap: int, inventory: list, holder=None):
        self.carry_cap = carry_cap
        self.inventory = inventory
        self.holder = holder

    def print(self):
        """Prints contents of an inventory """
        print("------ {}'s Inventory ------".format(self.holder))
        for item in self.inventory:
            print(item)

    def addItem(self, item: Item):
        """Adds an item to an inventory """
        self.inventory.append(item)

    def removeItem(self, itemIndex: int):
        """Removes an item to an inventory """
        del self.inventory[itemIndex]
