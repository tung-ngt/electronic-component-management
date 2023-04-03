from sqlite3 import connect

def get_connection(filepath : str):
    conn = connect(filepath)
    cursor = conn.cursor()
    return conn, cursor

