import random
from models.pushpull.Pushpulltosql import pull, update, get_sub_category



# Test section    
def main():
    
    print('Capacitor: ',get_sub_category('capacitor'))
    print('Resistor: ',get_sub_category('resistor'))
    print('Inductor: ',get_sub_category('inductor'))
    print('Sensor: ',get_sub_category('sensor'))
    print('IC: ',get_sub_category('ic'))
    
    
    filters = {
    "mnf_id": "",
    "part_number": "MAX",
    "inventory_date" : [("<=",""), (">=", "")],
    "price" : [("<=",""), (">=", "")],
    "guarantee" : [("<=",""), (">=", "")],
    "sub_category" : [],
    "stock": [("<=",""), (">=", "")],
    "clock" : [("<=",""), (">=", "")],
    }

    # Pull from database
    cap_num, cap_list = pull('capacitor', {'mnf_id' : '05'}, [('guarantee')])
    ic_num, ic_list = pull(table = 'ic', condition = {'part_number' : 'BRM4555C-T'},sort_option = [('mnf_id', 'desc'), ('price', 'asc')])

    print("IC list:")
    if len(ic_list) == 0:
        print('No item found')
    else:
        print(ic_num)
        for item in ic_list:
            print(f'Part_num: {item.get_part_number()}, Manu_id: {item.get_mnf_id()}, Price: {item.get_price()}, Invent_date: {item.get_inventory_date()}, Guarantee: {item.get_guarantee()}, Clock: {item.get_clock()}, Stock: {item.get_stock()}')

    updated = update(table = 'ic', change = [('price', 2.5)], condition = 'BRM4555C-T')
    if updated == False:
        print('Update failed')

    ic_num, ic_list = pull(table = 'ic', condition = {'part_number' : 'BRM4555C-T'},sort_option = [('mnf_id', 'desc'), ('price', 'asc')])
    print("IC list:")
    if len(ic_list) == 0:
        print('No item found')
    else:
        print(ic_num)
        for item in ic_list:
            print(f'Part_num: {item.get_part_number()}, Manu_id: {item.get_mnf_id()}, Price: {item.get_price()}, Invent_date: {item.get_inventory_date()}, Guarantee: {item.get_guarantee()}, Clock: {item.get_clock()}, Stock: {item.get_stock()}')

        
    res_num, res_list = pull('resistor', {'price' : [('<', 4)]}, [('inventory_date')])
    ind_num, ind_list = pull('inductor', {'price' : [('<', 4)]}, [('stock')])
    sen_num, sen_list = pull('sensor', {'price' : [('<', 4)]}, [('price asc')])
    manu_num, manu_list = pull('manufacturer', {'name':'M'}, [('name')])
    

    # Print out the list
    print("Manu list: ")
    if len(manu_list) == 0:
        print('No item found')
    else:
        print(manu_num)
        for item in manu_list:
            print(f'Name: {item.get_name()}, ID: {item.get_id()}, Country: {item.get_country()}')

    print("Cap list:")
    if len(cap_list) == 0:
        print('No item found')
    else:
        print(cap_num)
        for item in cap_list:
            print(f'Part_num: {item.get_part_number()}, Manu_id: {item.get_mnf_id()}, Price: {item.get_price()}, Invent_date: {item.get_inventory_date()},  Guarantee: {item.get_guarantee()}, Capacitance: {item.get_capacitance()}, Stock: {item.get_stock()}')

    

    print("Res list:")
    if len(res_list) == 0:
        print('No item found')
    else:
        print(res_num)
        for item in res_list:
            print(f'Part_num: {item.get_part_number()}, Manu_id: {item.get_mnf_id()}, Price: {item.get_price()}, Invent_date: {item.get_inventory_date()}, Guarantee: {item.get_guarantee()}, Resistance: {item.get_resistance()}, Stock: {item.get_stock()}')

    print("Ind list:")
    if len(ind_list) == 0:
        print('No item found')
    else:
        print(ind_num)
        for item in ind_list:
            print(f'Part_num: {item.get_part_number()}, Manu_id: {item.get_mnf_id()}, Price: {item.get_price()}, Invent_date: {item.get_inventory_date()}, Guarantee: {item.get_guarantee()}, Inductance: {item.get_inductance()}, Stock: {item.get_stock()}')

    print("Sen list:")
    if len(sen_list) == 0:
        print('No item found')
    else:
        print(sen_num)
        for item in sen_list:
            print(f'Part_num: {item.get_part_number()}, Manu_id: {item.get_mnf_id()}, Price: {item.get_price()}, Invent_date: {item.get_inventory_date()}, Guarantee: {item.get_guarantee()}, Sensor_type: {item.get_sensor_type()}, Stock: {item.get_stock()}')
    



if __name__ == '__main__':
    main()
 