from .Component import Component
from .Manufacturer import Manufacturer
from datetime import date

class Capacitor(Component):
    """Represents Capacitor components

    This class is a subclass of Component
    
    Attributes
    ----------
    mnf_id : manufacturer id
    price : price fo the part must be >= 0
    inventory_date : the date the part gets into inventory
    status : True (sold) False (have not sold)
    guarantee : months of guarantee
    part_number : part identifier string
    capacitance : float capacitance value
    """
    def __init__(self,
            mnf_id: str,
            price: float,
            inventory_date: date,
            status: bool,
            guarantee: int,
            part_number: str,
            capacitance: float
        ):
        super().__init__(mnf_id, price, inventory_date, status, guarantee, part_number)
        self.set_capacitance(capacitance)

    # Getters
    def get_capacitance(self):
        return self.__capacitance    

    # Setters
    def set_capacitance(self, capacitance: float):
        if isinstance(capacitance, float) and capacitance > 0:
            self.__capacitance = capacitance
        else:
            raise Exception("Invalid type of capacitance")