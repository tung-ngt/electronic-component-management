from .ComponentController import ComponentController
from models.domains import Resistor
from models.serializers.component_serializers import ResistorSerializer

class ResistorController(ComponentController):
    def __init__(self) -> None:
        super().__init__(
            "resistor",
            ["resistance", "range"],
            ResistorSerializer()                
        )

    def get_list(self) -> list[Resistor]:
        return super().get_list()
        
    def add(self, data: dict) -> Resistor:
        new_component = super().add(data)
        new_resistor = Resistor(
            new_component.get_mnf_id(),
            new_component.get_price(),
            new_component.get_inventory_date(),
            new_component.get_guarantee(),
            new_component.get_part_number(),
            new_component.get_sub_category(),
            new_component.get_stock(),
            float(data["resistance"])
        )
        self.add_to_list(new_resistor)
        self.create_db_row(new_resistor)
        return new_resistor
    
    def update(self, data: dict[str, str], key: str) -> Resistor:
        component_to_update: Resistor = super().update(data, key)

        if "resistance" in data.keys() and data["resistance"]:
            component_to_update.set_resistance(float(data["resistance"]))

        self.update_db_row(data, key)
        return component_to_update

    def get_filtered_list(
            self, 
            filters: dict[str, str] = ..., 
            sort_options: dict[str, str] = ...
        ) -> list[Resistor]:
        return super().get_filtered_list(filters, sort_options)