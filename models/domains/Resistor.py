from .Component import Component
from .Manufacturer import Manufacturer
from datetime import date

class Resistor(Component):
    """Represents Resistor components
    
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
    resistance : float value of resistance
    """
    def __init__(self,
            mnf_id: str,
            price: float,
            inventory_date: date,
            guarantee: int,
            part_number: str,
            sub_category: str,
            stock: int,
            resistance: float,
            image_path: str = None,
        ):
        super().__init__(mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock, image_path)
        self.set_resistance(resistance)

    # Getters
    def get_resistance(self):
        return self.__resistance
    
    def get_all_info(self):
        info = super().get_all_info()
        info.append(self.__resistance)
        return info
    
    # Setters
    def set_resistance(self, resistance: float):
        if isinstance(resistance, float) and resistance >0:
            self.__resistance = resistance
        else:
            raise Exception("Invalid type of resistance")