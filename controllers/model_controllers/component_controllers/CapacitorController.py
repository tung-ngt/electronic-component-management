from .ComponentController import ComponentController
from models.domains import Capacitor
from models.serializers.component_serializers import CapacitorSerializer

class CapacitorController(ComponentController):
    def __init__(self) -> None:
        super().__init__(
            "capacitor",
            ["capacitance", "range"],
            CapacitorSerializer()
        )

    def get_list(self) -> list[Capacitor]:
        return super().get_list()
    
    def add(self, data: dict) -> Capacitor:
        new_component = super().add(data)
        new_capacitor = Capacitor(
            new_component.get_mnf_id(),
            new_component.get_price(),
            new_component.get_inventory_date(),
            new_component.get_guarantee(),
            new_component.get_part_number(),
            new_component.get_sub_category(),
            new_component.get_stock(),
            float(data["capacitance"])
        )
        self.add_to_list(new_capacitor)
        self.create_db_row(new_capacitor)
        return new_capacitor

    def update(self, data: dict[str, str], key: str) -> Capacitor:
        component_to_update: Capacitor = super().update(data, key)

        if "capacitance" in data.keys() and data["capacitance"]:
            component_to_update.set_capacitance(float(data["capacitance"]))

        self.update_db_row(data, key)
        return component_to_update

    def get_filtered_list(self,
            filters: dict[str, str] = ..., 
            sort_options: dict[str, str] = ...
        ) -> list[Capacitor]:
        return super().get_filtered_list(filters, sort_options)
