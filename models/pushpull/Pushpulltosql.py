from models.db.Utils_database import get_connection
from models.domains import Component
from models.serializers.Serializer import serialize, deserialize
from controllers.component_controller import filter_component, count_condition

'''
    Import section needs to be changed base on real project
'''



# Push and pull from database
def push(thing):
    '''
        Push thing to database                 
    '''
    # Connect to database
    conn, mycursor  = get_connection('./data/electronic_store_with_classes.db')
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


def pull(kind : str, option : dict = {}):
    '''
        Pull things from database
    '''
    # Connect to database
    conn, mycursor  = get_connection('./data/electronic_store_with_classes.db')
    kind = kind.lower()
    mycursor = conn.cursor()
    myresult = filter_component(kind, option)

    conn.commit()
    mycursor.close()
    items = []
    for item in myresult:
        items.append(deserialize(kind, item))
    return count_condition(kind, option)[0][0], items
        
  








