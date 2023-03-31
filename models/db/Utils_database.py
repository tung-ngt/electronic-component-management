import sqlite3

def get_connection(filename):
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()
    return conn, cursor

