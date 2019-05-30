from .database import Database
from abc import ABC, abstractmethod


class Model(ABC):
    '''
    The abstract class used for creating different objects within the game.
    Players, NPCs, Weapons, etc. can be all based off of the Model Class
    '''

    def __init__(self, table: str, pk: str):
        self.table = table
        self.pk = pk

    @abstractmethod
    def print(self):
        ''' Prints all params within this object '''
        pass

    def save(self):
        ''' Saves object in the game database in a given table '''
        db = Database()
        db.save(self.table, vars(self))

    def get(self, query: str):
        '''
        Searches database for given query,
        where the query should be classes primary key.

        Sets objects attributes.
        '''

        try:
            db = Database()
            result = db.search(self.table, self.pk, query)
            self.__dictToObj(result[0])
        except IndexError:
            print("\n ERROR - Object Not Found \n")

        return self

    def update(self, query_value: str, key: str, update):
        '''
        Updates a field in an object in a given object.
        '''
        db = Database()
        update = db.update(self.table, self.pk, query_value, key, update)
        self.get(self.name)

    def __dictToObj(self, dict: dict):
        for key, value in dict.items():
            setattr(self, key, value)
