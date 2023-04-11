from .ComponentController import ComponentController
from models.domains import IC
from models.serializers.component_serializers import ICSerializer

class ICController(ComponentController):
    def __init__(self) -> None:
        super().__init__(
            "ic",
            ["clock", "range"],
            ICSerializer()
        )
        
    def get_list(self) -> list[IC]:
        return super().get_list()
    
    def add(self, data: dict) -> IC:
        new_component = super().add(data)
        new_ic = IC(
            new_component.get_mnf_id(),
            new_component.get_price(),
            new_component.get_inventory_date(),
            new_component.get_guarantee(),
            new_component.get_part_number(),
            new_component.get_sub_category(),
            new_component.get_stock(),
            float(data["clock"])
        )
        self.add_to_list(new_ic)
        self.create_db_row(new_ic)
        return new_ic

    def update(self, data: dict[str, str], key: str) -> IC:
        component_to_update: IC = super().update(data, key)

        if "clock" in data.keys() and data["clock"]:
            component_to_update.set_clock(float(data["clock"]))

        self.update_db_row(data, key)
        return component_to_update

    def get_filtered_list(
            self,
            filters: dict[str, str] = ..., 
            sort_options: dict[str, str] = ...
        ) -> list[IC]:
        return super().get_filtered_list(filters, sort_options)