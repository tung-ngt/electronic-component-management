import models.db.create_database as mktable 

if __name__ == "__main__":
    # Create db file in "models/db/electronic store.db"
    conn, cur = mktable.get_connection()
    mktable.delete_all_tables(conn)
    mktable.create_tables()
    