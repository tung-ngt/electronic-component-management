from db.push_to_db import create_row, update_row
from db.pull_from_db import get_rows,  get_distinct_column

from .model_controllers import ManufacturerController, CustomerController, OrderController
from .model_controllers.component_controllers import \
CapacitorController, \
ICController, \
ResistorController, \
SensorController, \
InductorController

from .utils import file_utils
import os
import threading

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
        self.add_order = self.order_controller.add

        self.update_manufacturer = self.manufacturer_controller.update
        self.update_customer = self.customer_controller.update
        self.update_order = self.order_controller.update

        self.load_data_from_db()

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
    
    # def update_mnf_image(self, image, man_id):
    #     update("manufacturer", {"image_path" : image}, man_id)
    
    # def update_component_image(self, image, component_type, part_number):
    #     update(component_type, {"image_path" : image}, part_number)
    
    def get_subcategories(self, component_type):
        controller = self.__controller_switcher(component_type)
        return controller.get_subcategories()
    
    
    # def get_sensor_types(self):
    #     return get_sensor_types()
    
    def get_mnf_countries(self):
        return self.get_distinct_column("manufacturer", "country")
    

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
    # def compress_and_remove_image(self, img):
    #     file_utils.compress_file(img)
    #     os.remove(img) 

    # def compress_all_images(self):
    #     manufacturer_imgs = file_utils.get_files_of_type("./images/manufacturers/", ".png")
    #     for manufacturer_img in manufacturer_imgs:
    #         thread = threading.Thread(
    #             target=self.compress_and_remove_image,
    #             args=(f"./images/manufacturers/{manufacturer_img}",)
    #         )
    #         thread.start()
    
    # def decompress_image(self, img):
    #     file = img.replace(".dat", "")
    #     file_utils.write_bytes_to_file(file, file_utils.decompress_file_bytes(img))
        

    # def decompress_all_images(self):
    #     manufacturer_imgs = file_utils.get_files_of_type("./images/manufacturers/", ".png.dat")
    #     for manufacturer_img in manufacturer_imgs:
    #         thread = threading.Thread(
    #             target=self.decompress_image,
    #             args=(f"./images/manufacturers/{manufacturer_img}",)
    #         )
    #         thread.start()
    
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
    
