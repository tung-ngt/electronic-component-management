from .Component import Component
class IC(Component):
    """IC or Intergrated Circuits
    
    Attributes
    ----------
    mnf, price, inventory_date, clock
    """
    def __init__(self, mnf, price, inventory_date, status, guarantee, part_number, clock):
        super().__init__(mnf, price, inventory_date, status, guarantee, part_number)
        self.__clock = clock
    def getClock(self):
        return self.__clock
    def setClock(self, clock):
        self.__clock = clock