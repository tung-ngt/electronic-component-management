from re import match
from .Manufacturer import Manufacturer
import os

def validate_date(d: str):
    if match(r"^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$", d) == None:
        raise Exception("Invalid date, must be the form yyyy-mm-dd")
    else:
        return True

def validate_guarantee(g):
    if isinstance(g, int) and g>=0:
        return True
    else:
        raise Exception("Invalid type of guarantee")

def validate_price(p):
    if isinstance(p, float) and p>0:
        return True
    else:
        raise Exception("Invalid type of price")
    
def validate_part_number(part_number):
    if len(part_number) == 0:
        raise Exception("Part number must not be empty")
    else:
        return True

def validate_stock(stock):
    if stock < 0:
        raise Exception("Stock must not be negative")
    else:
        return True

class Component:
    """This class is the entity of electronic components

    Attributes
    ----------
    mnf_id : manufacturer id str
    price : price fo the part must be >= 0
    inventory_date : the date the part gets into inventory
    guarantee : months of guarantee
    part_number : part identifier string
    sub_category : which subcategory does the component belong in
    stock : number of that compnent in the inventory
    """
    def __init__(self,
            mnf_id: str,
            price: float,
            inventory_date: str,
            guarantee: int, 
            part_number: str,
            sub_category: str,
            stock: int,
            image_path: str = None,
        ):
        self.set_image_path(image_path)
        self.set_mnf_id(mnf_id)
        self.set_price(price)
        self.set_inventory_date(inventory_date)
        self.set_guarantee(guarantee)
        self.set_part_number(part_number)
        self.set_sub_category(sub_category)
        self.set_stock(stock)
        self.set_image_path(image_path)

    # Getters
    def get_mnf_id(self):
        return self.__mnf_id
    
    def get_image_path(self):
        return self.__image_path
    
    def get_price(self):
        return self.__price
    
    def get_inventory_date(self):
        return self.__inventory_date
    
    def get_guarantee(self):
        return self.__guarantee
    
    def get_part_number(self):
        return self.__part_number
    
    def get_sub_category(self):
        return self.__sub_category
    
    def get_stock(self):
        return self.__stock
    
    def get_all_info(self):
        return [
            self.__part_number, 
            self.__price, 
            self.__guarantee, 
            self.__mnf_id, 
            self.__inventory_date,
            self.__sub_category, 
            self.__stock
        ]
    
    # Setters
    def set_mnf_id(self, mnf_id):
        self.__mnf_id = mnf_id

    def set_image_path(self, image_path):
        if image_path == None or image_path == "None":
            self.__image_path = "None"
            return

        if os.path.isfile(f"./images/components/{image_path}"):
            self.__image_path = image_path
        else:
            raise Exception("Image path not found")

    def set_price(self, price: float):
        if validate_price(price):
            self.__price = price

    def set_inventory_date(self, inventory_date: str):
        if validate_date(inventory_date):
            self.__inventory_date = inventory_date

    def set_guarantee(self, guarantee: int):
        if validate_guarantee(guarantee):
            self.__guarantee = guarantee

    def set_part_number(self, part_number: str):
        if validate_part_number(part_number):
            self.__part_number = part_number

    def set_sub_category(self, sub_category: str):
        self.__sub_category = sub_category
    
    def set_stock(self, stock: int):
        if validate_stock(stock):
            self.__stock = stock