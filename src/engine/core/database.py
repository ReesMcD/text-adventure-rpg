from tinydb import TinyDB, Query


class Database():
    def __init__(self):
        self.database = TinyDB('db.json')

    def search(self, table: str, field: str, search: str):
        query = Query()
        queryTable = self.database.table(table)

        return queryTable.search(query[field] == search)

    def save(self, table: str, obj: dict):
        queryTable = self.database.table(table)
        queryTable.insert(obj)

    def update(self, table: str, queryKey: str, queryValue: str, key: str, update):
        query = Query()
        queryTable = self.database.table(table)

        return queryTable.update({key: update}, query[queryKey] == queryValue)
