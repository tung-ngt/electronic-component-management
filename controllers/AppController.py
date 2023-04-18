from db.pull_from_db import get_distinct_column

from .model_controllers import ManufacturerController, CustomerController, OrderController
from .model_controllers.component_controllers import \
CapacitorController, \
ICController, \
ResistorController, \
SensorController, \
InductorController

from .utils import file_utils
from threading import Thread

class AppController:
    def __init__(self):
        self.ic_controller = ICController()
        self.capacitor_controller = CapacitorController()
        self.inductor_controller = InductorController()
        self.resistor_controller = ResistorController()
        self.sensor_controller = SensorController()
        
        self.manufacturer_controller = ManufacturerController()
        self.customer_controller = CustomerController()
        self.order_controller = OrderController()

        self.add_manufacturer = self.manufacturer_controller.add
        self.add_customer = self.customer_controller.add

        self.update_manufacturer = self.manufacturer_controller.update
        self.update_customer = self.customer_controller.update
        self.update_order = self.order_controller.update

    def add_order(self, data):
        items = data["items"]
        for part_number, amount in list(items.items()):
            print(part_number)
            print(amount)
            component_type, c = self.get_component(part_number)
            print(component_type)
            print(c.get_all_info())
            controller = self.__controller_switcher(component_type)
            print(controller)
            controller.update({"stock": c.get_stock() - amount}, part_number)
        self.order_controller.add(data)

    def get_component(self, part_number):   
        for c in self.get_list("ic"):
            if c.get_part_number() == part_number:
                return "ic", c
        for c in self.get_list("inductor"):
            if c.get_part_number() == part_number:
                return "inductor", c
        for c in self.get_list("capacitor"):
            if c.get_part_number() == part_number:
                return "capacitor", c
        for c in self.get_list("resistor"):
            if c.get_part_number() == part_number:
                return "resistor", c
        for c in self.get_list("sensor"):
            if c.get_part_number() == part_number:
                return "sensor", c

    def load_data_from_db(self):
        self.ic_controller.load_data_from_db()
        self.capacitor_controller.load_data_from_db()
        self.inductor_controller.load_data_from_db()
        self.resistor_controller.load_data_from_db()
        self.sensor_controller.load_data_from_db()
        self.manufacturer_controller.load_data_from_db()
        self.order_controller.load_data_from_db()
        self.customer_controller.load_data_from_db()

    def __controller_switcher(self, table):
        if table == "ic":
            return self.ic_controller
        if table == "capacitor":
            return self.capacitor_controller
        if table == "inductor":
            return self.inductor_controller
        if table == "resistor":
            return self.resistor_controller
        if table == "sensor":
            return self.sensor_controller
        if table == "order":
            return self.order_controller
        if table == "manufacturer":
            return self.manufacturer_controller
        if table == "customer":
            return self.customer_controller

    def get_list(self, table):
        controller = self.__controller_switcher(table)
        return controller.get_list()
    
    def add(self, table, data):
        controller = self.__controller_switcher(table)
        controller.add(data)
    
    def update_component(self, component_type, data, part_number):
        controller = self.__controller_switcher(component_type)
        controller.update(data, part_number)
    
    def get_filtered_list(
            self, 
            table, 
            filters: dict[str, str] = {},
            sort_options: dict[str, str]= {}
        ):
        controller = self.__controller_switcher(table)
        return controller.get_filtered_list(filters, sort_options)
    
    def get_subcategories(self, component_type):
        controller = self.__controller_switcher(component_type)
        return controller.get_subcategories()
    
    def get_mnf_countries(self):
        return self.get_distinct_column("manufacturer", "country")
    
    def get_all_components_prices(self):
        components = []
        components.extend(self.capacitor_controller.get_list())
        components.extend(self.resistor_controller.get_list())
        components.extend(self.ic_controller.get_list())
        components.extend(self.inductor_controller.get_list())
        components.extend(self.sensor_controller.get_list())

        components_prices = {}
        for r in components:
            components_prices[r.get_part_number()] = r.get_price()
        return components_prices

    def get_no_of_components(self):
        return len(self.capacitor_controller.get_list()) \
             + len(self.ic_controller.get_list()) \
             + len(self.inductor_controller.get_list()) \
             + len(self.resistor_controller.get_list()) \
             + len(self.sensor_controller.get_list())

    def get_distinct_column(sef, table, column):
        if table == "order":
            table = "orders"
        return get_distinct_column(table, column)

    def zip_images(self):
        compressed_components_imgs = file_utils.get_files_of_type("./images/components/", ".png", with_path=True)

        components_zip_thread = Thread(
            target=file_utils.zip_files,
            args=(compressed_components_imgs, "./images/components/components.zip",)
        )
        components_zip_thread.start()

        compressed_manufacturers_imgs = file_utils.get_files_of_type("./images/manufacturers/", ".png", with_path=True)
        manufacturers_zip_thread = Thread(
            target=file_utils.zip_files,
            args=(compressed_manufacturers_imgs, "./images/manufacturers/manufacturers.zip",)
        )
        manufacturers_zip_thread.start()

        components_zip_thread.join()
        Thread(
            target=file_utils.remove_files,
            args=(compressed_components_imgs,)
        ).start()

        manufacturers_zip_thread.join()
        Thread(
            target=file_utils.remove_files,
            args=(compressed_manufacturers_imgs,)
        ).start()

    def unzip_images(self):
        component_thread = Thread(
            target=file_utils.unzip_file,
            args=("./images/components/components.zip",)
        )
        component_thread.start()


        manufacturer_thead = Thread(
            target=file_utils.unzip_file,
            args=("./images/manufacturers/manufacturers.zip",)
        )
        manufacturer_thead.start()

        component_thread.join()
        manufacturer_thead.join()