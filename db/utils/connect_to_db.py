from sqlite3 import connect
from .db_configs import DB_PATH

def get_connection():
    conn = connect(DB_PATH)
    cursor = conn.cursor()
    return conn, cursor

