from .item import Item


class Weapon(Item):
    ''' Weapons that will be used by playable characters and npcs'''

    def __init__(self, name="", type="", value=0, rarity="", weight=0, desc="",
        damage=0, weapon_type="", weapon_range=0):

        super().__init__(name, type, value, rarity, weight, desc)
        self.damage = damage
        self.weapon_type = weapon_type
        self.weapon_range = weapon_range

    def print(self):
        print()
        print("------ {} ------".format(self.name))
        print("Type: {}".format(self.type))
        print("Value: {}".format(self.value))
        print("Rarity: {}".format(self.rarity))
        print("Weight: {}".format(self.weight))
        print("Weapon Type: {}".format(self.weapon_type))
        print("Damage: 1d{}".format(self.damage))
        print("Range: {}".format(self.weapon_range))
        print("Description: {}".format(self.desc))
        print()
