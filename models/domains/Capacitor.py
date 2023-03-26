from .Component import Component
class Capacitor(Component):
    """Represents Capacitor objects
    
    Attributes
    ----------
    mnf, price, inventory_date, status, guarantee, part_number, capacitance
    """
    def __init__(self, mnf, price, inventory_date, status, guarantee, part_number, capacitance):
        super().__init__(mnf, price, inventory_date, status, guarantee, part_number)
        self.__capacitance = capacitance
    def getCapacitance(self):
        return self.__capacitance
    def setCapacitance(self, capacitance):
        self.__capacitance = capacitance