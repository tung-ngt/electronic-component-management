from models.pushpull.Pushpulltosql import pull, push, update, get_sub_category, get_sensor_types
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
        return self.__capacitors.copy()

    def get_ics(self):
        return self.__ics.copy()

    def get_inductors(self):
        return self.__inductors.copy()

    def get_manufacturers(self):
        return self.__manufacturers.copy()

    def get_resistors(self):
        return self.__resistors.copy()

    def get_sensors(self):
        return self.__sensors.copy()
    
    def add_component(self, component_type, data):
        if component_type == "ic":
            self.add_ic(data)
        if component_type == "capacitor":
            self.add_capacitor(data)
        if component_type == "inductor":
            self.add_inductor(data)
        if component_type == "resistor":
            self.add_resistor(data)
        if component_type == "sensor":
            self.add_sensor(data)
    
    def add_ic(self, data):
        new_ic = IC(
            data["mnf_id"],
            float(data["price"]),
            data["inventory_date"],
            int(data["guarantee"]),
            data["part_number"],
            data["sub_category"],
            int(data["stock"]),
            float(data["clock"])
        )
        self.__ics.append(new_ic)
        push(new_ic)
    
    def add_capacitor(self, data):
        new_capacitors = Capacitor(
            data["mnf_id"],
            float(data["price"]),
            data["inventory_date"],
            int(data["guarantee"]),
            data["part_number"],
            data["sub_category"],
            int(data["stock"]),
            float(data["capacitance"])
        )
        self.__capacitors.append(new_capacitors)
        push(new_capacitors)
    
    def add_inductor(self, data):
        new_inductor = Inductor(
            data["mnf_id"],
            float(data["price"]),
            data["inventory_date"],
            int(data["guarantee"]),
            data["part_number"],
            data["sub_category"],
            int(data["stock"]),
            float(data["inductance"])
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
            float(data["price"]),
            data["inventory_date"],
            int(data["guarantee"]),
            data["part_number"],
            data["sub_category"],
            int(data["stock"]),
            float(data["resistance"])
        )
        self.__ics.append(new_resistor)
        push(new_resistor)
    
    def add_sensor(self, data):
        new_sensor = Sensor(
            data["mnf_id"],
            float(data["price"]),
            data["inventory_date"],
            int(data["guarantee"]),
            data["part_number"],
            data["sub_category"],
            int(data["stock"]),
            data["sensor_type"]
        )
        self.__ics.append(new_sensor)
        push(new_sensor)

    def get_list_with_filters(self, list_type, filters, sort_options = []):
        return pull(list_type, filters, sort_options)
    
    def get_sub_categories(self, component_type):
        return get_sub_category(component_type)
    
    def get_sensor_types(self):
        return get_sensor_types()
    
    def update_component(self, component_type, data, part_number):
        update(component_type, data, part_number)
