from .Component import Component
from .Manufacturer import Manufacturer
from datetime import date

class Sensor(Component):
    """Represents Sensor components
    
    This class is a subclass of Component

    Attributes
    ----------
    mnf : manufacturer
    price : price fo the part must be >= 0
    inventory_date : the date the part gets into inventory
    status : True (sold) False (have not sold)
    guarantee : months of guarantee
    part_number : part identifier string
    sensor_type : type of the sensor (temperature, pH, conductivity, ...)
    """
    def __init__(self,
            mnf: Manufacturer,
            price: float,
            inventory_date: date,
            status: bool,
            guarantee: int,
            part_number: str,
            sensor_type: str,
        ):
        super().__init__(mnf, price, inventory_date, status, guarantee, part_number)
        self.__sensor_type: str = self.set_sensor_type(sensor_type)
        
    # Getters
    def get_sensor_type(self):
        return self.__sensor_type
    
    # Setters
    def set_sensor_type(self, sensor_type: str):
        if len(sensor_type) > 0:
            self.__sensor_type: str = sensor_type
        else:
            raise Exception("Sensor type can not be empty")