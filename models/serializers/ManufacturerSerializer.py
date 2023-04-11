from .Serializer import Serializer
from ..domains import Manufacturer
from .constants import MANUFACTURER_COULUMNS_INDEX

class ManufacturerSerializer(Serializer):
    def __init__(self) -> None:
        super().__init__()

    def load(self, query_result: list[str]) -> Manufacturer:
        name = query_result[MANUFACTURER_COULUMNS_INDEX["name"]]
        id = query_result[MANUFACTURER_COULUMNS_INDEX["id"]]
        country = query_result[MANUFACTURER_COULUMNS_INDEX["country"]]
        image_path = query_result[MANUFACTURER_COULUMNS_INDEX["image_path"]]
        return Manufacturer(
            id,
            name,
            country,
            image_path
        )
    
    def load_many(self, query_results: list[list[str]]) -> list[Manufacturer]:
        return super().load_many(query_results)
    
    def dump(self, obj: Manufacturer) -> list[str]:
        data = [
            obj.get_id(),
            obj.get_name(),
            obj.get_country(),
            obj.get_image_path()
        ]
        return data