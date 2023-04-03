from models.domains import Component, Capacitor, Resistor, Inductor, Sensor, IC, Manufacturer

'''
    Import section needs to be changed base on real project
'''

# Index
index_compo = {'part_number' : 0, 'mnf_id' : 1, 'price' : 2, 
         'inventory_date' : 3, 'guarantee' : 4, 'special_att' : 5,
         'sub_category' : 6, 'stock' : 7}

index_manu = {'name' : 0, 'ID' : 1, 'country' : 2}


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
        image_path = thing.get_image_path()
        return mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock, image_path

    elif type(thing).__name__ == 'Manufacturer':
        name = thing.get_name()
        ID = thing.get_id()
        country = thing.get_country()
        image_path = thing.get_image_path()
        return name, ID, country, image_path

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
    

