from .ComponentSerializer import ComponentSerializer
from ...domains import Inductor
from .component_configs import COMPONENT_COLUMNS_INDEX

class InductorSerializer(ComponentSerializer):
    def __init__(self) -> None:
        super().__init__()

    def load(self, query_result: list[str]) -> Inductor:
        inductance = float(query_result[COMPONENT_COLUMNS_INDEX["special_attr"]])
        base_component = super().load(query_result)
        return Inductor(
            base_component.get_mnf_id(),
            base_component.get_price(),
            base_component.get_inventory_date(),
            base_component.get_guarantee(),
            base_component.get_part_number(),
            base_component.get_sub_category(),
            base_component.get_stock(),
            inductance,
            base_component.get_image_path()
        )
    
    def load_many(self, query_results: list[list[str]]) -> list[Inductor]:
        return super().load_many(query_results)
    
    def dump(self, obj: Inductor) -> list[str]:
        data = super().dump(obj)
        data.append(obj.get_inductance())
        return data