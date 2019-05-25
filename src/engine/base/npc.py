from engine.core.model import Model
from engine.base.statblock import StatBlock
from engine.base.inventory import Inventory

TABLE = "npc"
PK = "name"


class NPC(Model):
    """
    An class for creating Non Playable Characters. Meant to be an abstract
    class but can also be used to create simple NPCs.
    """

    def __init__(self, name: str, race: str, stats: StatBlock, max_hp: int,
                 armor_class: int, speed: int, challenge_rating: int):
        super().__init__(TABLE, PK)
        self.name = name
        self.race = race
        self.stats = stats
        self.max_hp = max_hp
        self.challenge_rating = challenge_rating
        self.armor_class = armor_class
        self.speed = speed

        self.inventory = Inventory(stats.strength, [], name)
        self.current_hp = max_hp
        self.initiative = stats.dexterity

        # super().__init__(name, race, stats, max_hp, challenge_rating,
        #                  armor_class, speed, self.inventory, self.current_hp,
        #                  self.initiative)
        # TODO: Add Initative and actions

    def print(self):
        """Prints full character info, ie Name, Race, Stats, etc.  """
        print("------ {} ------".format(self.name))
        print("Race: {}".format(self.race))
        self.stats.print()
        print("Armor Class: {}".format(self.armor_class))
        print("HP: {}/{}".format(self.current_hp, self.max_hp))
        print("Speed: {}".format(self.speed))
        print("CR: {} \n".format(self.challenge_rating))
