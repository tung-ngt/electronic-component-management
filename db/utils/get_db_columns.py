from .db_configs import *

def get_db_columns(table: str) -> list[str]:
    if table == "manufacturer":
        return MANUFACTURER_COLUMNS.copy()
    
    if table == "customer":
        return CUSTOMER_COLUMNS.copy()
    
    if table == "orders":
        return ORDER_COLUMNS.copy()

    columns = COMPONENT_COLUMNS.copy()
    columns[-1] = COMPONENT_SPECIAL_ATTR[table]
    return columns
    
