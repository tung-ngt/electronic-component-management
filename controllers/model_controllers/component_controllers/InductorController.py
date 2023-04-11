from .ComponentController import ComponentController
from models.domains import Inductor
from models.serializers.component_serializers import InductorSerializer

class InductorController(ComponentController):
    def __init__(self) -> None:
        super().__init__(
            "inductor", 
            ["inductance", "range"],
            InductorSerializer()
        )
    def get_list(self) -> list[Inductor]:
        return super().get_list()
        
    def add(self, data: dict) -> Inductor:
        new_component = super().add(data)
        new_inductor = Inductor(
            new_component.get_mnf_id(),
            new_component.get_price(),
            new_component.get_inventory_date(),
            new_component.get_guarantee(),
            new_component.get_part_number(),
            new_component.get_sub_category(),
            new_component.get_stock(),
            float(data["inductance"])
        )
        self.add_to_list(new_inductor)
        self.create_db_row(new_inductor)
        return new_inductor
    
    def update(self, data: dict[str, str], key: str) -> Inductor:
        component_to_update: Inductor = super().update(data, key)

        if "inductance" in data.keys() and data["inductance"]:
            component_to_update.set_inductance(float(data["inductance"]))

        self.update_db_row(data, key)
        return component_to_update

    def get_filtered_list(
            self, 
            filters: dict[str, str] = ...,
            sort_options: dict[str, str] = ...
        ) -> list[Inductor]:
        return super().get_filtered_list(filters, sort_options)