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
    guarantee : months of guarantee
    part_number : part identifier string
    capacitance : float capacitance value
    sub_category : which subcategory does the component belong in
    stock : number of that compnent in the inventory
    """
    def __init__(self,
            mnf_id: str,
            price: float,
            inventory_date: date,
            guarantee: int,
            part_number: str,
            sub_category: str,
            stock: int,
            capacitance: float
        ):
        super().__init__(mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock)
        self.set_capacitance(capacitance)

    # Getters
    def get_capacitance(self):
        return self.__capacitance

    def get_all_info(self):
        info = super().get_all_info()
        info.append(self.__capacitance)
        return info

    # Setters
    def set_capacitance(self, capacitance: float):
        if isinstance(capacitance, float) and capacitance > 0:
            self.__capacitance = capacitance
        else:
            raise Exception("Invalid type of capacitance")