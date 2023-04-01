from .Component import Component
from .Manufacturer import Manufacturer
from datetime import date

class Inductor(Component):
    """Represents Inductor components

    This is a subclass of Component
    
    Attributes
    ----------
    mnf_id : manufacturer id
    price : price fo the part must be >= 0
    inventory_date : the date the part gets into inventory
    guarantee : months of guarantee
    part_number : part identifier string
    sub_category : which subcategory does the component belong in
    stock : number of that compnent in the inventory
    inductance : inductance value
    """
    def __init__(self,
            mnf_id: str,
            price: float,
            inventory_date: date,
            guarantee: int,
            part_number: str,
            sub_category: str,
            stock: int,
            inductance: float
        ):
        super().__init__(mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock)
        self.set_inductance(inductance)

    # Getters
    def get_inductance(self):
        return self.__inductance
    
    def get_all_info(self):
        info = super().get_all_info()
        info.append(self.__inductance)
        return info
    
    # Setters
    def set_inductance(self, inductance: float):
        if isinstance(inductance, float) and inductance > 0:
            self.__inductance = inductance
        else:
            raise Exception("Invalid type of inductance")