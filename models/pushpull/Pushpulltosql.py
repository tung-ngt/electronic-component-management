from os import path
import sys
path_to_models = path.abspath(r'C:\Users\ciltr\Desktop\USTH\Semester 2\Python\Python project\electronic-component-management\models')
sys.path.append(path_to_models)
from db.database_with_classes import get_connection, create_tables, delete_all_tables
from domains import Component
from serializers.Serializer import serialize, deserialize

'''
    Import section needs to be changed base on real project
'''

# Connect to database
conn, mycursor  = get_connection()

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


def pull(kind : str):
    '''
        Pull things from database
    '''

    kind = kind.lower()
    mycursor = conn.cursor()
    mycursor.execute(f"SELECT * FROM {kind}")
    myresult = mycursor.fetchall()
    conn.commit()
    mycursor.close()
    items = []
    for item in myresult:
        items.append(deserialize(kind, item))
    return items
        
'''   
# Test section    
def main():
    delete_all_tables(conn)
    create_tables()
    # Pull from database
    cap_list = pull('capacitor')
    ic_list = pull('ic')
    res_list = pull('resistor')
    ind_list = pull('inductor')
    sen_list = pull('sensor')
    manu_list = pull('manufacturer')

    # Print out the list
    for item in cap_list:
        print(item.get_part_number(), item.get_mnf_id(), item.get_price(), item.get_inventory_date(),
              item.get_guarantee(), item.get_capacitance(), item.get_stock())
    for item in ic_list:
        print(item.get_part_number(), item.get_mnf_id(), item.get_price(), item.get_inventory_date(),
              item.get_guarantee(), item.get_clock(), item.get_stock())
    for item in res_list:
        print(item.get_part_number(), item.get_mnf_id(), item.get_price(), item.get_inventory_date(),
              item.get_guarantee(), item.get_resistance(), item.get_stock())
    for item in ind_list:
        print(item.get_part_number(), item.get_mnf_id(), item.get_price(), item.get_inventory_date(),
              item.get_guarantee(), item.get_inductance(), item.get_stock())
    for item in sen_list:
        print(item.get_part_number(), item.get_mnf_id(), item.get_price(), item.get_inventory_date(),
              item.get_guarantee(), item.get_sensor_type(), item.get_stock())
    for item in manu_list:
        print(item.get_name(), item.get_id(), item.get_country())



if __name__ == '__main__':
    main()
''' 







