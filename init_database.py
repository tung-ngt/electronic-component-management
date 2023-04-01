from models.db.database_with_classes import create_tables, delete_all_tables
from models.db.Utils_database import get_connection
conn, mycursor = get_connection('./data/electronic_store_with_classes.db')
delete_all_tables(conn)
create_tables(conn)