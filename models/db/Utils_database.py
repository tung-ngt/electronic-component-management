import sqlite3

def get_connection(filepath : str):
    conn = sqlite3.connect(filepath)
    cursor = conn.cursor()
    return conn, cursor

