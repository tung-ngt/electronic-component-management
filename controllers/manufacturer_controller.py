import sqlite3

# Should change base on where the db file is


def connection():
    conn = sqlite3.connect('electronic_store.db')
    c = conn.cursor()
    return (conn, c)


def convert_list(items):
    return ",".join(f"{w}" for w in items)


def convert_condition(items: dict):
    x = ""
    for (column, value) in items.items():
        x += f"REGEXP_LIKE({column}, \'{value}\', 'i') and"
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
