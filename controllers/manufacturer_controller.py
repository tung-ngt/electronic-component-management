from models.db.Utils_database import get_connection

def convert_list(items):
    return ",".join(f"{w}" for w in items)


def convert_condition(items: dict):
    x = ""
    for (column, value) in items.items():
        x += f" lower({column}) REGEXP lower(\'{value}\') and"
    x = x.rsplit(' ', 1)[0]
    return x


def filter_component(table: str, condition: dict, sort_option : str):
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
