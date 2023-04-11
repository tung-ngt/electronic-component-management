from .utils import create_query, get_connection, get_db_columns 

def create_row(table: str, values: list):
    conn, cursor = get_connection()
    query = create_query.insert_into(table, get_db_columns(table), values)
    query += create_query.QUERY_END
    with conn:
        cursor.execute(query)

def update_row(table: str, values: dict[str, str], key: tuple[str, str]):
    conn, cursor = get_connection()
    query = create_query.update_row(table, values, key)
    query += create_query.QUERY_END
    with conn:
        cursor.execute(query)

def create_rows(table, values: list[list[str]]):
    conn, cursor = get_connection()
    columns = get_db_columns(table)
    with conn:
        for v in values:
            query = create_query.insert_into(table, columns, v)
            query += create_query.QUERY_END
            cursor.execute(query)