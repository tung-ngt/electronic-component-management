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
            x += f" lower({column}) REGEXP lower(\'{value}\') and"
        elif category_search[column] == 'val':
            x += f" {column} = \'{value}\' and"
        elif category_search[column] == "val_list":
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


def filter_component(table: str, condition: dict, sort_option: str):
    '''
    Filter component by condition and sort by sort_option (optional)
    '''
    conn, c = get_connection('./data/electronic_store_with_classes.db')
    query = f"""select * from {table}"""
    if len(condition) > 0 and len(sort_option) > 0:
        query += f" where {convert_condition(condition)} order by {sort_option};"
    elif len(condition) > 0:
        query += f" where {convert_condition(condition)};"
    elif len(sort_option) > 0:
        query += f" order by {sort_option};"

    # print(query)
    c.execute(query)
    items = c.fetchall()
    conn.close()
    return items

def filter_manufacturer(table: str, condition: dict, sort_option : str):
    '''
    Filter component by condition and sort by sort_option (optional)
    '''
    conn, c = get_connection('./data/electronic_store_with_classes.db')
    query = f"""select * from {table}"""
    if len(condition) > 0 and len(sort_option) > 0:
        query += f" where {convert_condition(condition)} order by {sort_option};"
    elif len(condition) > 0:
        query += f" where {convert_condition(condition)};"
    elif len(sort_option) > 0:
        query += f" order by {sort_option};"

    print(query)
    c.execute(query)
    items = c.fetchall()
    conn.close()
    return items


def count_condition(table: str, condition: dict):
    conn, c = get_connection('./data/electronic_store_with_classes.db')
    query = f"""select count(*) from {table}"""
    if len(condition) > 0:
        query += f""" where {convert_condition(condition)}"""
    c.execute(query)
    items = c.fetchall()
    conn.close()
    return items
