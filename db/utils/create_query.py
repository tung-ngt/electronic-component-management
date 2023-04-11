SELECT_TABLE = "SELECT {columns} FROM {tables} "
INSERT_INTO = "INSERT INTO {table} ({columns}) VALUES ({values}) "
QUERY_END = ";"
WHERE = "WHERE {conditions} "
AND = " AND "
LIKE = "LOWER({column}) LIKE LOWER('%{value}%') "
START_FROM = "{column} >= '{value}' "
UPTO = "{column} <= '{value}' "
CONTAINS = "{column} IN ({values}) "
ORDER_BY = "ORDER BY {options} "
UPDATE_ROW = "UPDATE {table} SET {values} "
DISTINC_COLUMN = "SELECT DISTINCT {column} FROM {table} "
DROP_TABLE = "DROP TABLE {table} "
GET_TABLES = "SELECT name FROM sqlite_schema WHERE type='table' "

def drop_table(table: str):
    return DROP_TABLE.format(table=table)

def get_tables():
    return GET_TABLES

def separated_list(values_list: list[str], separator=", ", wrapped=False):
    if wrapped:
        values_list = [f"'{value}'" for value in values_list]
    
    return separator.join(values_list)


def select_from_table(tables: str or list[str], columns: str or list[str]="*") -> str:
    if isinstance(tables, list):
        tables = separated_list(tables)
    
    if isinstance(columns, list):
        columns = separated_list(columns)
    
    return SELECT_TABLE.format(columns=columns, tables=tables)

def insert_into(table: str, columns: list[str], values: list) -> str:
    columns = separated_list(columns)
    values = separated_list(values, wrapped=True)
    return INSERT_INTO.format(table=table, columns=columns, values=values)


def where_conditions(conditions: list[str]) -> str:
    """Return the where clause
    
    Parameters
    ----------
    conditions: [str] example(["price between 2 and 6", "name = '123'"])
    -> price between 2 and 6 AND name = '123'
    """
    return WHERE.format(conditions=separated_list(conditions, AND))

def like(column: str, value: str) -> str:
    return LIKE.format(column=column, value=value)

def start_from(column: str, value: str) -> str:
    return START_FROM.format(column=column, value=value)

def upto(column: str, value: str) -> str:
    return UPTO.format(column=column, value=value)

def contains(column: str, values: list[str]) -> str:
    values = separated_list(values, wrapped=True)
    return CONTAINS.format(column=column, values=values)

def sort_by(sort_options: dict[str, str]) -> str:
    options = []
    for sort_option in list(sort_options.items()):
        options.append(separated_list(sort_option, " "))
    return ORDER_BY.format(options=separated_list(options))
    
def update_row(table: str, values: dict[str, str], key: tuple[str, str]) -> str:
    set_values = []
    for column, value in list(values.items()):
        set_values.append(f"{column} = '{value}'")
    query = UPDATE_ROW.format(table=table, values=separated_list(set_values))
    query += WHERE.format(conditions=f"{key[0]} = '{key[1]}'")
    return query

def distinct_column(table: str, column: str) -> str:
    return DISTINC_COLUMN.format(table=table, column=column)