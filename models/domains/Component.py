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
    mnf_id : manufacturer id str
    price : price fo the part must be >= 0
    inventory_date : the date the part gets into inventory
    status : True (sold) False (have not sold)
    guarantee : months of guarantee
    part_number : part identifier string
    sub_category : which sub category does the component belong in
    """
    def __init__(self,
            mnf_id: str,
            price: float,
            inventory_date: date,
            status: bool,
            guarantee: int, 
            part_number: str,
            sub_category: str
        ):
        self.set_mnf_id(mnf_id)
        self.set_price(price)
        self.set_inventory_date(inventory_date)
        self.set_status(status)
        self.set_guarantee(guarantee)
        self.set_part_number(part_number)
        self.set_sub_category(sub_category)

    # Getters
    def get_mnf_id(self):
        return self.__mnf_id
    
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
    
    def get_sub_category(self):
        return self.__sub_category
    
    # Setters
    def set_mnf_id(self, mnf_id):
        self.__mnf_id = mnf_id

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

    def set_sub_category(self, sub_category: str):
        self.__sub_category = sub_category
    