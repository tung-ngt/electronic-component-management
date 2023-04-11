import pickle
from db.functions import create_tables, delete_all_tables
from db.push_to_db import create_rows
from models.serializers.ManufacturerSerializer import ManufacturerSerializer
from models.serializers.component_serializers.SensorSerializer import SensorSerializer
from models.serializers.component_serializers.ICSerializer import ICSerializer
from models.serializers.component_serializers.InductorSerializer import InductorSerializer
from models.serializers.component_serializers.ResistorSerializer import ResistorSerializer
from models.serializers.component_serializers.CapacitorSerializer import CapacitorSerializer
from models.serializers.CustomerSerializer import CustomerSerializer
from models.serializers.OrderSerializer import OrderSerializer

def reset_database():
    delete_all_tables()
    create_tables()

def load_data():
    manufacturer_serializer = ManufacturerSerializer()
    sensor_serializer = SensorSerializer()
    ic_serializer = ICSerializer()
    inductor_serializer = InductorSerializer()
    resistor_serializer = ResistorSerializer()
    capacitor_serializer = CapacitorSerializer()
    customer_serializer = CustomerSerializer()
    order_serializer = OrderSerializer()

    # Load the data from pickle
    with open('./generated_data/manufacturers.pickle', 'rb') as f:
        manufacturers = pickle.load(f)
    manufacturers_data = manufacturer_serializer.dump_many(manufacturers)
    create_rows("manufacturer", manufacturers_data)
    
    with open('./generated_data/sensors.pickle', 'rb') as f:
        sensors = pickle.load(f)
    sensors_data = sensor_serializer.dump_many(sensors)
    create_rows("sensor", sensors_data)
    
    with open('./generated_data/ics.pickle', 'rb') as f:
        ics = pickle.load(f)
    ics_data = ic_serializer.dump_many(ics)
    create_rows("ic", ics_data)
    
    with open('./generated_data/inductors.pickle', 'rb') as f:
        inductors = pickle.load(f)
    inductors_data = inductor_serializer.dump_many(inductors)
    create_rows("inductor", inductors_data)
    
    with open('./generated_data/resistors.pickle', 'rb') as f:
        resistors = pickle.load(f)
    resistors_data = resistor_serializer.dump_many(resistors)
    create_rows("resistor", resistors_data)
    
    with open('./generated_data/capacitors.pickle', 'rb') as f:
        capacitors = pickle.load(f)
    capacitors_data = capacitor_serializer.dump_many(capacitors)
    create_rows("capacitor", capacitors_data)
    
    with open('./generated_data/customers.pickle', 'rb') as f:
        customers = pickle.load(f)
    customers_data = customer_serializer.dump_many(customers)
    create_rows("customer", customers_data)
    
    with open('./generated_data/orders.pickle', 'rb') as f:
        orders = pickle.load(f)
    orders_data = order_serializer.dump_many(orders)
    create_rows("orders", orders_data)

if __name__ == "__main__":
    create_tables()
    load_data()