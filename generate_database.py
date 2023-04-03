from models.db.create_database import create_tables, delete_all_tables
from models.db.utils.connect_to_db import get_connection
conn, mycursor = get_connection('./data/database.db')
delete_all_tables(conn)
create_tables()