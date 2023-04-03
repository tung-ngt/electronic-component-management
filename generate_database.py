from models.db.create_database import create_tables, delete_all_tables
from models.db.utils.connect_to_db import get_connection
conn, mycursor = get_connection('./data/electronic_store_with_classes.db')
delete_all_tables(conn)
create_tables()