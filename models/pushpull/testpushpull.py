from Pushpulltosql import push, pull
from db.Utils_database import get_connection
from db.database_with_classes import create_tables, delete_all_tables



# Test section    
def main():
    # Connect to database
    conn, mycursor = get_connection('electronic_store_with_classes')
    delete_all_tables(conn)
    create_tables()
  
    # Pull from database
    cap_list = pull('capacitor', 'price > 4')
    ic_list = pull('ic', 'price < 10')
    res_list = pull('resistor', 'price > 5')
    ind_list = pull('inductor', 'price < 10')
    sen_list = pull('sensor', 'price >20')
    manu_list = pull('manufacturer')

    # Print out the list
    print("Manu list:")
    for item in manu_list:
        print(f'Name: {item.get_name()}, ID: {item.get_id()}, Country: {item.get_country()}')

    print("Cap list:")
    for item in cap_list:
        print(f'Part_num: {item.get_part_number()}, Manu_id: {item.get_mnf_id()},\
                Price: {item.get_price()}, Invent_date: {item.get_inventory_date()},\
                Guarantee: {item.get_guarantee()}, Capacitance: {item.get_capacitance()}, Stock: {item.get_stock()}')

    print("IC list:")
    for item in ic_list:
        print(f'Part_num: {item.get_part_number()}, Manu_id: {item.get_mnf_id()},\
                Price: {item.get_price()}, Invent_date: {item.get_inventory_date()},\
                Guarantee: {item.get_guarantee()}, Clock: {item.get_clock()}, Stock: {item.get_stock()}')

    print("Res list:")
    for item in res_list:
        print(f'Part_num: {item.get_part_number()}, Manu_id: {item.get_mnf_id()},\
                Price: {item.get_price()}, Invent_date: {item.get_inventory_date()},\
                Guarantee: {item.get_guarantee()}, Resistance: {item.get_resistance()}, Stock: {item.get_stock()}')

    print("Ind list:")
    for item in ind_list:
        print(f'Part_num: {item.get_part_number()}, Manu_id: {item.get_mnf_id()},\
                Price: {item.get_price()}, Invent_date: {item.get_inventory_date()},\
                Guarantee: {item.get_guarantee()}, Inductance: {item.get_inductance()}, Stock: {item.get_stock()}')

    print("Sen list:")
    for item in sen_list:
        print(f'Part_num: {item.get_part_number()}, Manu_id: {item.get_mnf_id()},\
                Price: {item.get_price()}, Invent_date: {item.get_inventory_date()},\
                Guarantee: {item.get_guarantee()}, Sensor_type: {item.get_sensor_type()}, Stock: {item.get_stock()}')
    



if __name__ == '__main__':
    main()
 