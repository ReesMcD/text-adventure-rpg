from engine.core.model import Model

TABLE = "item"
PK = "name"


class Item(Model):
    """Class used for simple items."""

    def __init__(self, name="", type="", value=0, rarity="", weight=0, desc=""):
        super().__init__(TABLE, PK)
        self.name = name
        self.type = type
        self.value = value
        self.rarity = rarity
        self.weight = weight
        self.desc = desc

    def print(self):
        print()
        print("------ {} ------".format(self.name))
        print("Type: {}".format(self.type))
        print("Value: {}".format(self.value))
        print("Rarity: {}".format(self.rarity))
        print("Weight: {}".format(self.weight))
        print("Description: {}".format(self.desc))
        print()
