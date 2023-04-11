class Serializer:
    """Base serializer class"""
    def __init__(self) -> None:
        pass

    def load(self, query_result: list[str]) -> object:
        pass

    def load_many(self, query_results: list[list[str]]) -> list[object]:
        objs_list: list[object] = []
        for result in query_results:
            objs_list.append(self.load(result))
        
        return objs_list

    def dump(self, obj: object) -> list[str]:
        pass

    def dump_many(self, objs: list[object]) -> list[list[str]]:
        data: list[list[str]] = []
        for obj in objs:
            data.append(self.dump(obj))
        
        return data
    