from .Component import Component
from datetime import date
from .Manufacturer import Manufacturer

class IC(Component):
    """IC or Intergrated Circuits
    
    This class is a subclass of Component

    Attributes
    ----------
    mnf : manufacturer
    price : price fo the part must be >= 0
    inventory_date : the date the part gets into inventory
    status : True (sold) False (have not sold)
    guarantee : months of guarantee
    part_number : part identifier string
    clock : clock speed in GHz
    """
    def __init__(self,
            mnf: Manufacturer,
            price: float,
            inventory_date: date,
            status: bool,
            guarantee: int,
            part_number: str,
            clock: float
        ):
        super().__init__(mnf, price, inventory_date, status, guarantee, part_number)
        self.__clock: float = self.set_clock(clock)

    # Getters
    def get_clock(self):
        return self.__clock
    
    # Setters
    def set_clock(self, clock: float):
        if isinstance(clock, float) and clock >0:
            self.__clock = clock
        else:
            raise Exception("Invalid type of clock")