from os import path
import sys
path_to_models = path.abspath(r'C:\Users\ciltr\Desktop\USTH\Semester 2\Python\Python project\electronic-component-management\models')
sys.path.append(path_to_models)
from db.Utils_database import get_connection
from domains import Component
from serializers.Serializer import serialize, deserialize

'''
    Import section needs to be changed base on real project
'''

# Connect to database
conn, mycursor  = get_connection('electronic_store_with_classes')

# Push and pull from database
def push(thing):
    '''
        Push thing to database                 
    '''

    mycursor = conn.cursor()
    if isinstance(thing, Component):
        mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock = serialize(thing)

        if type(thing).__name__ == 'Capacitor':
            special_att = thing.get_capacitance()
            mycursor.execute(f"INSERT INTO {type(thing).__name__} (part_number, mnf_id , price, inventory_date, guarantee, capacitance, sub_category, stock) VALUES {part_number, mnf_id, price, inventory_date, guarantee,  special_att, sub_category, stock};")

        elif type(thing).__name__ == 'Resistor':  
            special_att = thing.get_resistance()
            mycursor.execute(f"INSERT INTO {type(thing).__name__} (part_number, mnf_id , price, inventory_date, guarantee, resistance, sub_category, stock) VALUES {part_number, mnf_id, price, inventory_date, guarantee,  special_att, sub_category, stock};")

        elif type(thing).__name__ == 'Inductor':
            special_att = thing.get_inductance()
            mycursor.execute(f"INSERT INTO {type(thing).__name__} (part_number, mnf_id , price, inventory_date, guarantee, inductance, sub_category, stock) VALUES {part_number, mnf_id, price, inventory_date, guarantee,  special_att, sub_category, stock};")

        elif type(thing).__name__ == 'Sensor':
            special_att = thing.get_sensor_type()
            mycursor.execute(f"INSERT INTO {type(thing).__name__} (part_number, mnf_id , price, inventory_date, guarantee, sensor_type, sub_category, stock) VALUES {part_number, mnf_id, price, inventory_date, guarantee,  special_att, sub_category, stock};")

        elif type(thing).__name__ == 'IC':
            special_att = thing.get_clock()
            mycursor.execute(f"INSERT INTO {type(thing).__name__} (part_number, mnf_id , price, inventory_date, guarantee, clock, sub_category, stock) VALUES {part_number, mnf_id, price, inventory_date, guarantee,  special_att, sub_category, stock};")
  
    elif type(thing).__name__ == 'Manufacturer':
        name, ID, country = serialize(thing)
        mycursor.execute(f"INSERT INTO {type(thing).__name__} (id, name, country) VALUES {ID, name, country}")

    conn.commit()
    mycursor.close()


def pull(kind : str, option : str = ""):
    '''
        Pull things from database
    '''

    kind = kind.lower()
    mycursor = conn.cursor()

    if option != "":
        mycursor.execute(f"SELECT * FROM {kind} where {option}")
    else:
        mycursor.execute(f"SELECT * FROM {kind}")

    myresult = mycursor.fetchall()
    conn.commit()
    mycursor.close()
    items = []
    for item in myresult:
        items.append(deserialize(kind, item))
    return items
        
  








