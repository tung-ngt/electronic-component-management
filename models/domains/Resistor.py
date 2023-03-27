from .Component import Component
from .Manufacturer import Manufacturer
from datetime import date

class Resistor(Component):
    """Represents Resistor components
    
    This class is a subclass of Component

    Attributes
    ----------
    mnf : manufacturer
    price : price fo the part must be >= 0
    inventory_date : the date the part gets into inventory
    status : True (sold) False (have not sold)
    guarantee : months of guarantee
    part_number : part identifier string
    resistance : float value of resistance
    """
    def __init__(self,
            mnf: Manufacturer,
            price: float,
            inventory_date: date,
            status: bool,
            guarantee: int,
            part_number: str,
            resistance: float
        ):
        super().__init__(mnf, price, inventory_date, status, guarantee, part_number)
        self.__resistance: float = self.set_resistance(resistance)

    # Getters
    def get_resistance(self):
        return self.__resistance
    
    # Setters
    def set_resistance(self, resistance: float):
        if isinstance(resistance, float) and resistance >0:
            self.__resistance = resistance
        else:
            raise Exception("Invalid type of resistance")