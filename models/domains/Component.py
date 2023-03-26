from datetime import datetime
def validate_date_time(d):
    if datetime.strptime(d, '%d-%m-%Y'):
        return 1
    else:
        raise Exception("Invalid type of d-m-Y")
def validate_status(s):
    if s == 0 or s == 1:
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
    mnf: manufacturer
    price
    inventory_date
    status
    guarantee
    part_number
    """
    def __init__(self, mnf, price, inventory_date, status, guarantee, part_number) :
        self.__mnf = mnf
        self.__price = price
        self.__inventory_date = inventory_date
        self.__status = status
        self.__guarantee = guarantee
        self.__part_number = part_number
    def getMnf(self):
        return self.__mnf
    def getPrice(self):
        return self.__price
    def getInventory_date(self):
        return self.__inventory_date
    def getStatus(self):
        return self.__status
    def getGuarantee(self):
        return self.__guarantee
    def getPart_number(self):
        return self.__part_number
    def setMnf(self, mnf):
        self.__mnf = mnf
    def setPrice(self, price):
        if validate_price(price):
            self.__price = price
    def setInventory_date(self, inventory_date):
        if validate_date_time(inventory_date):
            self.__inventory_date = inventory_date
    def setStatus(self, status):
        if validate_status(status):
            self.__status = status
    def setGuarantee(self, guarantee):
        if validate_guarantee(guarantee):
            self.__guarantee = guarantee
    def setPart_number(self, part_number):
        self.__part_number = part_number