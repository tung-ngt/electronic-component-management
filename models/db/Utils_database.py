import sqlite3

def get_connection(filename : str):
    conn = sqlite3.connect(f'models/db/{filename}.db')
    cursor = conn.cursor()
    return conn, cursor

