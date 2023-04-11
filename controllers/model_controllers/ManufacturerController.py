from .ModelController import ModelController
from models.domains import Manufacturer
from models.serializers import ManufacturerSerializer

class ManufacturerController(ModelController):
    def __init__(self) -> None:
        super().__init__(
            "manufacturer",
            "id",
            {
                "id": "search",
                "name": "search",
                "country": "val_list"
            },
            ManufacturerSerializer()
        )

    def get_list(self) -> list[Manufacturer]:
        return super().get_list()

    def add(self, data: dict) -> Manufacturer:
        if self.item_exists(data["id"]) != None:
            raise Exception("Manufacturer's id must be unique")
        
        new_manufacturer = Manufacturer(
            data["id"],
            data["name"],
            data["country"],
        )
        self.add_to_list(new_manufacturer)
        self.create_db_row(new_manufacturer)
        return new_manufacturer
    
    def item_exists(self, key: str) -> Manufacturer:
        for manufacturer in self._list:
            if key == manufacturer.get_id():
                return manufacturer
        return None
    
    def update(self, data: dict, key: str) -> Manufacturer:
        manufacturer_to_update = self.item_exists(key)
        if manufacturer_to_update == None:
            raise Exception("Manufacturer's id not found")
        
        if "name" in data.keys() and data["name"] != "":
            manufacturer_to_update.set_name(data["name"])
        if "country" in data.keys() and data["country"] != "":
            manufacturer_to_update.set_country(data["country"])

        self.update_db_row(data, key)
        return manufacturer_to_update

    def get_filtered_list(
            self,
            filters: dict[str, str] = ..., 
            sort_options: dict[str, str] = ...
        ) -> list[Manufacturer]:
        return super().get_filtered_list(filters, sort_options)