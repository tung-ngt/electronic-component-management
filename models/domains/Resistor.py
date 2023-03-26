from .Component import Component
class Resistor(Component):
    """Represents Resistor objects
    
    Attributes
    ----------
    mnf, price, inventory_date, status, guarantee, part_number, resistance
    """
    def __init__(self, mnf, price, inventory_date, status, guarantee, part_number, resistance):
        super().__init__(mnf, price, inventory_date, status, guarantee, part_number)
        self.__resistance = resistance
    def getResistance(self):
        return self.__resistance
    def setResistance(self, resistance):
        self.__resistance = resistance