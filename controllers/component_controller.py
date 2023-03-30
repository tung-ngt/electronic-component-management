import sqlite3
import numbers

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

# Should change base on where the db file is
def connection():
    conn = sqlite3.connect('electronic_store.db')
    c = conn.cursor()
    return (conn, c)


def convert_list(table, items):

    x = f"insert into {table} values ("
    for i in items:
        if isinstance(i, numbers.Number):
            x += str(i) + ","
        else:
            x += i + ","
    x = x[:-1] + ")"
    return x


def convert_condition(items: dict):
    x = ""
    for (column, value) in items.items():
        if category_search[column] == "search":
            x += f" REGEXP_LIKE({column}, \'{value}\', 'i') and"
        elif category_search[column] == 'val':
            x += f" {column} = \'{value}\' and"
        elif category_search[column] == "val_list":
            x+= f" {column} in ({convert_list(value)}) and"
        else:
            for sign, condition in value:
                x += f"{column} {sign} {condition} and "
    x = x.rsplit(' ', 1)[0] + ";"
    return x


def filter_component(table: str, condition: dict) -> None:
    conn, c = connection()
    query = f"""select * from {table}"""
    if len(condition) > 0:
        query += f"""where {convert_condition(condition)}"""

    # print(query)
    c.execute(query)
    items = c.fetchall()
    conn.close()
    return items


def count_condition(table: str, condition: dict):
    conn, c = connection()
    query = f"""select count(*) from {table}"""
    if len(condition) > 0:
        query += f""" where {convert_condition(condition)}"""
    c.execute(query)
    items = c.fetchall()
    conn.close()
    return items


