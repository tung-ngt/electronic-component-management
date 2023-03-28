from datetime import date
from .Manufacturer import Manufacturer

# def validate_date_time(d: str):
#     if datetime.strptime(d, '%d-%m-%Y'):
#         return 1
#     else:
#         raise Exception("Invalid type of d-m-Y")

def validate_status(s):
    if s == True or s == False:
        return 1
    else:
        raise Exception("Invalid type of status")

def validate_guarantee(g):
    if isinstance(g, int) and g>0:
        return 1
    else:
        raise Exception("Invalid type of guarantee")

def validate_price(p):
    if isinstance(p, float) and p>0:
        return 1
    else:
        raise Exception("Invalid type of price")

class Component:
    """This class is the entity of electronic components

    Attributes
    ----------
    mnf : manufacturer
    price : price fo the part must be >= 0
    inventory_date : the date the part gets into inventory
    status : True (sold) False (have not sold)
    guarantee : months of guarantee
    part_number : part identifier string
    """
    def __init__(self,
            mnf: Manufacturer,
            price: float,
            inventory_date: date,
            status: bool,
            guarantee: int, 
            part_number: str,
            sub_categories: tuple(str)
        ):
        self.__mnf: Manufacturer = self.set_mnf(mnf)
        self.__price: float = self.set_price(price)
        self.__inventory_date: date = self.set_inventory_date(inventory_date)
        self.__status: bool = self.set_status(status)
        self.__guarantee: int = self.set_guarantee(guarantee)
        self.__part_number: str = self.set_part_number(part_number)
        self.__sub_categories: tuple[str] = self.set_sub_cateories(sub_categories)

    # Getters
    def get_mnf(self):
        return self.__mnf
    
    def get_price(self):
        return self.__price
    
    def get_inventory_date(self):
        return self.__inventory_date
    
    def get_status(self):
        return self.__status
    
    def get_guarantee(self):
        return self.__guarantee
    
    def get_part_number(self):
        return self.__part_number
    
    def get_sub_categories(self):
        return self.__sub_categories
    
    # Setters
    def set_mnf(self, mnf):
        self.__mnf = mnf

    def set_price(self, price: float):
        if validate_price(price):
            self.__price = price

    def set_inventory_date(self, inventory_date: date):
        # if validate_date_time(inventory_date):
        self.__inventory_date = inventory_date

    def set_status(self, status: bool):
        if validate_status(status):
            self.__status = status

    def set_guarantee(self, guarantee: int):
        if validate_guarantee(guarantee):
            self.__guarantee = guarantee

    def set_part_number(self, part_number: str):
        self.__part_number = part_number

    def set_sub_categories(self, sub_categories: tuple[str]):
        self.__sub_categories = sub_categories
    