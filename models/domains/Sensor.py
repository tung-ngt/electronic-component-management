from .Component import Component
from .Manufacturer import Manufacturer
from datetime import date

class Sensor(Component):
    """Represents Sensor components
    
    This class is a subclass of Component

    Attributes
    ----------
    mnf_id : manufacturer id
    price : price fo the part must be >= 0
    inventory_date : the date the part gets into inventory
    guarantee : months of guarantee
    part_number : part identifier string
    sensor_type : type of the sensor (temperature, pH, conductivity, ...)
    """
    def __init__(self,
            mnf_id: str,
            price: float,
            inventory_date: date,
            guarantee: int,
            part_number: str,
            sensor_type: str,
        ):
        super().__init__(mnf_id, price, inventory_date, guarantee, part_number)
        self.set_sensor_type(sensor_type)
        
    # Getters
    def get_sensor_type(self):
        return self.__sensor_type
    
    # Setters
    def set_sensor_type(self, sensor_type: str):
        if len(sensor_type) > 0:
            self.__sensor_type: str = sensor_type
        else:
            raise Exception("Sensor type can not be empty")