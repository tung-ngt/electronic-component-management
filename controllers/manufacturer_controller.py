from models.db.Utils_database import get_connection

def convert_list(items):
    return ",".join(f"{w}" for w in items)


def convert_condition(items: dict):
    x = ""
    for (column, value) in items.items():
        x += f"REGEXP_LIKE({column}, \'{value}\', 'i') and"
    x = x.rsplit(' ', 1)[0] + ";"
    return x


def filter_component(table: str, condition: dict):
    conn, c = get_connection('electronic_store_with_classes')
    query = f"""select * from {table}"""
    print(query)
    if len(condition) > 0:
        query += f"""where {convert_condition(condition)}"""

    print(query)
    c.execute(query)
    items = c.fetchall()
    conn.close()
    return items


def count_condition(table: str, condition: dict):
    conn, c = get_connection('electronic_store_with_classes')
    query = f"""select count(*) from {table}"""
    if len(condition) > 0:
        query += f""" where {convert_condition(condition)}"""
    c.execute(query)
    items = c.fetchall()
    conn.close()
    return items
