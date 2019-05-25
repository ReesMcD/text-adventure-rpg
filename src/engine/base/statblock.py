from engine.core.model import Model


class StatBlock(Model):
    """
    Class that contains the base seven stats meant for
    calculations for different actions.
    """

    def __init__(self, strength: int, dexterity: int, constitution: int,
                 intelligence: int, wisdom: int, charisma: int):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    def print(self):
        """Prints stat block """
        print("STR: {}, DEX: {}, CON: {}, INT: {}, WIS: {}, CHA: {}".format(
            self.strength, self.dexterity, self.constitution,
            self.intelligence, self.wisdom, self.charisma))
