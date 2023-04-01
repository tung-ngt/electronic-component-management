from models.db.Utils_database import get_connection
from models.domains import Component
from models.serializers.Serializer import serialize, deserialize
from controllers.item_controller import filter_component, filter_manufacturer

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


def pull(table : str, condition : dict = {}, sort_option = ""):
    '''
        Pull things from database
    '''
    # Connect to database
    conn, mycursor  = get_connection('./data/electronic_store_with_classes.db')
    table = table.lower()
    mycursor = conn.cursor()

    if table in ['capacitor', 'resistor', 'ic', 'sensor', 'inductor']:
        count, myresult = filter_component(table, condition, sort_option)
       
    elif table == 'manufacturer':
        count, myresult = filter_manufacturer(table, condition, sort_option)
        

    conn.commit()
    mycursor.close()
    items = []
    for item in myresult:
        items.append(deserialize(table, item))

    return count, items


def update(table : str, change_value : list, change_place : list):
    '''
        Update things in database
        Example : update('capacitor', [('part_number', '1'), ('price', '100')])
        * len(change_place) must be equal to len(change_value)
    '''
    # Connect to database
    conn, mycursor  = get_connection('./data/electronic_store_with_classes.db')
    mycursor = conn.cursor()

    try:
        for i in range(len(change_place)):
            query = f"""UPDATE {table} SET {change_value[i][0]} = {change_value[i][1]} WHERE {change_place[i][0]} = '{change_place[i][1]}';"""
            #print(query)
            mycursor.execute(query)
    except:
        return False

    conn.commit()
    mycursor.close()

        
  
def get_sub_category(table : str):
    '''
        Get sub category from database
    '''
    # Connect to database
    conn, mycursor  = get_connection('./data/electronic_store_with_classes.db')
    mycursor = conn.cursor()
    mycursor.execute(f"SELECT DISTINCT sub_category FROM {table}")
    result = mycursor.fetchall()
    sub_category = []
    for item in result:
        sub_category.append(item[0])
    return sub_category







