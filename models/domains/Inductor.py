from .Component import Component
class Inductor(Component):
    """Represents Inductor objects
    
    Attributes
    ----------
    mnf, price, inventory_date, status, guarantee, part_number, inductance
    """
    def __init__(self, mnf, price, inventory_date, status, guarantee, part_number, inductance):
        super().__init__(mnf, price, inventory_date, status, guarantee, part_number)
        self.__inductance = inductance
    def getInductance(self):
        return self.__inductance
    def setInductance(self, inductance):
        if isinstance(inductance, float) and inductance > 0:
            self.__inductance = inductance
        else:
            raise Exception("Invalid type of inductance")