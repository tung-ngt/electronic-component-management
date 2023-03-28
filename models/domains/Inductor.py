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
    status : True (sold) False (have not sold)
    guarantee : months of guarantee
    part_number : part identifier string
    inductance : inductance value
    """
    def __init__(self,
            mnf_id: str,
            price: float,
            inventory_date: date,
            status: bool,
            guarantee: int,
            part_number: str,
            inductance: float
        ):
        super().__init__(mnf_id, price, inventory_date, status, guarantee, part_number)
        self.set_inductance(inductance)

    # Getters
    def get_inductance(self):
        return self.__inductance
    
    # Setters
    def set_inductance(self, inductance: float):
        if isinstance(inductance, float) and inductance > 0:
            self.__inductance = inductance
        else:
            raise Exception("Invalid type of inductance")