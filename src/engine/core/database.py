from tinydb import TinyDB, Query
from src.engine.core.config import config


class Database():
    def __init__(self):
        self.database = TinyDB(config.save)

    def search(self, table: str, field: str, search: str):
        query = Query()
        queryTable = self.database.table(table)

        return queryTable.search(query[field] == search)

    def save(self, table: str, obj: dict):
        queryTable = self.database.table(table)
        queryTable.insert(obj)

    def update(
      self, table: str, query_key: str, query_value: str, key: str, update):
        query = Query()
        queryTable = self.database.table(table)

        return queryTable.update(
            {key: update}, query[query_key] == query_value)
