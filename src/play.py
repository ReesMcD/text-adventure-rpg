''' play script '''
import sys
from game.build.buildall import BuildAll
from engine.base.characters.npc import NPC


def main(arg):
    if arg == "build":
        print("Build Started")
        build = BuildAll()
        build.build()

    elif arg == "play":
        print("Play Script")

        npc = NPC(
            "Jon Snow", "Human", "Commoner", {"item": (1, "Shortsword")},
            {"inital": "Hello World"})

        npc.print()
        npc.save()

    else:
        print("Command not recognized")


if __name__ == "__main__":
    main(sys.argv[1])
