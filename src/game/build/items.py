from .build import Build
from engine.base.items.item import Item
from engine.base.items.weapon import Weapon


class BuildItems(Build):
    ''' Class that builds all items in the game. '''

    def __init__(self):
        super().__init__("items.json")

        itemData = self.importData()
        self.weapons = itemData["weapons"]

    def build(self):
        print("Building Items...")

        print("Building Weapons...")
        weapons = self.weapons
        for key, value in weapons.items():
            print("Added {}".format(value["name"]))
            weapon = Weapon(
                value["name"], value["type"], value["value"], value["rarity"],
                value["weight"], value["desc"], value["damage"], value["weapon_type"],
                value["weapon_range"])

            weapon.save()
