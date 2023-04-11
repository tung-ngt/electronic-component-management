from .ComponentSerializer import ComponentSerializer
from ...domains import Sensor
from .component_configs import COMPONENT_COLUMNS_INDEX

class SensorSerializer(ComponentSerializer):
    def __init__(self) -> None:
        super().__init__()

    def load(self, query_result: list[str]) -> Sensor:
        sensor_type = query_result[COMPONENT_COLUMNS_INDEX["special_attr"]]
        base_component = super().load(query_result)
        return Sensor(
            base_component.get_mnf_id(),
            base_component.get_price(),
            base_component.get_inventory_date(),
            base_component.get_guarantee(),
            base_component.get_part_number(),
            base_component.get_sub_category(),
            base_component.get_stock(),
            sensor_type,
            base_component.get_image_path()
        )
    
    def load_many(self, query_results: list[list[str]]) -> list[Sensor]:
        return super().load_many(query_results)
    
    def dump(self, obj: Sensor) -> list[str]:
        data = super().dump(obj)
        data.append(obj.get_sensor_type())
        return data