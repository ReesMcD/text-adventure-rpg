from game.build.buildAll import BuildAll
from engine.base.items.weapon import Weapon
import sys


def main(arg):
    print(arg)
    if arg == "build":
        print("Build Started")
        build = BuildAll()
        build.build()
    elif arg == "play":
        print("Play Script")
        # Get Item
        item = Weapon().get("Longsword")
        item.print()
        #
        # # Update Item
        item.update("Longsword", "value", 5)
        item.print()
    else:
        print("Command not recognized")


if __name__ == "__main__":
    main(sys.argv[1])
