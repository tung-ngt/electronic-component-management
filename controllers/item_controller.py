import numbers
from models.db.Utils_database import get_connection

category_search = {"mnf_id": "search",
                   "part_number": "search",
                   "inventory_date": "range",
                   "price": "range",
                   "guarantee": "range",
                   "sub_category": "val_list",
                   "stock": "range",
                   "capacitance": "range",
                   "clock": "range",
                   "inductance": "range",
                   "resistance": "range",
                   "sensor_type": "val_list"
                   }


def convert_list(items):
    x = ""
    for i in items:
        if isinstance(i, numbers.Number):
            x += str(i) + ","
        else:
            x += f"\'{i}\',"
    x = x[:-1]
    return x


def convert_condition(items: dict):
    """
    Convert condition to string to execute 
    """
    x = ""
    for (column, value) in items.items():
        if category_search[column] == "search":
            x += f" lower({column}) like lower(\'%{value}%\') and"
        elif category_search[column] == 'val':
            x += f" {column} = \'{value}\' and"
        elif category_search[column] == "val_list":
            if len(value) == 0:
               continue
            x += f" {column} in ({convert_list(value)}) and"
        else:
            for sign, condition in value:
                if not isinstance(condition, str) or len(condition) != 0:
                    x += f" {column} {sign} \'{condition}\' and"
    x = x.rsplit(' ', 1)[0]
    return x

def convert_mnf_condition(items: dict):
    x = ""
    for (column, value) in items.items():
        x += f" lower({column}) like lower(\'%{value}%\') and"
    x = x.rsplit(' ', 1)[0]
    return x


# Specific sort function for each column
def sort_by_price(table : str):
    conn, c = get_connection('./data/electronic_store_with_classes.db')
    query = f"""select * from {table} order by price;"""
    c.execute(query)
    items = c.fetchall()
    conn.close()
    return len(items), items

def sort_by_guarantee(table : str):
    conn, c = get_connection('./data/electronic_store_with_classes.db')
    query = f"""select * from {table} order by guarantee;"""
    c.execute(query)
    items = c.fetchall()
    conn.close()
    return len(items), items

def sort_by_stock(table : str):
    conn, c = get_connection('./data/electronic_store_with_classes.db')
    query = f"""select * from {table} order by stock;"""
    c.execute(query)
    items = c.fetchall()
    conn.close()
    return len(items), items

def sort_by_inventory_date(table : str):
    conn, c = get_connection('./data/electronic_store_with_classes.db')
    query = f"""select * from {table} order by inventory_date;"""
    c.execute(query)
    items = c.fetchall()
    conn.close()
    return len(items), items

def sort_by_mnf_id(table : str):
    conn, c = get_connection('./data/electronic_store_with_classes.db')
    query = f"""select * from {table} order by mnf_id;"""
    c.execute(query)
    items = c.fetchall()
    conn.close()
    return len(items), items

def sort_by_part_number(table : str):
    conn, c = get_connection('./data/electronic_store_with_classes.db')
    query = f"""select * from {table} order by part_number;"""
    c.execute(query)
    items = c.fetchall()
    conn.close()
    return len(items), items

def sort_by_sub_category(table : str):
    conn, c = get_connection('./data/electronic_store_with_classes.db')
    query = f"""select * from {table} order by sub_category;"""
    c.execute(query)
    items = c.fetchall()
    conn.close()
    return len(items), items

def sort_by_special_att(table : str):
    conn, c = get_connection('./data/electronic_store_with_classes.db')
    if table == 'capacitor':
        query = f"select * from {table} order by capacitance;"
    elif table == 'inductor':
        query = f"select * from {table} order by inductance;"
    elif table == 'resistor':
        query = f"select * from {table} order by resistance;"
    elif table == 'sensor':
        query = f"select * from {table} order by sensor_type;"  
    elif table == 'ic':
        query = f"select * from {table} order by clock;"

    c.execute(query)
    items = c.fetchall()
    conn.close()
    return len(items), items

def filter_component(table: str, condition: dict, sort_option: str):
    '''
    Filter component by condition and sort by sort_option (optional)

    Example: filter_component("capacitor", "table name"
                             {"price": [(">", 1000), ("<", 2000)], "where condition"
                             "price", "order condition", default is from low to high)
    '''
    conn, c = get_connection('./data/electronic_store_with_classes.db')
    query = f"""select * from {table}"""
    if len(condition) > 0 and len(sort_option) > 0:
        query += f" where {convert_condition(condition)} order by {sort_option};"
    elif len(condition) > 0:
        query += f" where {convert_condition(condition)};"
    elif len(sort_option) > 0:
        query += f" order by {sort_option};"

    #print(query)
    c.execute(query)
    items = c.fetchall()
    conn.close()
    return len(items), items

def filter_manufacturer(table: str, condition: dict, sort_option : str):
    '''
    Filter component by condition and sort by sort_option (optional)
    '''
    conn, c = get_connection('./data/electronic_store_with_classes.db')
    query = f"""select * from {table}"""
    if len(condition) > 0 and len(sort_option) > 0:
        query += f" where {convert_mnf_condition(condition)} order by {sort_option};"
    elif len(condition) > 0:
        query += f" where {convert_mnf_condition(condition)};"
    elif len(sort_option) > 0:
        query += f" order by {sort_option};"

    #print(query)
    c.execute(query)
    items = c.fetchall()
    conn.close()
    return len(items), items


