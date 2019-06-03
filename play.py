''' play script '''
import sys
from src.game.build.buildall import BuildAll
from src.engine.base.characters.npc import NPC
from src.engine.base.characters.player import Player
from src.engine.core.database import Database
from src.engine.core.config import config


def main(arg):
    if arg == "build":
        print("Build Started")
        config.env = "DEFAULT"
        config.get_save_config()
        build = BuildAll()
        build.build()

    elif arg == "play":
        print("Play Script")
        config.env = "DEFAULT"
        config.get_save_config()
        # player = Player("Frodo", "Hobbit", "Fighter", {}, 1)
        # player.print()
        # player.save()
        player = Player()
        player.get("Frodo")
        player.print()

        # jon_snow = NPC()
        # jon_snow.get("Jon Snow")
        # jon_snow.print()
    elif arg == "test":
        config.env = "TEST"
        config.get_save_config()
        build = BuildAll()
        build.build()
    else:
        print("Command not recognized")


if __name__ == "__main__":
    main(sys.argv[1])
