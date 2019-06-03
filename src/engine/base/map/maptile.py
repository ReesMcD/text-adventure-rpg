''' Abstract Map Tile '''
from src.engine.core.model import Model

TABLE = "map"
PK = "id"


class MapTile(Model):
    '''
    Abstact class for a map tiles

    Attributes:
        id: Integers that identifies map itel
        x: x component of a point
        y: y component of a point
        desc: String of desctiption of the tile
        npc: dict of the npcs located on the map tile

    '''
    def __init__(
      self, table: str, id: str, x: int, y: int, desc: str, npcs: dict):
        super().__init__(table, PK)
