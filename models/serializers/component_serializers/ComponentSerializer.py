from .component_configs import COMPONENT_COLUMNS_INDEX
from ...domains import Component
from ..Serializer import Serializer

class ComponentSerializer(Serializer):
    def __init__(self) -> None:
        super().__init__()

    def load(self, query_result: list[str]) -> Component:
        part_number = query_result[COMPONENT_COLUMNS_INDEX["part_number"]]
        mnf_id = query_result[COMPONENT_COLUMNS_INDEX["mnf_id"]]
        price = float(query_result[COMPONENT_COLUMNS_INDEX["price"]])
        inventory_date = query_result[COMPONENT_COLUMNS_INDEX["inventory_date"]]
        guarantee = int(query_result[COMPONENT_COLUMNS_INDEX["guarantee"]])
        sub_category = query_result[COMPONENT_COLUMNS_INDEX["sub_category"]]
        stock = int(query_result[COMPONENT_COLUMNS_INDEX["stock"]])
        image_path = query_result[COMPONENT_COLUMNS_INDEX["image_path"]]

        return Component(
            mnf_id,
            price,
            inventory_date,
            guarantee,
            part_number,
            sub_category,
            stock,
            image_path
        )

    def load_many(self, query_results: list[list[str]]) -> list[Component]:
        return super().load_many(query_results)
    
    def dump(self, obj: Component) -> list[str]:
        data = [
            obj.get_part_number(),
            obj.get_mnf_id(),
            obj.get_price(),
            obj.get_inventory_date(),
            obj.get_guarantee(),
            obj.get_sub_category(),
            obj.get_stock(),
            obj.get_image_path(),
        ]
        return data
    