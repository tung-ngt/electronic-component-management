from .Component import Component
class Sensor(Component):
    """Represents Sensor objects
    
    Attributes
    ----------
    mnf, price, inventory_date, status, guarantee, part_number, type
    type: temperature, pH or conductivity
    """
    def __init__(self, mnf, price, inventory_date, status, guarantee, part_number, type):
        super().__init__(mnf, price, inventory_date, status, guarantee, part_number)
        self.__type = type
    def getType(self):
        return self.__type
    def setType(self, type):
        self.__type = type