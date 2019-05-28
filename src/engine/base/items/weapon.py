from .item import Item


class Weapon(Item):
    ''' Weapons that will be used by playable characters and npcs'''

    def __init__(self, name="", type="", value=0, rarity="", weight=0, desc="",
        damage=0, weaponType="", weaponRange=0):

        super().__init__(name, type, value, rarity, weight, desc)
        self.damage = damage
        self.weaponType = weaponType
        self.weaponRange = weaponRange

    def print(self):
        print()
        print("------ {} ------".format(self.name))
        print("Type: {}".format(self.type))
        print("Value: {}".format(self.value))
        print("Rarity: {}".format(self.rarity))
        print("Weight: {}".format(self.weight))
        print("Weapon Type: {}".format(self.weaponType))
        print("Damage: 1d{}".format(self.damage))
        print("Range: {}".format(self.weaponRange))
        print("Description: {}".format(self.desc))
        print()
