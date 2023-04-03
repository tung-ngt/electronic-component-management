from .Component import Component
from datetime import date
from .Manufacturer import Manufacturer

class IC(Component):
    """IC or Intergrated Circuits
    
    This class is a subclass of Component

    Attributes
    ----------
    mnf_id : manufacturer id
    price : price fo the part must be >= 0
    inventory_date : the date the part gets into inventory
    guarantee : months of guarantee
    part_number : part identifier string
    sub_category : which subcategory does the component belong in
    stock : number of that compnent in the inventory
    clock : clock speed in GHz
    """
    def __init__(self,
            mnf_id: str,
            price: float,
            inventory_date: date,
            guarantee: int,
            part_number: str,
            sub_category: str,
            stock: int,
            clock: float,
            image_path: str = None
        ):
        super().__init__(mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock, image_path)
        self.set_clock(clock)

    # Getters
    def get_clock(self):
        return self.__clock
    
    def get_all_info(self):
        info = super().get_all_info()
        info.append(self.__clock)
        return info
    
    # Setters
    def set_clock(self, clock: float):
        if isinstance(clock, float) and clock >0:
            self.__clock = clock
        else:
            raise Exception("Invalid type of clock")