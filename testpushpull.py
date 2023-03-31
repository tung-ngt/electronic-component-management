from models.pushpull.Pushpulltosql import pull
from models.db.Utils_database import get_connection
from models.db.database_with_classes import create_tables, delete_all_tables



# Test section    
def main():
    # Connect to database
    conn, mycursor = get_connection('./data/electronic_store_with_classes.db')
    delete_all_tables(conn)
    create_tables()
  
    # Pull from database
    cap_num, cap_list = pull('capacitor', {'price' : [('>', 4)]})
    ic_num, ic_list = pull('ic', {'price' : [('>', 4)]})
    res_num, res_list = pull('resistor', {'price' : [('>', 4)]})
    ind_num, ind_list = pull('inductor', {'price' : [('>', 4)]})
    sen_num, sen_list = pull('sensor', {'price' : [('>', 4)]})
    manu_num, manu_list = pull('manufacturer')
    

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

    print("IC list:")
    if len(ic_list) == 0:
        print('No item found')
    else:
        print(ic_num)
        for item in ic_list:
            print(f'Part_num: {item.get_part_number()}, Manu_id: {item.get_mnf_id()}, Price: {item.get_price()}, Invent_date: {item.get_inventory_date()}, Guarantee: {item.get_guarantee()}, Clock: {item.get_clock()}, Stock: {item.get_stock()}')

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
 