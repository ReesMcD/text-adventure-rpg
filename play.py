''' play script '''
import sys
from src.game.build.buildall import BuildAll
from src.engine.base.characters.npc import NPC
from src.engine.base.characters.player import Player


def main(arg):
    if arg == "build":
        print("Build Started")
        build = BuildAll()
        build.build()

    elif arg == "play":
        print("Play Script")

        player = Player("Frodo", "Hobbit", "Fighter", {}, 1)
        player.print()
        player.save()
        player = Player()
        player.get("Frodo")
        player.print()

        # jon_snow = NPC()
        # jon_snow.get("Jon Snow")
        # jon_snow.print()

    else:
        print("Command not recognized")


if __name__ == "__main__":
    main(sys.argv[1])
