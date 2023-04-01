from models.pushpull.Pushpulltosql import pull, push
from models.db.Utils_database import get_connection
from models.domains import IC, Capacitor, Inductor, Manufacturer, Resistor, Sensor

class AppController:
    def __init__(self):
        self.__ics = []
        self.__capacitors = []
        self.__inductors = []
        self.__manufacturers = []
        self.__resistors = []
        self.__sensors = []

    def load_data_from_db(self):
        cap_num, self.__capacitors = pull('capacitor')
        ic_num, self.__ics = pull('ic')
        res_num, self.__resistors = pull('resistor')
        ind_num, self.__inductors = pull('inductor')
        sen_num, self.__sensors = pull('sensor')
        manu_num, self.__manufacturers = pull('manufacturer')

    def get_capacitors(self):
        return self.__capacitors

    def get_ics(self):
        return self.__ics

    def get_inductors(self):
        return self.__inductors

    def get_manufacturers(self):
        return self.__manufacturers

    def get_resistors(self):
        return self.__resistors

    def get_sensors(self):
        return self.__sensors
    
    def add_ic(self, data):
        new_ic = IC(
            data["mnf_id"],
            data["price"],
            data["inventory_date"],
            data["guarantee"],
            data["part_number"],
            data["sub_category"],
            data["stock"],
            data["clock"]
        )
        self.__ics.append(new_ic)
        push(new_ic)
    
    def add_capacitors(self, data):
        new_capacitors = Capacitor(
            data["mnf_id"],
            data["price"],
            data["inventory_date"],
            data["guarantee"],
            data["part_number"],
            data["sub_category"],
            data["stock"],
            data["capacitance"]
        )
        self.__capacitors.append(new_capacitors)
        push(new_capacitors)
    
    def add_inductor(self, data):
        new_inductor = Inductor(
            data["mnf_id"],
            data["price"],
            data["inventory_date"],
            data["guarantee"],
            data["part_number"],
            data["sub_category"],
            data["stock"],
            data["inductance"]
        )
        self.__inductors.append(new_inductor)
        push(new_inductor)
    
    def add_manufacturer(self, data):
        new_manufacturer = Manufacturer(
            data["id"],
            data["name"],
            data["country"],
        )
        self.__manufacturers.append(new_manufacturer)
        push(new_manufacturer)
    
    def add_resistor(self, data):
        new_resistor = Resistor(
            data["mnf_id"],
            data["price"],
            data["inventory_date"],
            data["guarantee"],
            data["part_number"],
            data["sub_category"],
            data["stock"],
            data["resistance"]
        )
        self.__ics.append(new_resistor)
        push(new_resistor)
    
    def add_sensor(self, data):
        new_sensor = Sensor(
            data["mnf_id"],
            data["price"],
            data["inventory_date"],
            data["guarantee"],
            data["part_number"],
            data["sub_category"],
            data["stock"],
            data["sensor_type"]
        )
        self.__ics.append(new_sensor)
        push(new_sensor)

    def get_list_with_filters(self, list_type, filters):
        return pull(list_type, filters)
