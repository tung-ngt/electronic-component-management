from .utils import create_query, get_connection

def get_rows(
        table: str, 
        conditions: list[str] = [], 
        sort_options: dict[str, str] = {}
    ) -> list[list]:
    """Pull rows from database

    Parameters
    ----------
    conditions : list of conditions str example(["price = 2", "part_number like '123'"])
    sort_options : {column: direction}
    """
    conn, cursor = get_connection()
    
    query = create_query.select_from_table(table)
    
    if len(conditions) > 0:
        query += create_query.where_conditions(conditions)
    if len(sort_options) > 0:
        query += create_query.sort_by(sort_options)

    query += create_query.QUERY_END
    
    query_result = cursor.execute(query).fetchall()
    conn.close()
    
    return query_result

def get_distinct_column(table: str, column: str):
    conn, cursor = get_connection()

    query = create_query.distinct_column(table, column)
    query += create_query.QUERY_END

    query_result = cursor.execute(query).fetchall()
    conn.close()
    
    items = []
    for item in query_result:
        items.append(item[0])

    return items

