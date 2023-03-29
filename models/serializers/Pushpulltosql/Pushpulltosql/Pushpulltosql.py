import sqlite3
from os import path
import sys
path_to_models = path.abspath(r'C:\Users\ciltr\Desktop\USTH\Semester 2\Python\Python project\electronic-component-management\models')
sys.path.append(path_to_models)
from db.create_database import delete_all_tables, create_tables
from domains import Component, Capacitor, Resistor, Inductor, Sensor, IC, Manufacturer

# Connect to database
conn = sqlite3.connect('electronic_store.db')  
mycursor = conn.cursor()

# Index
index_compo = {'part_number' : 0, 'mnf_id' : 1, 'price' : 2, 
         'inventory_date' : 3, 'guarantee' : 4, 'special_att' : 5,
         'sub_category' : 6, 'stock' : 7}

index_manu = {'name' : 0, 'ID' : 1, 'country' : 2}

# Enter info
def enter_component(kind, mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock, special_att):
    '''Enter info of component'''
    kind = kind.lower()
    if kind == 'capacitor':
        return Capacitor(mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock, special_att)
    elif kind == 'resistor':
        return Resistor(mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock, special_att)
    elif kind == 'inductor':
        return Inductor(mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock, special_att)
    elif kind == 'sensor':
        return Sensor(mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock, special_att)
    elif kind == 'ic':
        return IC(mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock, special_att)
    else:
        print('Invalid input')

def enter_manufacturer(name, id, country):
    '''Enter info of manufacturer'''
    return Manufacturer(name, id, country)



# Serialize and deserialize
def serialize(thing):
    '''
        Serialize thing to push to database
    '''
    if isinstance(thing, Component):
        mnf_id = thing.get_mnf_id()
        price = thing.get_price()
        inventory_date = thing.get_inventory_date()
        guarantee = thing.get_guarantee()
        part_number = thing.get_part_number()
        sub_category = thing.get_sub_category()
        stock = thing.get_stock()
        return mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock

    elif type(thing).__name__ == 'Manufacturer':
        name = thing.get_name()
        ID = thing.get_id()
        country = thing.get_country()
        return name, ID, country

def deserialize(kind:str, myresult:list):
    '''
        Deserialize thing pulled from database
    '''
    compo_list = ['capacitor', 'resistor', 'inductor', 'ic']
    if kind in compo_list:
        mnf_id = myresult[index_compo['mnf_id']]
        price = myresult[index_compo['price']]
        inventory_date = myresult[index_compo['inventory_date']]    
        guarantee = myresult[index_compo['guarantee']]
        part_number = myresult[index_compo['part_number']]
        special_att = float(myresult[index_compo['special_att']])
        sub_category = myresult[index_compo['sub_category']]
        stock = myresult[index_compo['stock']]

        if kind == 'capacitor':
            return Capacitor(mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock, special_att)
        elif kind == 'resistor':
            return Resistor(mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock, special_att)
        elif kind == 'inductor':
            return Inductor(mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock, special_att)
        elif kind == 'ic':
            return IC(mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock, special_att)

    elif kind == 'sensor':
        mnf_id = myresult[index_compo['mnf_id']]
        price = myresult[index_compo['price']]
        inventory_date = myresult[index_compo['inventory_date']]    
        guarantee = myresult[index_compo['guarantee']]
        part_number = myresult[index_compo['part_number']]
        special_att = myresult[index_compo['special_att']]
        sub_category = myresult[index_compo['sub_category']]
        stock = myresult[index_compo['stock']]
        return Sensor(mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock, special_att)
        

    elif kind == 'manufacturer':
        name = myresult[index_manu['name']]
        ID = myresult[index_manu['ID']]
        country = myresult[index_manu['country']]
        return Manufacturer(name, ID, country)




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
            mycursor.execute(f"INSERT INTO {type(thing).__name__.lower()} (part_number, mnf_id , price, inventory_date, guarantee, capacitance, sub_category, stock) VALUES {part_number, mnf_id, price, inventory_date, guarantee,  special_att, sub_category, stock};")

        elif type(thing).__name__ == 'Resistor':  
            special_att = thing.get_resistance()
            mycursor.execute(f"INSERT INTO {type(thing).__name__.lower()} (part_number, mnf_id , price, inventory_date, guarantee, resistance, sub_category, stock) VALUES {part_number, mnf_id, price, inventory_date, guarantee,  special_att, sub_category, stock};")

        elif type(thing).__name__ == 'Inductor':
            special_att = thing.get_inductance()
            mycursor.execute(f"INSERT INTO {type(thing).__name__.lower()} (part_number, mnf_id , price, inventory_date, guarantee, inductance, sub_category, stock) VALUES {part_number, mnf_id, price, inventory_date, guarantee,  special_att, sub_category, stock};")

        elif type(thing).__name__ == 'Sensor':
            special_att = thing.get_sensor_type()
            mycursor.execute(f"INSERT INTO {type(thing).__name__.lower()} (part_number, mnf_id , price, inventory_date, guarantee, sensor_type, sub_category, stock) VALUES {part_number, mnf_id, price, inventory_date, guarantee,  special_att, sub_category, stock};")

        elif type(thing).__name__ == 'IC':
            special_att = thing.get_clock()
            mycursor.execute(f"INSERT INTO {type(thing).__name__.lower()} (part_number, mnf_id , price, inventory_date, guarantee, clock, sub_category, stock) VALUES {part_number, mnf_id, price, inventory_date, guarantee,  special_att, sub_category, stock};")
  
    elif type(thing).__name__ == 'Manufacturer':
        name, ID, country = serialize(thing)
        mycursor.execute(f"INSERT INTO {type(thing).__name__.lower()} (id, name, country) VALUES {ID, name, country}")

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
  
    # Create a new manufacturer
    manu_id_list = []
    manu1 = Manufacturer('1111', 'm', 'vn')
    manu_id_list.append(manu1.get_id())
    push(manu1)
    manu2 = Manufacturer('2222', 'm', 'vn')
    manu_id_list.append(manu2.get_id())
    push(manu2)
    manu3 = Manufacturer('3333', 'm', 'vn')
    manu_id_list.append(manu3.get_id())
    push(manu3)
    manu4 = Manufacturer('4444', 'm', 'vn')
    manu_id_list.append(manu4.get_id())
    push(manu4)
    manu5 = Manufacturer('5555', 'm', 'vn')
    manu_id_list.append(manu5.get_id())
    push(manu5)


    # Create a new components
    mnf_id = '1111'
    if mnf_id in manu_id_list:
        cap = Capacitor(mnf_id, 20.0, '2020-01-01', 1, '1', 'g', 1, 1.0)
        push(cap)

    mnf_id = '2222'
    if mnf_id in manu_id_list:
        ic = IC(mnf_id, 20.0, '2020-01-01', 1, '2', 'h', 2, 2.0)
        push(ic)

    mnf_id = '3333'
    if mnf_id in manu_id_list:
        res = Resistor(mnf_id, 20.0, '2020-01-01', 1, '3', 'i', 3, 3.0)
        push(res)

    mnf_id = '4444'
    if mnf_id in manu_id_list:
        ind = Inductor(mnf_id, 20.0, '2020-01-01', 1, '4', 'j', 4, 4.0)
        push(ind)

    mnf_id = '5555'
    if mnf_id in manu_id_list:
        sen = Sensor(mnf_id, 20.0, '2020-01-01', 1, '5', 'k', 5, 'heat')
        push(sen)

    
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


'''
    Import section needs to be changed base on real project
'''




