''' play script '''
import sys
from src.game.build.buildall import BuildAll
from src.engine.base.characters.npc import NPC


def main(arg):
    if arg == "build":
        print("Build Started")
        build = BuildAll()
        build.build()

    elif arg == "play":
        print("Play Script")

        jon_snow = NPC()
        jon_snow.get("Jon Snow")
        jon_snow.print()

    else:
        print("Command not recognized")


if __name__ == "__main__":
    main(sys.argv[1])
