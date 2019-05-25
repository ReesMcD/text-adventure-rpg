from game.build.items import BuildItems
import os

def main():
    build = BuildItems()
    build.build()
    # # # Get Item
    # item = Item().get("Iron Sword")
    # item.print()
    # #
    # # # Update Item
    # item.update("Iron Sword", "value", 5)
    # item.print()


if __name__ == "__main__":
    main()
