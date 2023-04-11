from db.utils import create_query
from db.pull_from_db import get_rows
from db.push_to_db import update_row, create_row
from models.serializers.Serializer import Serializer

class ModelController:
    def __init__(self, table, key, search_type, serializer) -> None:
        self._list: list[object] = []
        self._TABLE = table
        self._KEY = key
        self._SEARCH_TYPES = search_type
        self.serializer: Serializer = serializer

    def get_list(self) -> list[object]:
        return self._list.copy()
    
    def load_data_from_db(self):
        query_results = get_rows(self._TABLE)
        self._list = self.serializer.load_many(query_results)

    def add(self, data: dict) -> object:
        pass

    def add_to_list(self, obj: object):
        self._list.append(obj)

    def create_db_row(self, obj: object):
        values = self.serializer.dump(obj)
        create_row(self._TABLE, values)

    def update(self, data: dict, key: str) -> object:
        pass

    def update_db_row(self, data: dict[str, str], key: str):
        update_row(self._TABLE, data, (self._KEY, key))

    def item_exists(self, key: str) -> object:
        pass

    def get_filtered_list(self, 
            filters: dict[str, str] = {},
            sort_options: dict[str, str] = {}
        ) -> list[object]:
        query_conditions = self.resolve_filters(filters)
        query_results = get_rows(self._TABLE, query_conditions, sort_options)
        return self.serializer.load_many(query_results)

    def resolve_filters(self, filters: dict[str, str]) -> list[str]:
        query_conditions = []
        for column, value in list(filters.items()):
            search_type = self._SEARCH_TYPES[column]
            if search_type == "search" and value != "":
                query_conditions.append(create_query.like(column, value))

            if search_type == "range":
                if "from" in value.keys() and value["from"] !=  "":
                    query_conditions.append(create_query.start_from(column, value["from"]))
                if "to" in value.keys() and value["to"] != "":
                    query_conditions.append(create_query.upto(column, value["to"]))
            
            if search_type == "val_list" and len(value) > 0:
                query_conditions.append(create_query.contains(column, value))

        return query_conditions