from .ComponentController import ComponentController
from models.domains import Sensor
from models.serializers.component_serializers import SensorSerializer

class SensorController(ComponentController):
    def __init__(self) -> None:
        super().__init__(
            "sensor",
            ["sensor_type", "val_list"],
            SensorSerializer()
        )

    def get_list(self) -> list[Sensor]:
        return super().get_list()
    
    def add(self, data: dict) -> Sensor:
        new_component = super().add(data)
        new_sensor = Sensor(
            new_component.get_mnf_id(),
            new_component.get_price(),
            new_component.get_inventory_date(),
            new_component.get_guarantee(),
            new_component.get_part_number(),
            new_component.get_sub_category(),
            new_component.get_stock(),
            data["sensor_type"]
        )
        self.add_to_list(new_sensor)
        self.create_db_row(new_sensor)
        return new_component
    
    def update(self, data: dict[str, str], key: str) -> Sensor:
        component_to_update: Sensor = super().update(data, key)

        if "sensor_type" in data.keys() and data["sensor_type"]:
            component_to_update.set_sensor_type(data["sensor_type"])

        self.update_db_row(data, key)
        return component_to_update

    def get_filtered_list(
            self, 
            filters: dict[str, str] = ..., 
            sort_options: dict[str, str] = ...
        ) -> list[Sensor]:
        return super().get_filtered_list(filters, sort_options)