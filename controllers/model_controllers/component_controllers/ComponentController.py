from models.domains import Component
from ..ModelController import ModelController
from db.pull_from_db import get_distinct_column

class ComponentController(ModelController):
    def __init__(self, tables, special_attr, serializer) -> None:
        search_type = {
            "mnf_id": "search",
            "part_number": "search",
            "inventory_date": "range",
            "price": "range",
            "guarantee": "range",
            "sub_category": "val_list",
            "stock": "range",
        }
        search_type[special_attr[0]] = special_attr[1]        
        super().__init__(tables, "part_number", search_type, serializer)
        self._subcategories: list[str] = None

    def get_list(self) -> list[Component]:
        return super().get_list()

    def add(self, data: dict) -> Component:
        if self.item_exists(data["part_number"]) != None:
            raise Exception("Part number must be unique")
        
        new_component = Component(
            data["mnf_id"],
            float(data["price"]),
            data["inventory_date"],
            int(data["guarantee"]),
            data["part_number"],
            data["sub_category"],
            int(data["stock"])
        )
        return new_component
            
    def item_exists(self, key: str) -> Component:
        for component in self._list:
            if key == component.get_part_number():
                return component
        return None
    
    def update(self, data: dict[str, str], key: str) -> Component:
        component_to_update = self.item_exists(key)
        if component_to_update == None:
            raise Exception("Part not found")

        if "price" in data.keys() and data["price"] != "":
            component_to_update.set_price(float(data["price"]))
        if "inventory_date" in data.keys() and data["inventory_date"] != "":
            component_to_update.set_inventory_date(data["inventory_date"])
        if "guarantee" in data.keys() and data["guarantee"] != "":
            component_to_update.set_guarantee(int(data["guarantee"]))
        if "part_number" in data.keys() and data["part_number"] != "":
            component_to_update.set_part_number(data["part_number"])
        if "sub_category" in data.keys() and data["sub_category"] != "":
            component_to_update.set_sub_category(data["sub_category"])
        if "stock" in data.keys() and data["stock"] != "":
            component_to_update.set_stock(int(data["stock"]))
        if "image_path" in data.keys() and data["image_path"] != "":
            component_to_update.set_image_path(data["image_path"])

        return component_to_update

    def get_filtered_list(
            self, 
            filters: dict[str, str] = ..., 
            sort_options: dict[str, str] = ...
        ) -> list[Component]:
        return super().get_filtered_list(filters, sort_options)
    
    def get_subcategories(self) -> list[str]:
        if self._subcategories == None:
            self._subcategories = get_distinct_column(self._TABLE, "sub_category")
        
        return self._subcategories.copy()
